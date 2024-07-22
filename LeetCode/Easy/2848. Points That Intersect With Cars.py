def sumOddLengthSubarrays(arr):
    n = len(arr)
    prefix_sums = [0] * n

    prefix_sums[0] = arr[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + arr[i]

    total_sum = 0

    # Итерация по всем возможным подмассивам
    for i in range(n):
        for j in range(i, n):
            length = j - i + 1
            if length % 2 == 1:  # Проверяем, что длина нечетная
                total_sum += prefix_sums[j + 1] - prefix_sums[i]

    return total_sum
arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))