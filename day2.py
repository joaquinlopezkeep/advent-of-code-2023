import re

from day1 import extract_numbers_from_string

max_values = {"red": 12, "green": 13, "blue": 14}


def divide_string(value: str) -> list[str]:
    result: list[str] = []

    split = value.split(":")

    key: str = split[0]

    values: list[str] = split[1].split(";")

    result.append(key)

    for i, val in enumerate(values):
        result.extend(val.split(","))

    return result


def join_string_of_numbers_array(arr: list[str]) -> int:
    num = ""
    for j, val in enumerate(arr):
        if val.isdigit():
            num += val
    return int(num)


def extract_color_from_string(value: str) -> str | None:
    pattern = r'(red|green|blue)'

    result: list[str] = re.findall(pattern, value)

    if not result:
        return None

    return result[0]


with open('./day2-input.txt', "r", encoding="utf-8") as input_file:
    count = 0

    while True:
        text: str = input_file.readline()

        if not text:
            break

        game: list[str] = divide_string(text)

        game_id: int = join_string_of_numbers_array(extract_numbers_from_string(game[0]))

        valid_game = True

        for i, val in enumerate(game):
            if i == 0:
                continue

            current_val = join_string_of_numbers_array(extract_numbers_from_string(val))

            if current_val > 14:
                valid_game = False
                break

            key = extract_color_from_string(val)

            if key is None:
                continue
            max_v = max_values.get(key)

            if current_val > max_v:
                valid_game = False
                break

        if valid_game:
            count += game_id

    print("total: ", count)
