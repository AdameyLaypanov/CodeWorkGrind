class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        pref_s = [0] * n
        pref_s[0] = nums[0]

        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]

        sp = []
        for i in queries:
            k = 0
            for j in pref_s:
                if j <= i:
                    k += 1
                else:
                    break
            sp.append(k)
        return sp