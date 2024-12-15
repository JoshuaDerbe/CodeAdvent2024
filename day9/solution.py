class Solution:
    def defragment(self, diskmap: str) -> int:
        checksum = 0

        final_drive = []
        file_block = True
        file_id = 0
        free_space_indexes = []
        cur_index = 0
        for file in diskmap:
            if file_block:
                final_drive += int(file) * [str(file_id)]
                file_id += 1
            else:
                final_drive += int(file) * ["."]
                free_space_indexes += range(cur_index, cur_index + int(file))
            cur_index += int(file)
            file_block = not file_block
        for i, char in reversed(list(enumerate(final_drive))):
            if char != ".":
                spare_spot = free_space_indexes.pop(0)
                if spare_spot > i:
                    break
                final_drive[spare_spot] = char
                final_drive[i] = "."
        print("".join(final_drive))

        # Calc checksum
        for i, file in enumerate(final_drive):
            if file != ".":
             checksum += i * int(file)

        return checksum
    
    def defragment_whole_files(self, diskmap: str) -> int:
        checksum = 0

        final_drive = []
        file_block = True
        file_id = 0
        for file in diskmap:
            if file_block:
                final_drive += int(file) * [str(file_id)]
                file_id += 1
            else:
                final_drive += int(file) * ["."]
            file_block = not file_block
        print("".join(final_drive))

        lpl = 0
        lpr = 0
        rpl = len(final_drive) - 1
        rpr = len(final_drive) - 1
        while (rpl >= 0):
            if final_drive[rpr] == ".":
                rpl -= 1
                rpr -= 1
                continue
            if final_drive[rpl - 1] == final_drive[rpr]:
                rpl -= 1
                continue
            # rpl to rpr should now be the current whole file
            file_len = rpr - rpl
            file_id = final_drive[rpr]

            lpl = 0
            lpr = 0
            for i, space in enumerate(final_drive):
                if lpl > rpl:
                    break
                if space != ".":
                    lpr += 1
                    lpl = lpr
                    continue

                if lpr - lpl == file_len:
                    # Place file here
                    for j in range(lpl, lpr + 1):
                        final_drive[j] = file_id
                        final_drive[rpr] = "."
                        rpr -= 1
                    break
                lpr += 1
            rpl -= 1
            rpr = rpl
            
        print("".join(final_drive))
        # Calc checksum
        for i, file in enumerate(final_drive):
            if file != ".":
             checksum += i * int(file)

        return checksum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        diskmap = ""
        for line in file:
            diskmap += line.strip()

        print(diskmap)
        #print(Solution().defragment(diskmap))
        print(Solution().defragment_whole_files(diskmap))
