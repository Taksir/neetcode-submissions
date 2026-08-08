class TimeMap:
    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        l, r = 0, len(self.map[key]) - 1
        ans = ""
        while l <= r:
            mid = l + (r - l) // 2
            t, v = self.map[key][mid]
            if t > timestamp:
                r = mid - 1
            else:
                ans = v
                l = mid + 1
        
        return ans