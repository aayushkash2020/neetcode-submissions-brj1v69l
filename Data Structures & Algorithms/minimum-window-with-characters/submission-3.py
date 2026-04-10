class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = Counter(t)
        dq = deque()
        found = 0
        best = float('inf')
        st = end = -1
        for i, ch in enumerate(s):
            if ch not in freqs:
                continue
            dq.append((i, ch))
            if len(dq) > 1 and ch == dq[0][0]:
                dq.popleft()
                continue
            print(dq)
            if freqs[ch] > 0:
                found += 1
                # print(f"Incrementing found to {found}")
            freqs[ch] -= 1
            # print(f"need {freqs[ch]} more {ch}")
            # print(f"{found=}")
            if found == len(t):
                while dq and freqs[dq[0][1]] < 0:
                    freqs[dq[0][1]] += 1
                    dq.popleft()
                cur_st, cur_end = dq[0][0], dq[-1][0]
                cur_len = cur_end - cur_st + 1
                # print(f"found substring {cur_st}-{cur_end}")
                if cur_len < best:
                    best = cur_len
                    st, end = cur_st, cur_end
                    # print(f"new best: {end-st+1}")
                freqs[s[cur_st]] += 1
                if freqs[s[cur_st]] > 0:
                    found -= 1
                    # print(f"Decrementing found to {found}, need {freqs[s[cur_st]]} more {s[cur_st]}")
                dq.popleft()
        return s[st:end+1] if st is not -1 else ""
            



        pass