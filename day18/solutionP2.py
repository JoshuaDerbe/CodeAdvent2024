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


        return -1
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        GRID_SIZE = 71
        grid = [["." for _ in range(GRID_SIZE)] for _ in range (GRID_SIZE)]
        corruptions = []
        for line in file:
            m = re.findall("^(\d+),(\d+)$", line.strip())
            corrupt_row = int(m[0][1])
            corrupt_col = int(m[0][0])
            corruptions.append((corrupt_row, corrupt_col))
            grid[int(m[0][1])][int(m[0][0])] = "#"
            res = Solution().calc_shortest_path(grid)
            if res == -1:
                print(f"{corrupt_col},{corrupt_row}")
                break

