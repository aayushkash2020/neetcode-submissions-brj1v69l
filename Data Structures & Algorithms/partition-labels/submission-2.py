class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Kinda like merge overlapping intervals
        first_last = {}
        for i, ch in enumerate(s):
            if ch in first_last:
                first_last[ch][1] = i
            else:
                first_last[ch] = [i, i]
        res = []
        for ch, i in first_last.items():
            print(f"{ch}: {i}")
        # Python dicts preserve insertion order
        int_start = int_end = 0
        cur_len = 0
        for _, i in first_last.items():
            a, b = i[0], i[1]
            if a <= int_end:
                int_end = max(int_end, b)
            else:
                res.append(cur_len)
                int_start, int_end = a, b
            cur_len = int_end - int_start + 1
        res.append(cur_len)
        return res 
