from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.mapper = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper or self.mapper[key][0][1] > timestamp:
            return ""
        if self.mapper[key][-1][1] <= timestamp:
            return self.mapper[key][-1][0]
        
        l, r = 0, len(self.mapper[key]) - 1
        ans = ""
        while l <= r:
            mid = l + (r - l) // 2
            if self.mapper[key][mid][1] > timestamp:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return self.mapper[key][ans - 1][0] 

