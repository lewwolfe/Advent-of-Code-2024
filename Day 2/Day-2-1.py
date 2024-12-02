from typing import List

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
            difference = last_level - level 

            positive_difference = difference * -1 if difference < 0 else difference
            if positive_difference > 3 or positive_difference == 0:
                return False
 
            if index > 1:
                increasing = True if (report[index - 2] - last_level) < 0 else False 
                if level > last_level and not increasing:
                    return False
                    
                if level < last_level and increasing:
                    return False
    return True

def main():
    reports = parse_reports()
    safe_reports = 0

    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
            
    print(f"Number of safe reports: {safe_reports}")

if __name__ == "__main__":
    main()