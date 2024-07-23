class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pref_s = [0] * (n + 1)
        for i in range(1, n + 1):
            self.pref_s[i] = self.pref_s[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.pref_s[right + 1] - self.pref_s[left]
