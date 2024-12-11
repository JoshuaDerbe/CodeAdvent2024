from collections import defaultdict
from typing import List, Dict, Set

class Solution:
    def find_correct_printings(self, print_orders: List[List[int]], required_before_map: Dict[int, Set[int]]) -> int:
        correct_printings = 0
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
            
            if (valid):
                correct_printings += 1
                middle_sum += print_run[len(print_run)//2]


        print(correct_printings)
        return middle_sum
    
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
                updated_list = [print_run[0]]
                for page in print_run[1:]:
                    insert_index = 0
                    inserted = False
                    for i, final_num in enumerate(updated_list):
                        if (final_num in required_before_map[page]):
                            # Required before this num, insert it before this num
                            insert_index = i
                            inserted = True
                            break
                    if inserted:
                        updated_list.insert(insert_index, page)
                    else:
                        updated_list.append(page)
                middle_sum += updated_list[len(updated_list)//2]

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

        print(Solution().find_correct_printings(print_orders, required_before_map))
        print(Solution().reorder_incorrect_printings(print_orders, required_before_map))
        