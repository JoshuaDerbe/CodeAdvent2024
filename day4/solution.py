from typing import List

class Solution:
    def _dfs_search(self, input: List[List[str]], x: int, y: int, x_offset: int, y_offset: int, desired_char: str) -> bool:
        next_char_wanted = {
            "X": "M",
            "M": "A",
            "A": "S",
            "S": ""
        }
        if desired_char == "":
            return True
        if (x < 0) or (x >= len(input[0])) or (y < 0) or (y >= len(input)):
            return False
        if input[y][x] == desired_char:
            return self._dfs_search(input, x + x_offset, y + y_offset, x_offset, y_offset, next_char_wanted[desired_char])
        else:
            return False


    def find_xmas(self, input: List[List[str]]) -> int:
        total_words = 0
        for y, row in enumerate(input):
            for x, char in enumerate(row):
                if (char == "X"):
                    row_directions = [-1, 0, 1, 1, 1, 0, -1, -1]
                    col_directions = [-1 ,-1, -1, 0, 1, 1, 1, 0]
                    # Traverse in 8 directions
                    for i in range(8):
                        new_row = y + row_directions[i]
                        new_col = x + col_directions[i]
                        if (self._dfs_search(input, new_col, new_row, col_directions[i], row_directions[i], "M")):
                            input[y][x] = "."
                            total_words += 1

        return total_words
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append(list(line.strip()))

        print(Solution().find_xmas(matrix))
