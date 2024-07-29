def ok(min, x, y, n):
    return mid // x + mid // y >= (n - 1)


n, x, y = map(int, input().split())

l = 0
r = 2 * 10 ** 18
ans = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, x, y, n):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
if n == 1:
    print(min(x, y))
else:
    print(ans + min(x, y))
