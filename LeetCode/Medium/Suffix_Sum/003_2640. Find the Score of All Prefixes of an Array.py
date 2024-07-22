class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        sp = []
        pref_max = 0
        for i in range(n):
            pref_max = max(pref_max, nums[i])
            s = s + pref_max + nums[i]
            sp.append(s)
        return sp
