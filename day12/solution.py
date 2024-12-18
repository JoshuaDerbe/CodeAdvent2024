from typing import List, Set, Tuple
from collections import deque

class Solution:
    def _region_bfs(self, start_row: int, start_col: int, grid: List[List[str]], plant: str, seen_coords: Set[Tuple[int, int]]):
        area = 0
        perimeter = 0
        queue = deque()
        queue.append((start_row, start_col))
        seen_coords.add((start_row, start_col))
        while queue:
            cur = queue.popleft()
            area += 1

            row_dirs = [-1, 0, 1, 0]
            col_dirs = [0, 1, 0, -1]
            for i in range(4):
                row = cur[0]
                col = cur[1]
                new_row = row + row_dirs[i]
                new_col = col + col_dirs[i]
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] != plant:
                    perimeter += 1
                elif (new_row, new_col) not in seen_coords:
                    seen_coords.add((new_row, new_col))
                    queue.append((new_row, new_col))

        return area * perimeter

    def calculate_fence_price(self, grid: List[List[str]]) -> int:
        total_price = 0

        seen_coords = set()
        for row, line in enumerate(grid):
            for col, plant in enumerate(line):
                if (row, col) not in seen_coords:
                    total_price += self._region_bfs(row, col, grid, plant, seen_coords)


        return total_price
    
class SolutionPart2:
    def _region_bfs(self, start_row: int, start_col: int, grid: List[List[str]], plant: str, seen_coords: Set[Tuple[int, int]]):
        direction_mapper = {
            (-1, 0): "^",
            (0, 1): ">",
            (1, 0): "v",
            (0, -1): "<"
        }
        row_dirs = [-1, 0, 1, 0]
        col_dirs = [0, 1, 0, -1]
        area = 0
        side_set = set()
        queue = deque()
        queue.append((start_row, start_col))
        seen_coords.add((start_row, start_col))
        while queue:
            cur = queue.popleft()
            area += 1

            for i in range(4):
                row = cur[0]
                col = cur[1]
                new_row = row + row_dirs[i]
                new_col = col + col_dirs[i]
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] != plant:
                    side_set.add((direction_mapper[(row_dirs[i], col_dirs[i])], (row, col)))
                elif (new_row, new_col) not in seen_coords:
                    seen_coords.add((new_row, new_col))
                    queue.append((new_row, new_col))

        final_sides = set()

        looking_up_sides = sorted([side for side in side_set if side[0] == "^"], key=lambda tup: (tup[1][0], tup[1][1]))
        cur_row = None
        cur_col = None
        for upside in looking_up_sides:
            if upside[1][0] != cur_row or upside[1][1] != cur_col + 1:
                cur_row = upside[1][0]
                cur_col = upside[1][1]
                final_sides.add(upside)
            else: cur_col += 1

        looking_down_sides = sorted([side for side in side_set if side[0] == "v"], key=lambda tup: (tup[1][0], tup[1][1]))
        cur_row = None
        cur_col = None
        for downside in looking_down_sides:
            if downside[1][0] != cur_row or downside[1][1] != cur_col + 1:
                cur_row = downside[1][0]
                cur_col = downside[1][1]
                final_sides.add(downside)
            else: cur_col += 1

        looking_right_sides = sorted([side for side in side_set if side[0] == ">"], key=lambda tup: (tup[1][1], tup[1][0]))
        cur_row = None
        cur_col = None
        for rightside in looking_right_sides:
            if rightside[1][1] != cur_col or rightside[1][0] != cur_row + 1:
                cur_row = rightside[1][0]
                cur_col = rightside[1][1]
                final_sides.add(rightside)
            else: cur_row += 1

        looking_left_sides = sorted([side for side in side_set if side[0] == "<"], key=lambda tup: (tup[1][1], tup[1][0]))
        cur_row = None
        cur_col = None
        for leftside in looking_left_sides:
            if leftside[1][1] != cur_col or leftside[1][0] != cur_row + 1:
                cur_row = leftside[1][0]
                cur_col = leftside[1][1]
                final_sides.add(leftside)
            else: cur_row += 1

        return area * len(final_sides)

    def calculate_fence_price_part2(self, grid: List[List[str]]) -> int:
        total_price = 0

        seen_coords = set()
        for row, line in enumerate(grid):
            for col, plant in enumerate(line):
                if (row, col) not in seen_coords:
                    total_price += self._region_bfs(row, col, grid, plant, seen_coords)


        return total_price
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in grid]))
        print(Solution().calculate_fence_price(grid))
        print(SolutionPart2().calculate_fence_price_part2(grid))
