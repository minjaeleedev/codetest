class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # 만나는점이 수직이 아닌 경우 -> 꼭지점이 겹친다
        # for each point of rectangle
        d1 = ((x1 - xCenter) ** 2 + (y1 - yCenter) ** 2) ** 0.5
        d2 = ((x1 - xCenter) ** 2 + (y2 - yCenter) ** 2) ** 0.5
        d3 = ((x2 - xCenter) ** 2 + (y1 - yCenter) ** 2) ** 0.5
        d4 = ((x2 - xCenter) ** 2 + (y2 - yCenter) ** 2) ** 0.5
        if min(d1, d2, d3, d4) <= radius:
            return True

        # 수직이 되는 점 -> 그 점이 radius 내에 있고 선분 내에 있으면 됨
        if y1 <= yCenter <= y2:
            if abs(x1 - xCenter) <= radius:
                return True
            if abs(x2 - xCenter) <= radius:
                return True
            if x1 <= xCenter <= x2:
                return True
        if x1 <= xCenter <= x2:
            if abs(y1 - yCenter) <= radius:
                return True
            if abs(y2 - yCenter) <= radius:
                return True

        return False
