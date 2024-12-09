from typing import List

class Solution:
    def _is_mas_cross(self, input: List[List[str]], row: int, col: int):
        if (row - 1 < 0) or (col - 1 < 0) or (row + 1 >= len(input)) or (col + 1 >= len(input[0])):
            return False
        opposites = {
            "M": "S",
            "S": "M",
            "A": "",
            "X": ""
        }
        top_left = input[row - 1][col - 1]
        top_right = input[row - 1][col + 1]
        bottom_left = input[row + 1][col - 1]
        bottom_right = input[row + 1][col + 1]
        if (top_left == opposites[bottom_right]) and (top_right == opposites[bottom_left]):
            return True
        
        return False


    def find_mas(self, input: List[List[str]]) -> int:
        total_crosses = 0
        for y, row in enumerate(input):
            for x, char in enumerate(row):
                if (char == "A") and (self._is_mas_cross(input, y, x)):
                    total_crosses += 1

        return total_crosses
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(list(line.strip()))

        print(Solution().find_mas(matrix))
