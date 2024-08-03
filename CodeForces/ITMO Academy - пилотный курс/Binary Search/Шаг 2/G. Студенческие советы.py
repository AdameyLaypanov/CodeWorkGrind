def ok(mid, k, a):
    count = 0
    for students in a:
        count += students // mid
    return count <= mid * k

def solve(k, n, a):
    l = 0
    r = max(a) * n
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if ok(mid, k, a):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans


k = int(input().strip())
n = int(input().strip())
a = [int(input().strip()) for _ in range(n)]


print(solve(k, n, a))
