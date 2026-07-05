class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for numb, freq in freq.items():
            buckets[freq].append(numb)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for bucket_el in buckets[i]:
                res.append(bucket_el)
                if len(res) == k:
                    return res
                