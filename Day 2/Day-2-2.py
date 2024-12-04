from typing import List
#455
def parse_reports() -> List[List[int]]:
    with open("Day-2-input.txt", "r") as input_file:
        reports = []
        for line in input_file:
            level = [int(number) for number in line.split()]
            reports.append(level)
    #reports = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
    return reports
    
def is_report_safe(report: List[int]) -> bool:
    for index, level in enumerate(report):
        if index > 0:
            last_level = report[index - 1]
            difference = abs(last_level - level)

            if difference > 3 or difference < 1:
                return False
            
            if index > 1:
                increasing = last_level > report[index - 2]
                if (level > last_level and not increasing):
                    return False
                if (level < last_level and increasing):
                    return False
    return True

def main():
    reports = parse_reports()
    safe_reports = 0

    for report in reports:
        report_safe = False
        #Run through all options to find if removing 1 item will fix it
        for index, level in enumerate(report):
            report_copy = report.copy()
            report_copy.pop(index)
            if is_report_safe(report_copy):
                report_safe = True

        if report_safe:
            safe_reports += 1
            
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    main()