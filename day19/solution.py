from typing import List
import re
from functools import cache

class Solution:
    def find_possible_towels(self, patterns: List[str], designs: List[str]):
        possible_designs = []
        for design in designs:
            n = len(design)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for pattern in patterns:
                    if i >= len(pattern) and design[i - len(pattern):i] == pattern and dp[i - len(pattern)]:
                        dp[i] = True
                        break
            if dp[n]:
                possible_designs.append(design)

        return len(possible_designs)
    
    def all_possiblities(self, patterns: List[str], designs: List[str]):
        total = 0
        for design in designs:
            total += count(design)

        return total

PATTERNS = []
@cache
def count(d):
    return d == '' or sum(count(d.removeprefix(p))
        for p in PATTERNS if d.startswith(p))

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        patterns = []
        designs = []
        on_designs = False
        for line in file:
            if line == "\n":
                on_designs = True
                continue
            if not on_designs:
                patterns = line.strip().split(", ")
            else:
                designs.append(line.strip())
        
        print(patterns)
        PATTERNS = patterns
        print(designs)
        print(Solution().find_possible_towels(patterns, designs))
        print(Solution().all_possiblities(patterns, designs))