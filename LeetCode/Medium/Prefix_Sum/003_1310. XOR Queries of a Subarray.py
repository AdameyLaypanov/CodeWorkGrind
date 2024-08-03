class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        xor_pref = [0] * n
        xor_pref[0] = arr[0]
        for i in range(1, n):
            xor_pref[i] = xor_pref[i - 1] ^ arr[i]

        ans = []
        for i in range(len(queries)):
            l, r = queries[i]
            temp = xor_pref[r]
            if (l - 1 >= 0):
                temp ^= xor_pref[l - 1]
            ans.append(temp)
        return ans