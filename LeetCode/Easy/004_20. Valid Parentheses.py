import queue
class Solution:
    def isValid(self, s: str) -> bool:
        sp = queue.LifoQueue()
        par_map = {'(' : 1, '[' : 2, '{' : 3, ')' : -1, ']' : -2, '}' : -3,}
        for i in range(len(s)):
            sym = par_map[s[i]]
            if sym > 0:
                sp.put(sym)
            else:
                if sp.qsize() == 0:
                    return False

                sym2 = sp.get()
                if (sym + sym2 != 0):
                    return False
        return sp.qsize() == 0