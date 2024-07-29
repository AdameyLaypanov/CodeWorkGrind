def getCnt(T: int, t: int, z: int, y: int) -> int:
    cnt = 0
    block = z * t + y
    cntBlocks = T // block
    cnt += cntBlocks * z
    cnt += min((T % block) // t, z)
    return cnt


def ok(T: int, t: [], z: [], y: []) -> bool:
    res = 0
    for i in range(len(t)):
        res += getCnt(T, t[i], z[i], y[i])
    return res


m, n = map(int, input().split())
t = []
z = []
y = []
for i in range(n):
    x1, x2, x3 = map(int, input().split())
    t.append(x1)
    z.append(x2)
    y.append(x3)

l = 0
r = 10 ** 18
T = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, t, z, y) >= m:
        r = mid - 1
        T = mid
    else:
        l = mid + 1
print(T)
for i in range(n):
    cnt = getCnt(T, t[i], z[i], y[i])
    print(min(m, cnt), end=' ')
    m -= cnt
    m = max(m, 0)
