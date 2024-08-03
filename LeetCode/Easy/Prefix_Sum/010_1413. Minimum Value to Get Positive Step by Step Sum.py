class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        pref_s = [0] * n
        pref_s[0] = nums[0]
        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]

        answer = 1 - min(pref_s) if min(pref_s) < 0 else 1

        return answer