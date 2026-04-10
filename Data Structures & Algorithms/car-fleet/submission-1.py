class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        lists = zip(*sorted(list(zip(position, speed))))
        position, speed = map(list, lists)
        st = []
        fleets = n
        st.append((target - position[0]) / speed[0])
        for i in range(1, n):
            time = (target - position[i]) / speed[i]
            while st and time >= st[-1]:
                st.pop()
                fleets -= 1
            st.append(time)
        
        return fleets