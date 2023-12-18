def look_around(top_row: str | None, bottom_row: str | None, current_row: str, index) -> int:
    # TODO
    count = 0
    return count


with open('./day3-input.txt', 'r', encoding="utf-8") as input_file:
    text: str = input_file.read()
    split_text: list[str] = text.splitlines()
    count = 0
    n = len(split_text)
    is_special_char = lambda \
            char: not (char.isalpha() or char.isnumeric() or char == "." or char.isspace())
    for i, line in enumerate(split_text):
        for j, char in enumerate(line):
            if is_special_char(char):
                print(char)
                if i == 0:
                    count += look_around(None, split_text[i + 1], split_text[i], j)
                elif i == n - 1:
                    count += look_around(split_text[i - 1], None, split_text[i], j)
                else:
                    count += look_around(split_text[i - 1], split_text[i + 1], split_text[i], j)
    print("total: ", count)
