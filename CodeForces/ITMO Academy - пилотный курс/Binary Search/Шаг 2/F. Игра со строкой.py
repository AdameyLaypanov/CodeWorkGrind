def ok(mid, a, t, p):
    pos_deleted = [0] * len(t)
    for i in range(mid):
        pos_deleted[a[i] - 1] = 1

    used = 0
    for i in range(len(t)):
        if pos_deleted[i]:
            continue
        if used >= len(p):
            break
        if t[i] == p[used]:
            used += 1
    return used >= len(p)


t = input()
p = input()
a = list(map(int, input().split()))
n = len(a)

l = 0
r = n - 1
ans = 0

while l <= r:
    mid = (l + r) // 2
    if ok(mid, a, t, p):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
