class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1

    def count(self, point: List[int]) -> int:
        # use find_squares to count all successfully found squares
        counter = 0
        for e_point in self.points:
            dx, dy = e_point[0]-point[0], e_point[1]-point[1]
            if abs(dx) == abs(dy) and dx != 0:
                corner1 = (point[0], e_point[1])
                corner2 = (e_point[0], point[1])
                counter += self.points[e_point] * self.points.get(corner1, 0) * self.points.get(corner2, 0)
        return counter