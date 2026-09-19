class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the coordinates of the closest point on the rectangle to the circle center
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point
        distance_x = xCenter - nearest_x
        distance_y = yCenter - nearest_y
        squared_distance = (distance_x ** 2) + (distance_y ** 2)
        
        # If the squared distance is less than or equal to the squared radius, they overlap
        return squared_distance <= (radius ** 2)
