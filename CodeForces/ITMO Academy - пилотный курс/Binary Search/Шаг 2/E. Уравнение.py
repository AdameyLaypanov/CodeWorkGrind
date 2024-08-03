def ok(mid, c):
    return mid ** 2 + mid ** 0.5 >= c


c = float(input())

l = 0
r = 10 ** 10
ans = 0.0
for i in range(200):
    mid = (l + r) / 2
    if ok(mid, c):
        r = mid
        ans = mid
    else:
        l = mid
print(ans)
