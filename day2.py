import re
from collections import deque

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


def is_game_valid(game: deque[str]) -> bool:
    valid_game = True
    for i, val in enumerate(game):

        current_val = join_string_of_numbers_array(extract_numbers_from_string(val))

        key = extract_color_from_string(val)

        if key is None:
            continue

        max_v = max_values.get(key)

        if current_val > max_v:
            valid_game = False
            break

    return valid_game


def fewest_number_of_cubes_of_each_color(game: deque[str]) -> dict[str, int]:
    fewest_cube_set = {"red": 0, "green": 0, "blue": 0}

    for i, val in enumerate(game):
        key = extract_color_from_string(val)

        current_val = int(join_string_of_numbers_array(extract_numbers_from_string(val)))

        fewest_cube_set[key] = max(fewest_cube_set[key], current_val)

    return fewest_cube_set


def power_of_set(set_of_cubes: dict[str, int]) -> int:
    result = 1
    for key, val in set_of_cubes.items():
        result *= int(val)
    return result


with open('./day2-input.txt', "r", encoding="utf-8") as input_file:
    count = 0
    valid_games = 0
    while True:
        text: str = input_file.readline()

        if not text:
            break

        game = deque(divide_string(text))

        game_id = join_string_of_numbers_array(extract_numbers_from_string(game.popleft()))

        fewest_set = fewest_number_of_cubes_of_each_color(game)

        # Solution for part one
        valid_game = is_game_valid(game)

        if valid_game:
            valid_games += game_id

        count += power_of_set(fewest_set)

    print("total valid games: ", valid_games)
    print("total: ", count)
