class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_s = [0] * n
        pref_s[0] = nums[0]
        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]
        return pref_s