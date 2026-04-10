class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        cur_time = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > cur_time:
                fleets += 1
                cur_time = time
        
        return fleets