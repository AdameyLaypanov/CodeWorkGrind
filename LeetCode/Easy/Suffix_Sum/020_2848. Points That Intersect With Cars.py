class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        n = len(nums)
        used = [0] * 102
        for i in range(n):
            start, end = nums[i]
            used[start] += 1
            used[end + 1] -= 1
        for i in range(1, len(used)):
            used[i] += used[i - 1]
        ans = 0
        for i in range(len(used)):
            if used[i] != 0:
                ans += 1
        return ans
