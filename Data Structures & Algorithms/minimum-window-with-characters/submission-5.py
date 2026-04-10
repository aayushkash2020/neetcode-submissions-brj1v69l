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
            if freqs[ch] > 0:
                found += 1
            freqs[ch] -= 1
            if found == len(t):
                while dq and freqs[dq[0][1]] < 0:
                    freqs[dq[0][1]] += 1
                    dq.popleft()
                cur_st, cur_end = dq[0][0], dq[-1][0]
                cur_len = cur_end - cur_st + 1
                if cur_len < best:
                    best = cur_len
                    st, end = cur_st, cur_end
                freqs[s[cur_st]] += 1
                if freqs[s[cur_st]] > 0:
                    found -= 1
                dq.popleft()
        return s[st:end+1] if st is not -1 else ""