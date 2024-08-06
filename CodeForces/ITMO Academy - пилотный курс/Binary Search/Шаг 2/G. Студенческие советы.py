def ok(mid, k, n, a):
    s = 0
    for i in range(n):
        s += min(a[i], mid)

    return s >= k * mid


k = int(input().strip())
n = int(input().strip())
a = [int(input().strip()) for _ in range(n)]

l = 0
r = 10 ** 16
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, k, n, a):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1

print(ans)
