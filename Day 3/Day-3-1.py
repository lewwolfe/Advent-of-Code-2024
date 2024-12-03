import re
from typing import List, Optional, Union

def parse_memory() -> List[List[int]]:
    with open("Day-3-input.txt", "r") as input_file:
        return input_file.read()

def use_regex(input_text):
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
    return pattern.findall(input_text)

def process_command(command: str) -> int:
    command = command.strip("mul(")
    command = command.strip(")")
    numbers = command.split(",")
    return int(numbers[0]) * int(numbers[1])

def main():
    final_result = 0
    memory = parse_memory()
    #memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    commands = use_regex(memory)
    for command in commands:
        final_result += process_command(command)
    print(f"Sum of results: {final_result}")

if __name__ == "__main__":
    main()