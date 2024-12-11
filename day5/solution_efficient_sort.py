from collections import defaultdict
from typing import List, Dict, Set
from functools import cmp_to_key

class Solution:
    def reorder_incorrect_printings(self, print_orders: List[List[int]], required_before_map: Dict[int, Set[int]]) -> int:
        incorrect_printings = 0
        middle_sum = 0

        for print_run in print_orders:
            already_printed = set()
            valid = True
            for page in print_run:
                required_before = required_before_map[page]
                if already_printed.intersection(required_before):
                    valid = False
                    break
                already_printed.add(page)
            
            if (not valid):
                incorrect_printings += 1
                # Reorder
                sorted_list = sorted(print_run, key=cmp_to_key(lambda item1, item2: -1 if item2 in required_before_map[item1] else 1))
                middle_sum += sorted_list[len(sorted_list)//2]

        print(incorrect_printings)
        return middle_sum
    

if __name__ == "__main__":
    required_before_map = defaultdict(set)
    with open("ordering_input.txt", "r") as file:
        for line in file:
            before, after = line.strip().split("|")
            before, after = int(before), int(after)
            required_before_map[before].add(after)
            

    with open("printing_input.txt", "r") as file:
        print_orders = []
        for line in file:
            print_order = [int(page) for page in line.strip().split(",")]
            print_orders.append(print_order)

        print(Solution().reorder_incorrect_printings(print_orders, required_before_map))
        