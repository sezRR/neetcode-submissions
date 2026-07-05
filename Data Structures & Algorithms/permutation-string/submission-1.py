class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_hash, window = {}, {}
        for c in s1:
            s1_hash[c] = s1_hash.get(c, 0) + 1

        have, need, need_len = 0, len(s1), len(s1_hash)
        l = 0
        for r in range(len(s2)):
            if s2[r] in s1_hash:
                window[s2[r]] = window.get(s2[r], 0) + 1
                if window[s2[r]] == s1_hash[s2[r]]:
                    have += 1
            if r - l + 1 > need:
                if s2[l] in s1_hash:
                    if window[s2[l]] == s1_hash[s2[l]]:
                        have -= 1
                    window[s2[l]] -= 1
                l += 1
            if have == need_len:
                return True
        return False