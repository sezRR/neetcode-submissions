class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key: (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        store = self.store[key]
        l, r = 0, len(store) - 1
        while l <= r:
            m = (l + r) // 2
            if store[m][0] == timestamp:
                return store[m][1]
            elif store[m][0] > timestamp:
                r = m - 1
            else:
                res = store[m][1]
                l = m + 1
        return res
