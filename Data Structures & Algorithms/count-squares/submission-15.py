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
            t_x, t_y = point
            e_x, e_y = e_point
            dx, dy = e_x-t_x, e_y-t_y
            if abs(dx) == abs(dy) and dx != 0:
                corner1 = (t_x, e_y)
                corner2 = (e_x, t_y)
                counter += self.points[e_point] * self.points.get(corner1, 0) * self.points.get(corner2, 0)
        return counter