from typing import List, Set, Tuple

class Solution:
    def _dfs_hike_score(self, grid: List[List[int]], row: int, col: int, prev_num: int, visited_nines: Set[Tuple[int, int]]) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        cur_num = grid[row][col]
        if cur_num != prev_num + 1:
            return
        if cur_num == 9:
            # Success
            visited_nines.add((row, col))
            return
        
        row_dirs = [-1, 0, 1, 0]
        col_dirs = [0, 1, 0, -1]
        for i in range(4):
            self._dfs_hike_score(grid, row + row_dirs[i], col + col_dirs[i], cur_num, visited_nines)

        return visited_nines
    
    def _dfs_hike_score_pt2(self, grid: List[List[int]], row: int, col: int, prev_num: int) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        cur_num = grid[row][col]
        if cur_num != prev_num + 1:
            return 0
        if cur_num == 9:
            # Success
            return 1
        
        score = 0
        row_dirs = [-1, 0, 1, 0]
        col_dirs = [0, 1, 0, -1]
        for i in range(4):
            score += self._dfs_hike_score_pt2(grid, row + row_dirs[i], col + col_dirs[i], cur_num)

        return score

    def calculate_hiking(self, grid: List[List[int]]) -> int:
        total_score = 0

        for row, line in enumerate(grid):
            for col, height in enumerate(line):
                if height == 0:
                    total_score += len(self._dfs_hike_score(grid, row, col, -1, set()))

        return total_score
    
    def calculate_hiking_pt2(self, grid: List[List[int]]) -> int:
        total_score = 0

        for row, line in enumerate(grid):
            for col, height in enumerate(line):
                if height == 0:
                    total_score += self._dfs_hike_score_pt2(grid, row, col, -1)

        return total_score


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        grid = []
        for line in file:
            grid.append([int(num) for num in list(line.strip())])

        print(Solution().calculate_hiking(grid))
        print(Solution().calculate_hiking_pt2(grid))
