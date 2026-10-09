class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        running = [0] * (2 * len(gas))
        running[0] = gas[0] - cost[0]
        streak = 0 if running[0] < 0 else 1
        if streak == len(gas):
            return 0
        for i in range(1, len(running)):
            cur, prev = i % len(gas), (i-1) % len(gas)
            diff = gas[cur] - cost[cur]
            running[i] = max(0, running[i-1]) + diff
            if running[i] >= 0:
                streak += 1
            else:
                streak = 0
            if streak == len(gas):
                return (cur - streak + 1) % len(gas)
        return -1

# -1, 3, -1, 2, 1, 4, 0
        