from typing import List
import time

class Solution:
    def _push_box(self, grid, row, col, direction):
        direction_mapper = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        look_ahead_row, look_ahead_col = row + direction_mapper[direction][0], col + direction_mapper[direction][1]
        obstacle = grid[look_ahead_row][look_ahead_col]
        if obstacle == ".":
            grid[look_ahead_row][look_ahead_col] = "O"
            grid[row][col] = "."
        elif obstacle == "O":
            self._push_box(grid, look_ahead_row, look_ahead_col, direction)
            if grid[look_ahead_row][look_ahead_col] == ".":
                grid[look_ahead_row][look_ahead_col] = "O"
                grid[row][col] = "."


    def move_robot(self, grid: List[List[str]], movements: List[str]) -> int:
        total_box_coords = 0
        direction_mapper = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        # Find starting pos
        cur_row = -1
        cur_col = -1
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "@":
                    cur_row, cur_col = row, col
                    break
            if cur_row != -1:
                break

        for movement in movements: 
            look_ahead_row, look_ahead_col = cur_row + direction_mapper[movement][0], cur_col + direction_mapper[movement][1]
            obstacle = grid[look_ahead_row][look_ahead_col]
            if obstacle == ".":
                grid[look_ahead_row][look_ahead_col] = "@"
                grid[cur_row][cur_col] = "."
                cur_row, cur_col = look_ahead_row, look_ahead_col
            elif obstacle == "O":
                self._push_box(grid, look_ahead_row, look_ahead_col, movement)
                if grid[look_ahead_row][look_ahead_col] == ".":
                    grid[look_ahead_row][look_ahead_col] = "@"
                    grid[cur_row][cur_col] = "."
                    cur_row, cur_col = look_ahead_row, look_ahead_col  
            

        #     print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        # for row in grid]))
        #     time.sleep(0.3)

        # Calculate final result
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "O":
                    total_box_coords += 100 * row + col

        return total_box_coords
    
class SolutionPart2:
    def _push_box(self, grid, row, col, direction):
        direction_mapper = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        cur_val = grid[row][col]
        if direction == "<" or direction == ">":
            look_ahead_row, look_ahead_col = row + direction_mapper[direction][0], col + direction_mapper[direction][1]
            obstacle = grid[look_ahead_row][look_ahead_col]
            if obstacle == ".":
                grid[look_ahead_row][look_ahead_col] = cur_val
                grid[row][col] = "."
            elif obstacle == "[" or obstacle == "]":
                self._push_box(grid, look_ahead_row, look_ahead_col, direction)
                if grid[look_ahead_row][look_ahead_col] == ".":
                    grid[look_ahead_row][look_ahead_col] = cur_val
                    grid[row][col] = "."
        else:
            if cur_val == "[" or cur_val == "]":
                if cur_val == "[":
                    l_col, r_col = col, col + 1
                else:
                    l_col, r_col = col - 1, col
                look_ahead_row, look_ahead_l_col, look_ahead_r_col = row + direction_mapper[direction][0], l_col + direction_mapper[direction][1], r_col + direction_mapper[direction][1]
                if self._can_push_box(grid, look_ahead_row, look_ahead_l_col, direction) and self._can_push_box(grid, look_ahead_row, look_ahead_r_col, direction):
                    self._push_box(grid, look_ahead_row, look_ahead_l_col, direction)
                    self._push_box(grid, look_ahead_row, look_ahead_r_col, direction)
                    grid[look_ahead_row][look_ahead_l_col] = "["
                    grid[look_ahead_row][look_ahead_r_col] = "]"
                    grid[row][l_col] = "."
                    grid[row][r_col] = "."

    def _can_push_box(self, grid, row, col, direction):
        direction_mapper = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        cur_val = grid[row][col]
        if cur_val == ".":
            return True
        if direction == "^" or direction == "v":
            if cur_val == "[" or cur_val == "]":
                if cur_val == "[":
                    l_col, r_col = col, col + 1
                else:
                    l_col, r_col = col - 1, col
                look_ahead_row, look_ahead_l_col, look_ahead_r_col = row + direction_mapper[direction][0], l_col + direction_mapper[direction][1], r_col + direction_mapper[direction][1]
                if self._can_push_box(grid, look_ahead_row, look_ahead_l_col, direction) and self._can_push_box(grid, look_ahead_row, look_ahead_r_col, direction):
                    return True

        return False




    def move_robot(self, grid: List[List[str]], movements: List[str]) -> int:
        total_box_coords = 0
        direction_mapper = {
            "^": (-1, 0),
            ">": (0, 1),
            "v": (1, 0),
            "<": (0, -1)
        }
        # Find starting pos
        cur_row = -1
        cur_col = -1
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "@":
                    cur_row, cur_col = row, col
                    break
            if cur_row != -1:
                break

        for movement in movements: 
            look_ahead_row, look_ahead_col = cur_row + direction_mapper[movement][0], cur_col + direction_mapper[movement][1]
            obstacle = grid[look_ahead_row][look_ahead_col]
            if obstacle == ".":
                grid[look_ahead_row][look_ahead_col] = "@"
                grid[cur_row][cur_col] = "."
                cur_row, cur_col = look_ahead_row, look_ahead_col
            elif obstacle == "[" or obstacle == "]":
                self._push_box(grid, look_ahead_row, look_ahead_col, movement)
                if grid[look_ahead_row][look_ahead_col] == ".":
                    grid[look_ahead_row][look_ahead_col] = "@"
                    grid[cur_row][cur_col] = "."
                    cur_row, cur_col = look_ahead_row, look_ahead_col  
            

        #     print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        # for row in grid]))
        #     time.sleep(0.3)

        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        for row in grid]))

        # Calculate final result
        for row, line in enumerate(grid):
            for col, char in enumerate(line):
                if char == "[":
                    total_box_coords += 100 * row + col

        return total_box_coords
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        on_movements = False
        movements = []
        grid = []
        for line in file:
            if line == "\n":
                on_movements = True
                continue
            if on_movements:
                movements += list(line.strip()) 
            else:
                grid.append(list(line.strip()))
        
        gridPart2 = [[] for _ in range(len(grid))]
        print(gridPart2)
        for row, line in enumerate(grid):
            for char in line:
                if char == "#":
                    gridPart2[row].append("#")
                    gridPart2[row].append("#")
                elif char == "O":
                    gridPart2[row].append("[")
                    gridPart2[row].append("]")
                elif char == ".":
                    gridPart2[row].append(".")
                    gridPart2[row].append(".")
                elif char == "@":
                    gridPart2[row].append("@")
                    gridPart2[row].append(".")

        

        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in grid]))
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in gridPart2]))
        print(movements)
        #print(Solution().move_robot(grid, movements))
        print(SolutionPart2().move_robot(gridPart2, movements))