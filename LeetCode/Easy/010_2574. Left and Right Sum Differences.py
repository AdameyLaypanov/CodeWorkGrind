class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref_s = [0] * n
        suff_s = [0] * n

        pref_s[0] = nums[0]
        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]

        suff_s[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_s[i] = suff_s[i + 1] + nums[i]

        ans = [0] * n
        for i in range(n):
            left_s = 0
            right_s = 0
            if i - 1 >= 0:
                left_s = pref_s[i - 1]
            if i + 1 < n:
                right_s = suff_s[i + 1]
            ans[i] = abs(left_s - right_s)
        return ans