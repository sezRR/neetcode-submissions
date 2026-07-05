class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {}
        t_h = {}
        for c in s:
            s_h[c] = s_h.get(c, 0) + 1
        for c in t:
            t_h[c] = t_h.get(c, 0) + 1
        return s_h == t_h