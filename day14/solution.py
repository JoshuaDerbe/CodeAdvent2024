import re
import math
from typing import List, Tuple, Dict

class Solution:
    def calc_robot_movement(self, robot_dict: Dict[int, Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
        NUM_ROWS = 103
        middle_row = NUM_ROWS // 2
        NUM_COLS = 101
        middle_col = NUM_COLS // 2
        grid = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
        
        for _ in range(100):
            for robot_id, robot in robot_dict.items():
                new_pos = ((robot[0][0] + robot[1][0]) % NUM_ROWS, (robot[0][1] + robot[1][1]) % NUM_COLS)
                robot_dict[robot_id] = (new_pos, robot[1])

        # Count robots in quadrants
        up_left_quad_count = 0
        up_right_quad_count = 0
        down_left_quad_rount = 0
        down_right_quad_count = 0
        for robot_id, robot in robot_dict.items():
            if robot[0][0] == middle_row or robot[0][1] == middle_col:
                continue
            elif robot[0][0] < middle_row:
                # Up half
                if robot[0][1] < middle_col:
                    up_left_quad_count += 1
                else:
                    up_right_quad_count +=1
            else:
                # Down half
                if robot[0][1] < middle_col:
                    down_left_quad_rount += 1
                else:
                    down_right_quad_count +=1
            grid[robot[0][0]][robot[0][1]] += 1

        print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
      for row in grid]))

        return up_left_quad_count * up_right_quad_count * down_left_quad_rount * down_right_quad_count
    
class SolutionPart2:
    def _check_for_tree(self, grid):
        for row in grid:
            for val in row:
                if val > 1:
                    return False
        return True

    def calc_robot_movement(self, robot_dict: Dict[int, Tuple[Tuple[int, int], Tuple[int, int]]]) -> int:
        NUM_ROWS = 103
        NUM_COLS = 101
        
        for second in range(100000):
            for robot_id, robot in robot_dict.items():
                new_pos = ((robot[0][0] + robot[1][0]) % NUM_ROWS, (robot[0][1] + robot[1][1]) % NUM_COLS)
                robot_dict[robot_id] = (new_pos, robot[1])
            
            grid = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
            for robot_id, robot in robot_dict.items():
                grid[robot[0][0]][robot[0][1]] += 1
            if self._check_for_tree(grid):
                return second + 1

        return 0
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        robot_dict = {}
        robot_num = 1
        for line in file:
            m = re.findall("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
            robot_dict[robot_num] = ((int(m[0][1]), int(m[0][0])), (int(m[0][3]), int(m[0][2])))
            robot_num += 1
        
        #print(Solution().calc_robot_movement(robot_dict))
        print(SolutionPart2().calc_robot_movement(robot_dict))

