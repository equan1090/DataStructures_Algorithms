# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        return self.findShip(sea, topRight, bottomLeft)
        
        
    def findShip(self, sea, topRight, bottomLeft):
        if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
            return 0
        
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            if sea.hasShips(topRight, bottomLeft):
                return 1
            else:
                return 0
        
        
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        mid = Point(midX, midY)
        
        topLeftQ = self.findShip(sea, Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y+1))
        topRightQ = self.findShip(sea, topRight, Point(mid.x+1, mid.y+1))
        bottomLeftQ = self.findShip(sea, Point(mid.x, mid.y), bottomLeft)
        bottomRightQ = self.findShip(sea, Point(topRight.x, mid.y), Point(mid.x+1, bottomLeft.y))
        return topLeftQ + topRightQ + bottomLeftQ + bottomRightQ
        
        '''
        -----------------
        |       |       |
        |       |       |
mid+1   |---------------
        |       |       |
        |       |       |
BLx     |       |       |
        -----------------
               mx mx+1
        '''
        
        
        