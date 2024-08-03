class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0 for _ in range(n + 1)]
        for start, finish, direct in shifts:
            dir = 1 if direct else -1
            d[start] += dir
            d[finish + 1] -= dir

        sp = []
        for i in range(n):
            if i != 0:
                d[i] += d[i - 1]
            chr_ans = (ord(s[i]) - ord("a") + d[i]) % 26 + ord("a")

            sp.append(chr(chr_ans))
        return "".join(sp)