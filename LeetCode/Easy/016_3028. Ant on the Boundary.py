class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        n = len(nums)
        t = 0
        pref_sum = [0] * n
        pref_sum[0] = nums[0]
        for i in range(1, n):
            pref_sum[i] = pref_sum[i - 1] + nums[i]
            if pref_sum[i] == 0:
                t += 1
        return t