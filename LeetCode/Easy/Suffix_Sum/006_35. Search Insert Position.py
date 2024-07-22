class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
            answer = 0
            for i in range(len(nums)):
                if nums[i] < target:
                    answer = i + 1
            return answer