class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] | nums[i]

        suff = [0] * n
        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = (suff[i + 1] | nums[i])

        ans = 0
        for i in range(n):
            temp = nums[i] * (1 << k)
            res = temp
            if i - 1 >= 0:
                res |= (pref[i - 1])
            if i + 1 < n:
                res |= (suff[i + 1])
            ans = max(ans, res)
        return ans