class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key: (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        self.store[key].insert(l, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        print(self.store)
        if r == -1:
            return ""

        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][0] == timestamp:
                return self.store[key][m][1]
            elif self.store[key][m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return self.store[key][r][1] if self.store[key][r][0] <= timestamp else ""
