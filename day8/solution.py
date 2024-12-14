from typing import List, Tuple
from collections import defaultdict
from itertools import combinations
from copy import deepcopy

class Solution:
    def _check_on_grid(self, coord: Tuple[int, int], grid: List[List[str]]) -> bool:
        if coord[0] < 0 or coord[0] >= len(grid) or coord[1] < 0 or coord[1] >= len(grid[0]):
            return False
        return True

    def count_antinodes(self, grid: List[List[str]]) -> int:
        antinode_coords = set()

        antenna_map = defaultdict(list)
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char != ".":
                    antenna_map[char].append((row, col))

        for char, coords in antenna_map.items():
            combos = list(combinations(coords, 2))
            for combo in combos:
                diff = (combo[1][0] - combo[0][0], combo[1][1] - combo[0][1])
                antinode1 = (combo[1][0] + diff[0], combo[1][1] + diff[1])
                antinode2 = (combo[0][0] - diff[0], combo[0][1] - diff[1])
                if self._check_on_grid(antinode1, grid):
                    antinode_coords.add(antinode1)
                    if grid[antinode1[0]][antinode1[1]] == ".":
                        grid[antinode1[0]][antinode1[1]] = "#"
                if self._check_on_grid(antinode2, grid):
                    antinode_coords.add(antinode2)
                    if grid[antinode2[0]][antinode2[1]] == ".":
                        grid[antinode2[0]][antinode2[1]] = "#"

        return len(antinode_coords)
    

    def count_antinodes_part2(self, grid: List[List[str]]) -> int:
        antinode_coords = set()

        antenna_map = defaultdict(list)
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char != ".":
                    antenna_map[char].append((row, col))
                    antinode_coords.add((row, col))


        for char, coords in antenna_map.items():
            combos = list(combinations(coords, 2))
            for combo in combos:
                diff = (combo[1][0] - combo[0][0], combo[1][1] - combo[0][1])
                # Check one direction
                dir1 = (combo[1][0] + diff[0], combo[1][1] + diff[1])
                while self._check_on_grid(dir1, grid):
                    antinode_coords.add(dir1)
                    if grid[dir1[0]][dir1[1]] == ".":
                        grid[dir1[0]][dir1[1]] = "#"
                    dir1 = (dir1[0] + diff[0], dir1[1] + diff[1])
                # Check next direction
                dir2 = (combo[0][0] - diff[0], combo[0][1] - diff[1])
                while self._check_on_grid(dir2, grid):
                    antinode_coords.add(dir2)
                    if grid[dir2[0]][dir2[1]] == ".":
                        grid[dir2[0]][dir2[1]] = "#"
                    dir2 = (dir2[0] - diff[0], dir2[1] - diff[1])

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in grid]))
        return len(antinode_coords)
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        
        print(Solution().count_antinodes(deepcopy(grid)))
        print(Solution().count_antinodes_part2(deepcopy(grid)))
