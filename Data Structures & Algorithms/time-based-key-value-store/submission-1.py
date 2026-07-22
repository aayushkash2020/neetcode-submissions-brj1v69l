from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.tm[key]
        l, r = 0, len(entries) - 1
        res = None
        while l <= r:
            m = (l + r) // 2
            cur_time = entries[m][0]
            if cur_time > timestamp:
                r = m - 1
            elif cur_time < timestamp:
                res = entries[m][1]
                l = m + 1
            else:
                return entries[m][1]
        return res or ""
