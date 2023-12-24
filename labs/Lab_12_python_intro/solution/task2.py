import math

from typing import List

def calc_median_sum(numbers: List[int]):

    numbers_sorted = []
    medians = []
    for number in numbers:
        left, right = 0, len(numbers_sorted) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers_sorted[mid] == number:
                pass
            elif numbers_sorted[mid] < number:
                left = mid + 1
            else:
                right = mid - 1
        numbers_sorted.insert(left, number)
        medians.append(numbers_sorted[math.ceil(len(numbers_sorted)/2) - 1])
    return sum(medians)

if __name__ == '__main__': # точка запуска решения
    n = int(input())   # ввод длины последовательности
    sequence = list(map(int, input().split()))  # ввод последовательности чисел

    if(len(sequence)>n or len(sequence)<n): # проверка на корректность данных
        print("Некорректный ввод данных. Введите еще раз")
    else:
        result = calc_median_sum(sequence) # вызов функции для расчета суммы медиан списка чисел
        print(result)  # вывод результата