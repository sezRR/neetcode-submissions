class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort()
        max_freq = freq[25]

        max_freq_count = 0
        for f in freq:
            if f == max_freq:
                max_freq_count += 1

        t = (max_freq - 1) * (n + 1) + max_freq_count

        return max(len(tasks), t)