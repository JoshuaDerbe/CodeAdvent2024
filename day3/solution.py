import re
from typing import List

class Solution:
    def calculate_muls(self, input: List[str]) -> int:
        total = 0
        for line in input:
            matches = re.findall("mul\([0-9]*?\,[0-9]*?\)",line)
            for match in matches:
                num1 = re.search("mul\(([0-9]*)", match).group(1)
                num2 = re.search("([0-9]*)\)", match).group(1)
                total += int(num1) * int(num2)
        return total
    
    def calculate_muls_do_dont(self, input: List[str]) -> int:
        total = 0
        do = True
        for line in input:
            matches = re.findall("do\(\)|don't\(\)|mul\([0-9]*?\,[0-9]*?\)",line)
            for match in matches:
                if (match == "don't()"):
                    do = False
                    continue
                elif (match == "do()"):
                    do = True
                    continue
                elif (do):
                    num1 = re.search("mul\(([0-9]*)", match).group(1)
                    num2 = re.search("([0-9]*)\)", match).group(1)
                    total += int(num1) * int(num2)
        return total


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        lines = []
        for line in file:
            lines.append(line)
        print(Solution().calculate_muls(lines))
        print(Solution().calculate_muls_do_dont(lines))
