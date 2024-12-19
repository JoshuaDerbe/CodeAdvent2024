import re
from typing import List, Tuple

class Solution:
    def _cheapest(self, a_movement, b_movement, desired, a_push_count, b_push_count, cache):
        if desired in cache:
            return cache[desired]
        if (a_movement[0], a_movement[1]) == desired:
            return 3
        if (b_movement[0], b_movement[1]) == desired:
            return 1
        if desired[0] < 0 or desired[1] < 0 or a_push_count >= 100 or b_push_count >= 100:
            # Unsolvable
            return None
        
        a_pushed = self._cheapest(a_movement, b_movement, (desired[0] - a_movement[0], desired[1] - a_movement[1]), a_push_count + 1, b_push_count, cache)
        b_pushed = self._cheapest(a_movement, b_movement, (desired[0] - b_movement[0], desired[1] - b_movement[1]), a_push_count, b_push_count + 1, cache)
        if a_pushed is None and b_pushed is None:
            answer = None
        elif a_pushed is None:
            answer = b_pushed + 1
        elif b_pushed is None:
            answer = a_pushed + 3
        else:
            answer = min(a_pushed + 3, b_pushed + 1)
        cache[desired] = answer
        return answer


    def calc_cheapest_win(self, a_buttons: List[Tuple[int, int]], b_buttons: List[Tuple[int, int]], desired: List[Tuple[int, int]]) -> int:
        total_tokens = 0
        for i in range(len(a_buttons)):
            a_movement = a_buttons[i]
            b_movement = b_buttons[i]
            required = desired[i]
            cache = {}
            cheapest = self._cheapest(a_movement, b_movement, required, 0, 0, cache) 
            if cheapest is not None:
                total_tokens += cheapest

        return total_tokens
    
class SolutionPart2:
    def _cheapest(self, a_movement, b_movement, desired):
        # A*a_x + B*b_x = d_x
        # A*a_x = d_x - B*b_x
        # A = (d_x - B*b_x)/a_x
        #
        # A*a_y + B*b_y = d_y
        # B*b_y = d_y - A*a_y
        # B = (d_y - A*a_y)/b_y

        a_x = a_movement[0]
        a_y = a_movement[1]
        b_x = b_movement[0]
        b_y = b_movement[1]
        d_x = desired[0]
        d_y = desired[1]

        a_pushes = (d_x*b_y - d_y*b_x) / (a_x*b_y - a_y*b_x)
        b_pushes = (a_x*d_y - a_y*d_x) / (a_x*b_y - a_y*b_x)
        if not a_pushes.is_integer() or not b_pushes.is_integer():
            return None
        
        return a_pushes * 3 + b_pushes



    def calc_cheapest_win(self, a_buttons: List[Tuple[int, int]], b_buttons: List[Tuple[int, int]], desired: List[Tuple[int, int]]) -> int:
        total_tokens = 0
        for i in range(len(a_buttons)):
            a_movement = a_buttons[i]
            b_movement = b_buttons[i]
            required = (desired[i][0] + 10000000000000, desired[i][1] + 10000000000000)
            cheapest = self._cheapest(a_movement, b_movement, required) 
            if cheapest is not None:
                total_tokens += int(cheapest)

        return total_tokens
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        a_buttons = []
        b_buttons = []
        desired = []
        for line in file:
            if line.startswith("Button A"):
                m = re.findall("X\+([0-9]+), Y\+([0-9]+)", line)
                a_buttons.append((int(m[0][0]), int(m[0][1])))
            if line.startswith("Button B"):
                m = re.findall("X\+([0-9]+), Y\+([0-9]+)", line)
                b_buttons.append((int(m[0][0]), int(m[0][1])))
            if line.startswith("Prize"):
                m = re.findall("X=([0-9]+), Y=([0-9]+)", line)
                desired.append((int(m[0][0]), int(m[0][1])))

        #print(Solution().calc_cheapest_win(a_buttons, b_buttons, desired))
        print(SolutionPart2().calc_cheapest_win(a_buttons, b_buttons, desired))


