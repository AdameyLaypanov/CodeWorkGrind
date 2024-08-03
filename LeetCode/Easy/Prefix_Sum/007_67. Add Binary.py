class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        zeros = '0' * (len(b) - len(a))
        a = zeros + a

        ans = ''
        overflow = 0 
        for i in range(len(a) - 1, -1, -1):
            res = int(a[i]) + int(b[i]) + overflow
            ans += str(res % 2)
            overflow = res // 2

        if overflow == 1:
            ans += '1'
        return ans[::-1]