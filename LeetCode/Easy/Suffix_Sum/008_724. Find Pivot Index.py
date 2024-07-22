class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pref_s = [0] * n
        suff_s = [0] * n

        pref_s[0] = nums[0]
        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]

        suff_s[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_s[i] = suff_s[i + 1] + nums[i]

        for i in range(n):
            left_sum = 0
            right_sum = 0
            if i - 1 >= 0:
                left_sum = pref_s[i - 1]
            if i + 1 < n:
                right_sum = suff_s[i + 1]
            if left_sum == right_sum:
                return i
        return -1
