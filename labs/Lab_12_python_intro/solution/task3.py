import string

def histogram(text):

    counts = {}
    for char in text:
        if char not in string.whitespace:
            current_count = counts.get(char, 0)
            updated_count = current_count + 1
            counts[char] = updated_count

    symbols = list(counts.keys())
    symbols.sort()
    max_count = max(counts.values())

    for i in range(max_count, 0, -1):
        for char in symbols:
            if counts[char] >= i:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()

    for char in symbols:
        print(char, end=' ')
    print()

if __name__ == '__main__':  # точка запуска решения
    txt = input() # ввод текста
    histogram(txt)  # вызов функции для нахождения символов, использованных чаще всего
