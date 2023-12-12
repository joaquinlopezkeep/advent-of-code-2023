
from typing import List


def extract_calibration_value(value: str) -> int:
    result: List[str] = []
    for char in value:
        if char.isdigit():
            result.append(char)
    if not result:
        return 0
    if len(result) == 1:
        return int(result[0] + result[0])
    return int(result[0] + result[-1])


with open('./day1-input.txt', 'r', encoding='utf-8') as input_file:
    total: int = 0
    while True:
        line: str = input_file.readline()
        if not line:
            break
        total += extract_calibration_value(line)

    print("total: ", total)
