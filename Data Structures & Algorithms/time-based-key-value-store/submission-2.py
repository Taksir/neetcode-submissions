import collections
class TimeMap:
    def __init__(self):
        self.mapper = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper:
            return ""
        
        kv_list = self.mapper[key]
        l, r = 0, len(kv_list) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2
            v, t = kv_list[m]

            if t <= timestamp:
                res = v
                l = m + 1
            else:
                r = m - 1

        return res
        

