
import re
from typing import List

numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8",  "nine": "9"}


def extract_calibration_value(value: str) -> int:
    pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'
    result: List[str] = [match.group(1)
                         for match in re.finditer(pattern, value)]
    if not result:
        return 0

    first = numbers.get(result[0])
    last = numbers.get(result[-1])
    first_number = first if first is not None else result[0]
    last_number = last if last is not None else result[-1]
    return int(first_number + last_number)


with open('./day1-input.txt', 'r', encoding='utf-8') as input_file:
    total: int = 0
    while True:
        line: str = input_file.readline()
        if not line:
            break
        total += extract_calibration_value(line)

    print("total: ", total)
