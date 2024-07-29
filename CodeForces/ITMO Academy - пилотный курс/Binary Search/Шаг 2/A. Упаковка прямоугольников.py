def ok(mid, w, h, n):
    return (mid // w) * (mid // h) >= n


w, h, n = map(int, input().split())

l = 0
r = 10 ** 18
ans = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, w, h, n):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)