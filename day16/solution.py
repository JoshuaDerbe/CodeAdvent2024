from typing import List
from collections import deque
import heapq

class Solution:
    def _bfs(self, grid: List[List[str]], start_row: int, start_col: int, start_direction: str):
        direction_mapper = {
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1),
            "^": (-1, 0)
        }
        rotate_clockwise_mapper = {
            ">": "v",
            "v": "<",
            "<": "^",
            "^": ">"
        }
        rotate_anticlockwise_mapper = {
            ">": "^",
            "^": "<",
            "<": "v",
            "v": ">"
        }
        pq = [(0, start_row, start_col, start_direction)]
        visited = set()
        while pq:
            cost, row, col, direction = heapq.heappop(pq)

            if (row, col, direction) in visited:
                continue
            visited.add((row, col, direction))

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == "#":
                continue
            if grid[row][col] == "E":
                return cost

            heapq.heappush(pq, (cost + 1, row + direction_mapper[direction][0], col + direction_mapper[direction][1], direction))

            cw_dir = rotate_clockwise_mapper[direction]
            heapq.heappush(pq, (cost + 1001, row + direction_mapper[cw_dir][0], col + direction_mapper[cw_dir][1], cw_dir))

            acw_dir = rotate_anticlockwise_mapper[direction]
            heapq.heappush(pq, (cost + 1001, row + direction_mapper[acw_dir][0], col + direction_mapper[acw_dir][1], acw_dir))

            flipped_dir = rotate_clockwise_mapper[cw_dir]
            heapq.heappush(pq, (cost + 2001, row + direction_mapper[flipped_dir][0], col + direction_mapper[flipped_dir][1], flipped_dir))

        return float("inf")

    def find_best_score(self, grid: List[List[str]]) -> int:
        best_score = 0

        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "S":
                    best_score = self._bfs(grid, row, col, ">")

        return best_score
    
class SolutionPart2:
    def _bfs(self, grid: List[List[str]], start_row: int, start_col: int, start_direction: str):
        direction_mapper = {
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1),
            "^": (-1, 0)
        }
        rotate_clockwise_mapper = {
            ">": "v",
            "v": "<",
            "<": "^",
            "^": ">"
        }
        rotate_anticlockwise_mapper = {
            ">": "^",
            "^": "<",
            "<": "v",
            "v": ">"
        }
        pq = [(0, start_row, start_col, start_direction, [(start_row, start_col, start_direction)])]
        min_cost = {} 
        best_paths = []
        best_cost = float("inf")
        while pq:
            cost, row, col, direction, path = heapq.heappop(pq)

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "#":
                continue

            if cost > best_cost:
                continue

            if (row, col, direction) in min_cost and cost > min_cost[(row, col, direction)]:
                continue
            min_cost[(row, col, direction)] = cost

            if grid[row][col] == "E":
                if cost < best_cost:
                    best_cost = cost
                    best_paths = [path]
                elif cost == best_cost:
                    best_paths.append(path)
                continue

            f_row = row + direction_mapper[direction][0]
            f_col = col + direction_mapper[direction][1]
            heapq.heappush(pq, (cost + 1, f_row, f_col, direction, path + [(f_row, f_col, direction)]))

            cw_dir = rotate_clockwise_mapper[direction]
            cw_row = row + direction_mapper[cw_dir][0]
            cw_col = col + direction_mapper[cw_dir][1]
            heapq.heappush(pq, (cost + 1001, cw_row, cw_col, cw_dir, path + [(cw_row, cw_col, cw_dir)]))

            acw_dir = rotate_anticlockwise_mapper[direction]
            acw_row = row + direction_mapper[acw_dir][0]
            acw_col = col + direction_mapper[acw_dir][1]
            heapq.heappush(pq, (cost + 1001, acw_row, acw_col, acw_dir, path + [(acw_row, acw_col, acw_dir)]))

            flipped_dir = rotate_clockwise_mapper[cw_dir]
            flipped_row = row + direction_mapper[flipped_dir][0]
            flipped_col = col + direction_mapper[flipped_dir][1]
            heapq.heappush(pq, (cost + 2001, flipped_row, flipped_col, flipped_dir, path + [(flipped_row, flipped_col, flipped_dir)]))

        return best_cost, best_paths

    def find_best_score(self, grid: List[List[str]]) -> int:
        best_score = 0
        paths = []

        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "S":
                    best_score, paths = self._bfs(grid, row, col, ">")

        tile_set = set()
        for path in paths:
            for coords in path:
                tile_set.add((coords[0], coords[1]))

        return len(tile_set)
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append(list(line.strip()))

        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        for row in grid]))

        #print(Solution().find_best_score(grid))
        print(SolutionPart2().find_best_score(grid))