class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        ans = ""
        for i in range(1, min_len + 1):
            prefix = strs[0][:i]
            flag = True
            for j in range(len(strs)):
                if strs[j][:i] != prefix:
                    flag = False
                    break
            if flag:
                ans = prefix
            else:
                break
        return ans