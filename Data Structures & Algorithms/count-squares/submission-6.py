from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.rows = defaultdict(lambda: defaultdict(int))
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.rows[y][x] += 1
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        for x2, cnt in self.rows[y].items():
            if x2 == x:
                continue
            d = x2 - x
            res += (
                cnt *
                self.points[(x, y+d)] *
                self.points[(x2, y+d)]
            )
            res += (
                cnt *
                self.points[(x, y-d)] *
                self.points[(x2, y-d)]
            )
        return res