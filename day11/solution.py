from typing import List

class Solution:
    def compute_stones(self, stones_original: List[int], blink_count: int) -> int:
        stones = stones_original[:]

        for _ in range(blink_count):
            new_stones = []
            for stone in stones:
                str_stone = str(stone)
                if stone == 0:
                    new_stones.append(1)
                elif len(str_stone) % 2 == 0:
                    # Even digits
                    new_stones.append(int(str_stone[:len(str_stone)//2]))
                    new_stones.append(int(str_stone[len(str_stone)//2:]))
                else:
                    new_stones.append(stone * 2024)

            stones = new_stones

        return len(stones)
    
    def compute_stones_part2(self, stones_original: List[int], blink_count: int) -> int:
        cache = {}
        def stones_from(stone: int, blinks: int):
            if blinks == 0:
                return 1
            if (stone, blinks) in cache:
                return cache[(stone, blinks)]
            str_stone = str(stone)
            if stone == 0:
                res = stones_from(1, blinks - 1)
            elif len(str_stone) % 2 == 0:   
                # Even digits
                res = stones_from(int(str_stone[:len(str_stone)//2]), blinks - 1) + stones_from(int(str_stone[len(str_stone)//2:]), blinks - 1)
            else:
                res = stones_from(stone * 2024, blinks - 1)
            cache[(stone, blinks)] = res
            return res

        return sum(stones_from(stone, blink_count) for stone in stones_original)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        stones = []
        for line in file:
            stones = [int(num) for num in line.strip().split(" ")]

        print(stones)
        print(Solution().compute_stones_part2(stones, 25))
        print(Solution().compute_stones_part2(stones, 75))
