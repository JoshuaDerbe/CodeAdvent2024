from typing import List

class Solution:
    def _safe_report(self, report: List[int]) -> bool:
        safe = True
        prev_level = report[0]
        increasing = report[0] < report[-1]
        for level in report[1:]:
            diff = level - prev_level
            if diff == 0 or abs(diff) > 3:
                safe = False
            elif diff < 0 and increasing:
                safe = False
            elif diff > 0 and not increasing:
                safe = False
            prev_level = level

            if safe == False:
                break

        return safe

    def safe_report_count(self, reports: List[List[int]]) -> int:
        safe_count = 0
        for report in reports:
            safe = self._safe_report(report)

            if safe:
                safe_count += 1

        return safe_count
    
    def safe_report_count_removing_bad(self, reports: List[List[int]]) -> int:
        first_pass_safe_count = 0
        unsafe_reports = []
        for report in reports:
            safe = self._safe_report(report)

            if safe:
                first_pass_safe_count += 1
            else:
                unsafe_reports.append(report)

        second_pass_safe_count = 0
        for report in unsafe_reports:
            safe = False
            for index_to_remove in range(len(report)):
                edited_report = report.copy()
                edited_report.pop(index_to_remove)
                safe = self._safe_report(edited_report)
                if safe:
                    break
            if safe:
                second_pass_safe_count += 1

        return first_pass_safe_count + second_pass_safe_count
    
if __name__ == "__main__":
    with open("input.txt", "r") as file:
        reports = []
        for line in file:
            reports.append([int(num) for num in line.strip().split(" ")])
        print(Solution().safe_report_count(reports))
        print(Solution().safe_report_count_removing_bad(reports))
