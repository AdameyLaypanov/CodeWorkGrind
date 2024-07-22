class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        used = [0] * 52
        for i in range(len(ranges)):
            start, end = ranges[i]
            used[start] += 1
            used[end + 1] -= 1

        for i in range(1, len(used)):
            used[i] += used[i - 1]

        for i in range(left, right + 1):
            if used[i] == 0:
                return False
        return True