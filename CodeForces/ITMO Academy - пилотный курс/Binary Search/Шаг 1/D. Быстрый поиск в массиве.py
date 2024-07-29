def left(x, sp):
    l = 0
    r = n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if sp[mid] >= x:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1

    return ans


def right(x, sp):
    l = 0
    r = n - 1
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if sp[mid] <= x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1

    return ans


n = int(input())
sp = list(map(int, input().split()))
k = int(input())
sp.sort()
for it in range(k):
    l, r = map(int, input().split())
    L = left(l, sp)
    R = right(r, sp)

    if sp[L] >= l and sp[R] <= r:
        print(R - L + 1, end=' ')
    else:
        print(0, end=' ')
