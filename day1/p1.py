from csv import DictReader
from typing import List
from collections import defaultdict

class Solution:
    def total_distance(self, list1: List[int], list2: List[int]) -> int:
        sorted1 = sorted(list1)
        sorted2 = sorted(list2)
        
        total = 0
        for index in range(len(list1)):
            total += abs(sorted2[index] - sorted1[index])

        return total
    
    def similarity_score(self, list1: List[int], list2: List[int]) -> int:
        list2_count = defaultdict(int)
        for num in list2:
            list2_count[num] += 1

        score = 0
        for num in list1:
            score += num * list2_count[num]

        return score

    
if __name__ == "__main__":
    with open("input.csv") as file:
        reader = DictReader(file)
        list1 = []
        list2 = []
        for row in reader:
            list1.append(int(row["one"]))
            list2.append(int(row["two"]))
        print(Solution().total_distance(list1, list2))
        print(Solution().similarity_score(list1, list2))
