def ok(mid, a, k):
    s = 0
    for j in range(len(a)):
        s += int(a[j] / mid)
    return s >= k


n, k = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())

l = 0
r = 10 ** 12

for it in range(100):
    mid = (l + r) / 2
    if ok(mid, a, k):
        l = mid
        ans = mid
    else:
        r = mid

print(ans)
