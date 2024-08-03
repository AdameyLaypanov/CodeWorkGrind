class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        pref_s = [0] * n

        pref_s[0] = nums[0]
        for i in range(1, n):
            pref_s[i] = pref_s[i - 1] + nums[i]

        rem = pref_s[-1] % p

        if rem == 0:
            return 0

        mod_map = {0: -1}
        min_length = n

        for i in range(n):
            current_sum = pref_s[i]
            current_mod = current_sum % p
            target_mod = (current_mod - rem + p) % p

            if target_mod in mod_map:
                min_length = min(min_length, i - mod_map[target_mod])

            mod_map[current_mod] = i

        return min_length if min_length < n else -1
