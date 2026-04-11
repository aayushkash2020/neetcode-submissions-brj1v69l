from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = []
        self.point_map = defaultdict(dict)


    def add(self, point: List[int]) -> None:
        self.points.append(point)
        if point[1] not in self.point_map[point[0]]:
            self.point_map[point[0]][point[1]] = 0
        self.point_map[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for other_x in self.point_map:
            if other_x == point[0]:
                continue
            for other_y in self.point_map[other_x]:
                if other_y == point[1]:
                    continue
                slope = (other_y - point[1]) / (other_x - point[0])
                if slope != -1 and slope != 1:
                    continue
                foundA = foundB = False
                if point[0] in self.point_map and other_y in self.point_map[point[0]]:
                    a = self.point_map[point[0]][other_y]
                    foundA = True
                if point[1] in self.point_map[other_x]:
                    b = self.point_map[other_x][point[1]]
                    foundB = True
                if not foundA or not foundB:
                    continue
                res += self.point_map[other_x][other_y] * a * b                
        return res