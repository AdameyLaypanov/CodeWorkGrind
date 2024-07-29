def ok(mid, sp, k):
    cnt = 0
    s = 0
    for i in range(len(sp)):
        if sp[i] > mid:
            return False

        if s + sp[i] > mid:
            cnt += 1
            s = sp[i]
        else:
            s += sp[i]
    if s > 0:
        cnt += 1
    return cnt <= k


n, k = map(int, input().split())
sp = list(map(int, input().split()))
l = 0
r = 10 ** 14
ans = 0
while l <= r:
    mid = (l + r) // 2
    if ok(mid, sp, k):
        r = mid - 1
        ans = mid
    else:
        l = mid + 1

print(ans)