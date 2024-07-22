class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        length = len(x_str)

        for i in range(length // 1):
            if x_str[i] != x_str[length - 1 - i]:
                return False

        return True