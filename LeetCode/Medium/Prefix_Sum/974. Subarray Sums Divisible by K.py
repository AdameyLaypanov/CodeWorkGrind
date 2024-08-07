class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {}
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] += pref[i - 1] + nums[i - 1]
        answer = 0
        for i in range(n + 1):
            pref[i] = (pref[i] + k) % k
            if pref[i] in dic:
                answer += dic[pref[i]]

            if pref[i] in dic:
                dic[pref[i]] += 1
            else:
                dic[pref[i]] = 1
        return answer