def good(mid, x, v):
    n = len(x)
    max_l = -10 ** 18
    min_r = 10 ** 18
    for i in range(n):
        pos_l = x[i] - v[i] * mid
        pos_r = x[i] + v[i] * mid
        max_l = max(max_l, pos_l)
        min_r = min(min_r, pos_r)
    return max_l <= min_r
n = int(input())
x = [0] * n
v = [0] * n
for i in range(n):
    x[i], v[i] = map(int, input().split())

l = 0
r = 10 ** 9
for i in range(100):
    mid = (l + r) / 2
    if good(mid, x, v):
        r = mid
    else:
        l = mid
print(r)