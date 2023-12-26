from collections import Counter

def histogram(text):
    char_count = Counter(text)
    sorted_chars = sorted(char_count.keys())
    max_count = max(char_count.values())

    first_non_empty_line = next(
        (i for i in range(max_count, 0, -1) 
            if any(char_count[char] >= i for char in sorted_chars 
                if char not in (' ', '\n'))), 0)

    result = []

    for i in range(first_non_empty_line, 0, -1):
        row = ''
        for char in sorted_chars:
            if char not in (' ', '\n'):
                row += '#' if char_count[char] >= i else ' '
        result.append(row)

    characters = ''.join(char for char in sorted_chars if char not in (' ', '\n'))

    return result, characters

if __name__ == "__main__":
    try:
        with open("input3.txt", "r") as file:
            encrypted_text = file.read()
    except FileNotFoundError:
        print("Файл input.txt не найден.")
        exit()

    result, characters = histogram(encrypted_text)

    for row in result:
        print(row)

    print(characters)
