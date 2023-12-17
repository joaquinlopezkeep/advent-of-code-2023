
import re
from typing import List

numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8",  "nine": "9"}


def extract_numbers_from_string(value: str) -> List[str]:
    # Regex pattern for part one
    # pattern = r'([0-9])'
    # result: list[str] = re.findall(pattern, value)

    # Regex pattern for part two
    pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'
    result: List[str] = [match.group(1)
                         for match in re.finditer(pattern, value)]

    if not result:
        return []

    return result


with open('./day1-input.txt', 'r', encoding='utf-8') as input_file:
    total: int = 0
    while True:
        text: str = input_file.readline()
        if not text:
            break
        calibration_numbers = extract_numbers_from_string(text)
        first_number = numbers.get(
            calibration_numbers[0]) or calibration_numbers[0]
        last_number = numbers.get(
            calibration_numbers[-1]) or calibration_numbers[-1]
        total += int(first_number + last_number)

    print("total: ", total)
