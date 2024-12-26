from typing import List, Set, Tuple
import heapq
from itertools import combinations
from collections import defaultdict

class Solution:
    def _best_path(self, grid: List[List[str]], start_row: int, start_col: int):
        pq = [(0, start_row, start_col, [])] # cost, row, col, path
        visited = set()
        while pq:
            cost, row, col, path = heapq.heappop(pq)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == "#":
                continue
            if grid[row][col] == "E":
                return path + [(row, col, cost)]
            
            row_dirs = [-1, 0, 1, 0]
            col_dirs = [0, 1, 0, -1]
            for i in range(4):
                heapq.heappush(pq, (cost + 1, row + row_dirs[i], col + col_dirs[i], path + [(row, col, cost)]))

    def _get_possible_cheats(self, path: Set[Tuple[int, int, int]], cheat_length: int):
        shortcuts = {}
        for (start_row, start_col, start_distance) in path:
            for (end_row, end_col, end_distance) in path:
                distance = abs(end_row - start_row) + abs(end_col - start_col)
                if distance <= cheat_length:
                    savings = end_distance - start_distance - distance
                    if savings >= 100:
                        shortcuts[((start_row, start_col), (end_row, end_col))] = savings
        return shortcuts

    def find_cheats(self, grid: List[List[str]], cheat_length: int):
        # Find start row and col and wall coords
        wall_coords = []
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "S":
                    start_row = row
                    start_col = col
                    path = self._best_path(grid, start_row, start_col)
                elif char == "#":
                    wall_coords.append((row, col))

        return len(self._get_possible_cheats(path, cheat_length))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        for row in grid]))

        print(Solution().find_cheats(grid, 2))
        print(Solution().find_cheats(grid, 20))
