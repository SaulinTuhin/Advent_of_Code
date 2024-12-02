import os

class Solution:
    def countSafeReports(self, reports: list[int]) -> int:
        safe_reports = 0
        for report in reports:
            is_safe = True
            min, max = 1, 3
            if report[1] - report[0] < 0:
                min, max = -3, -1
            for i in range(1, len(report)):    
                if not min <= report[i] - report[i - 1] <= max:
                    is_safe = False
                    break
            safe_reports += 1 if is_safe else 0
        return safe_reports
    
    def countSafeReports_wProblemDampener(self, reports: list[int]) -> int:
        safe_reports = 0
        for report in reports:
            fault_count = 0
            min, max = 1, 3
            if report[1] - report[0] < 0:
                min, max = -3, -1
            for i in range(1, len(report)):    
                if not min <= report[i] - report[i - 1] <= max:
                    fault_count += 1
            safe_reports += 1 if fault_count <= 1 else 0
        return safe_reports


if __name__=="__main__":
    sol = Solution()

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    reports = []
    with open(cur_dir + '/input.txt', 'r') as f:
        for report in f.readlines():
            reports.append([int(data) for data in report.split()]) if len(report) else None

    print('Safe reports - ' + str(sol.countSafeReports(reports)))
    print('safe reports with problem dampener - ' + str(sol.countSafeReports_wProblemDampener(reports)))