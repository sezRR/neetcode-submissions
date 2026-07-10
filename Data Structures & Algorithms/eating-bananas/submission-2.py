class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l + r) // 2
            temp_h = 0
            for p in piles:
                temp_h += math.ceil(p / k)
            if temp_h > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
            