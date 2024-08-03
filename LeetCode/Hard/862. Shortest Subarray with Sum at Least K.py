from collections import deque



class Solution(object):
    def shortestSubarray(self, nums, k):

        n = len(nums)
        dq = deque()
        ans = n + 1
        prefix_sum = 0
        min_sum = 0

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum - min_sum >= k:
                ans = min(ans, i + 1)

            print(dq)
            print()
            while dq and prefix_sum - dq[0][1] >= k:
                ans = min(ans, i - dq[0][0])
                dq.popleft()

            while dq and prefix_sum <= dq[-1][1]:
                dq.pop()

            dq.append((i, prefix_sum))
            min_sum = min(min_sum, prefix_sum)

        if ans == n + 1:
            return -1
        return ans


