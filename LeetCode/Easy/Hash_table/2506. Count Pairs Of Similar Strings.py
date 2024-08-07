class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            v = [0] * 26
            for j in range(len(word)):
                v[ord(word[j]) - ord('a')] = 1
            v = tuple(v)
            if v in dic:
                dic[v] += 1
            else:
                dic[v] = 1
        final = 0
        for i in dic:
            k = dic[i]
            final += k * (k - 1) // 2