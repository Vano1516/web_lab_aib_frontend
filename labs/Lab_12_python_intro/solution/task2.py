def alg(a):
    medians = []
    for i in range(1, len(a) + 1):
        subsequence = a[:i]
        subsequence.sort()
        length = len(subsequence)
        if length % 2 == 1:
            median = subsequence[length // 2]
        else:
            median = (subsequence[length // 2 - 1] + subsequence[length // 2]) / 2

        medians.append(median)

    median_sum = sum(medians)
    return int(median_sum)
print("Введите данные")
a = list(map(int, input().split()))
print(alg(a))

