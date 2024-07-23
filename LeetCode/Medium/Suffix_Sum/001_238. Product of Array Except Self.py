class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        preff, suff = 1, 1

        for i in range(n):
            ans[i] *= preff
            preff *= nums[i]

        for i in range(n - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]

        return ans