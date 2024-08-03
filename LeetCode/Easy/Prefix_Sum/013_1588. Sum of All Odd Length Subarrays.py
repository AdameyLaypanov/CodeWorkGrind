arr = [1,4,2,5,3]

n = len(arr)
prefix_sums = [0] * n

prefix_sums[0] = arr[0]
for i in range(1, n):
    prefix_sums[i] = prefix_sums[i - 1] + arr[i]

total_sum = 0

for i in range(n):
    for j in range(i, n):
        length = j - i + 1
        if length % 2 == 1:
            if i == 0:
                total_sum += prefix_sums[j]
            else:
                total_sum += prefix_sums[j] - prefix_sums[i - 1]

print(total_sum)
