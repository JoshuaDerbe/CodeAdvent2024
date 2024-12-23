import re
from typing import List

class Solution:
    def _combo_operand(self, A, B, C, operand):
        if operand == 4:
            return A
        if operand == 5:
            return B
        if operand == 6:
            return C
        return operand

    def calc_output(self, A: int, B: int, C: int, program: List[int]) -> int:
        output = []
        i = 0
        while i < len(program):
            code = program[i]
            combo = self._combo_operand(A, B, C, program[i+1])
            jumped = False
            if code == 0:
                res = A // (2**(combo))
                A = res
            if code == 1:
                res = B ^ program[i + 1]
                B = res
            if code == 2:
                res = combo % 8
                B = res
            if code == 3 and A != 0:
                i = program[i + 1]
                jumped = True
            if code == 4:
                res = B ^ C
                B = res
            if code == 5:
                res = combo % 8
                output.append(str(res))
            if code == 6:
                res = A // (2**(combo))
                B = res
            if code == 7:
                res = A // (2**(combo))
                C = res

            #print(i, "-", A, B, C, output)
            if not jumped:
                i += 2


        return ",".join(output)
    

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        A = 0
        B = 0
        C = 0
        program = []
        for line in file:
            if line.startswith("Register A"):
                m = re.findall("^Register A: (\d+)$", line.strip())
                A = int(m[0])
            elif line.startswith("Register B"):
                m = re.findall("^Register B: (\d+)$", line.strip())
                B = int(m[0])
            elif line.startswith("Register C"):
                m = re.findall("^Register C: (\d+)$", line.strip())
                C = int(m[0])
            elif line.startswith("Program"):
                m = re.findall("^Program: (.*)", line.strip())
                program = [int(num) for num in m[0].split(",")]
        print(Solution().calc_output(A, B, C, program))


