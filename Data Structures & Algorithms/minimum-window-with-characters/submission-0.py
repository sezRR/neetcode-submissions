class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_hash, s_hash = {}, {}
        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1

        res, res_len = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(t_hash)
        for r in range(len(s)):
            c = s[r]
            s_hash[c] = s_hash.get(c, 0) + 1
            if c in t_hash and t_hash[c] == s_hash[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                s_hash[s[l]] -= 1
                if s[l] in t_hash and t_hash[s[l]] > s_hash[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("infinity") else ""