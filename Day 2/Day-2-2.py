from typing import List, Optional, Union

def parse_reports() -> List[List[int]]:
    with open("Day-2-input.txt", "r") as input_file:
        reports = []
        for line in input_file:
            level = [int(number) for number in line.split()]
            reports.append(level)
    reports = [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]
    return reports

def is_report_safe(report: List[int]) -> Union[bool, Optional[int]]:
    for index, level in enumerate(report):
        if index > 0:
            last_level = report[index - 1]
            difference = abs(last_level - level)

            if difference > 3 or difference == 0:
                if not len(report) >= index + 2:
                    return False, index
                
                if is_report_safe([last_level, report[index + 1]])[0]:
                    return False, index
                elif is_report_safe([level, report[index + 1]])[0]:
                    return False, index - 1
                
                return False, index
            
            if index > 1:
                increasing = report[index - 2] < last_level
                if (level > last_level and not increasing) or (level < last_level and increasing):
                    if not len(report) >= index + 2:
                        return False, index
                    
                    if is_report_safe([last_level, report[index + 1]])[0]:
                        return False, index
                    elif is_report_safe([level, report[index + 1]])[0]:
                        return False, index - 1
                    
                    return False, index
    return True, None

def main():
    reports = parse_reports()
    safe_reports = 0

    for report in reports:
        safety_result = is_report_safe(report)
        if safety_result[0]:
            safe_reports += 1
        
        else:
            if safety_result[1]:
                report.pop(safety_result[1])

            #rerun without issue found in previous run
            if is_report_safe(report)[0]:
                safe_reports += 1
            
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    main()