from typing import List
import itertools

class Solution:
    def find_solutions(self, equal_list: List[int], equations: List[int]) -> int:
        correct_sum = 0

        for i, numbers in enumerate(equations):
            solution_possible = False
            desired_res = equal_list[i]
            binary_list = [list(n) for n in itertools.product([0, 1], repeat=len(numbers) - 1)]
            for combination in binary_list:
                sum = numbers[0]
                for j, op in enumerate(combination):
                    if op == 0:
                        sum += numbers[j + 1]
                    else:
                        sum *= numbers[j + 1]
                    if sum == desired_res:
                        solution_possible = True
                        break

                if solution_possible:
                    correct_sum += desired_res
                    break


        return correct_sum
    
    def find_solutions_with_concat(self, equal_list: List[int], equations: List[int]) -> int:
        correct_sum = 0

        for i, numbers in enumerate(equations):
            solution_possible = False
            desired_res = equal_list[i]
            trinary_list = [list(n) for n in itertools.product([0, 1, 2], repeat=len(numbers) - 1)]
            for combination in trinary_list:
                cur_sum = numbers[0]
                for j, op in enumerate(combination):
                    if op == 0:
                        cur_sum += numbers[j + 1]
                    elif op == 1:
                        cur_sum *= numbers[j + 1]
                    elif op == 2:
                        cur_sum = int(str(cur_sum) + str(numbers[j + 1]))
                if cur_sum == desired_res:
                    solution_possible = True
                    break

            if solution_possible:
                correct_sum += desired_res

        return correct_sum 
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        equations = []
        equal_list = []
        for line in file:
            temp = line.strip().split(":")
            equal_list.append(int(temp[0]))
            equations.append([int(num) for num in temp[1].strip().split(" ")])

        print(Solution().find_solutions(equal_list, equations))
        print(Solution().find_solutions_with_concat(equal_list, equations))
