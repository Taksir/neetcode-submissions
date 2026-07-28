
class TimeMap:

    def __init__(self):
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        pairs = self.times.get(key, [])
        l, r = 0, len(pairs) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if timestamp >= pairs[mid][1]:
                res = pairs[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
