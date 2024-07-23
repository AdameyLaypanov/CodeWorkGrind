
def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        pref_xor = [0] * n
        pref_xor[0] = nums[0]
        for i in range(1, n):
            pref_xor[i] = (pref_xor[i - 1] ^ nums[i])

        max_num = (1 << maximumBit) - 1
        ans = [0] * n
        for i in range(n):
            ans[i] = (pref_xor[n - i - 1] ^ max_num)
        return ans