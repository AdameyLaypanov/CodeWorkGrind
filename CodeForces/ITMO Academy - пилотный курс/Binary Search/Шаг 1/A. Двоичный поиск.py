def good(mid, sp, x):
    return sp[mid] <= x


n, k = map(int, input().split())
sp = list(map(int, input().split()))
q = list(map(int, input().split()))

for x in q:
    l = 0
    r = n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if good(mid, sp, x):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    if sp[ans] == x:
        print('YES')
    else:
        print('No')
