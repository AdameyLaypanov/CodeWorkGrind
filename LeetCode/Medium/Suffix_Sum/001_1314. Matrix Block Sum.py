class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        pref_s = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                pref_s[i][j] = mat[i][j]
                if i - 1 >= 0:
                    pref_s[i][j] += pref_s[i - 1][j]
                if j - 1 >= 0:
                    pref_s[i][j] += pref_s[i][j - 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    pref_s[i][j] -= pref_s[i - 1][j - 1]

        ans = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(n - 1, i + k)
                c2 = min(m - 1, j + k)

                ans[i][j] = pref_s[r2][c2]
                if r1 - 1 >= 0:
                    ans[i][j] -= pref_s[r1 - 1][c2]
                if c1 - 1 >= 0:
                    ans[i][j] -= pref_s[r2][c1 - 1]
                if r1 - 1 >= 0 and c1 - 1 >= 0:
                    ans[i][j] += pref_s[r1 - 1][c1 - 1]

        return ans