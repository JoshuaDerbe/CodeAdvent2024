from typing import List
import re
import heapq

class Solution:
    def calc_shortest_path(self, grid: List[List[int]], ):
        pq = [(0, 0, 0)] # cost, row, col
        visited = set()
        while pq:
            cost, row, col = heapq.heappop(pq)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue
            if grid[row][col] == "#":
                continue
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return cost
            
            row_dirs = [-1, 0, 1, 0]
            col_dirs = [0, 1, 0, -1]
            for i in range(4):
                heapq.heappush(pq, (cost + 1, row + row_dirs[i], col + col_dirs[i]))


        return 0
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        GRID_SIZE = 71
        CORRUPT_COUNT = 1024
        grid = [["." for _ in range(GRID_SIZE)] for _ in range (GRID_SIZE)]
        corrupt_count = 0
        for line in file:
            corrupt_count += 1
            m = re.findall("^(\d+),(\d+)$", line.strip())
            grid[int(m[0][1])][int(m[0][0])] = "#"
            if corrupt_count >= CORRUPT_COUNT:
                break

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in grid]))
        print(Solution().calc_shortest_path(grid))