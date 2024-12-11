from typing import List
from copy import deepcopy
from collections import defaultdict

class Solution:
    def count_visited(self, matrix: List[List[str]]) -> int:
        rotate_mapper = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0)
        }
        # Find starting position and direction
        cur_row = -1
        cur_col = -1
        direction = (-1, 0)
        for row, r in enumerate(matrix):
            for col, char in enumerate(r):
                if (char == "^"):
                    cur_row, cur_col = row, col
                    break

        visited_set = set()
        while cur_row >= 0 and cur_row < len(matrix) and cur_col >= 0 and cur_col < len(matrix[0]):
            visited_set.add((cur_row, cur_col))
            matrix[cur_row][cur_col] = "X"
            look_forward_row = cur_row + direction[0]
            look_forward_col = cur_col + direction[1]
            if (look_forward_row < 0 or look_forward_row >= len(matrix) or look_forward_col < 0 or look_forward_col >= len(matrix[0])):
                cur_row, cur_col = look_forward_row, look_forward_col
                continue
                
            if matrix[look_forward_row][look_forward_col] == "#":
                # rotate 90 degrees
                direction = rotate_mapper[direction]

            cur_row, cur_col = cur_row + direction[0], cur_col + direction[1]
        

        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in matrix]))
        return len(visited_set)

    def find_loops(self, matrix: List[List[str]]) -> int:
        possible_loops = 0
        rotate_mapper = {
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0)
        }
        # Find starting position and direction
        cur_row = -1
        cur_col = -1
        direction = (-1, 0)
        for row, r in enumerate(matrix):
            for col, char in enumerate(r):
                if (char == "^"):
                    cur_row, cur_col = row, col
                    break

        start_row = cur_row
        start_col = cur_col
        visited_set = set()
        while cur_row >= 0 and cur_row < len(matrix) and cur_col >= 0 and cur_col < len(matrix[0]):
            if ((cur_row, cur_col) != (start_row), start_col):
                visited_set.add((cur_row, cur_col))
            look_forward_row = cur_row + direction[0]
            look_forward_col = cur_col + direction[1]
            if (look_forward_row < 0 or look_forward_row >= len(matrix) or look_forward_col < 0 or look_forward_col >= len(matrix[0])):
                cur_row, cur_col = look_forward_row, look_forward_col
                continue
                
            if matrix[look_forward_row][look_forward_col] == "#":
                # rotate 90 degrees
                direction = rotate_mapper[direction]

            cur_row, cur_col = cur_row + direction[0], cur_col + direction[1]

        # Try placing walls at all spots in the original path
        for wall_pos in visited_set:
            grid_copy = deepcopy(matrix)
            grid_copy[wall_pos[0]][wall_pos[1]] = "#"
            visited_count = defaultdict(int)
            loop = False
            cur_row, cur_col = start_row, start_col
            direction = (-1, 0)
            while cur_row >= 0 and cur_row < len(grid_copy) and cur_col >= 0 and cur_col < len(grid_copy[0]):
                visited_count[(cur_row, cur_col)] += 1
                grid_copy[cur_row][cur_col] = "X"
                if visited_count[(cur_row, cur_col)] > 20:
                    # Loop
                    loop = True
                    break
                look_forward_row = cur_row + direction[0]
                look_forward_col = cur_col + direction[1]
                if (look_forward_row < 0 or look_forward_row >= len(grid_copy) or look_forward_col < 0 or look_forward_col >= len(grid_copy[0])):
                    cur_row, cur_col = look_forward_row, look_forward_col
                    continue
                    
                while grid_copy[look_forward_row][look_forward_col] == "#":
                    # rotate 90 degrees
                    direction = rotate_mapper[direction]
                    look_forward_row = cur_row + direction[0]
                    look_forward_col = cur_col + direction[1]

                cur_row, cur_col = cur_row + direction[0], cur_col + direction[1]
            if (loop):
                possible_loops += 1
        
        return possible_loops
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(list(line.strip()))

        copy1 = deepcopy(matrix)
        copy2 = deepcopy(matrix)

        print(Solution().count_visited(copy1))
        print(Solution().find_loops(copy2))
