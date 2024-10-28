import math

class Point:
    def __init__(self, axisX, axisY):
        self.axisX = axisX
        self.axisY = axisY
        
    def __str__(self):
        return 'Point ('+ str(self.axisX) +','+ str(self.axisY) +')'


# P1x, P1y = map(int, input("Enter the cartesian coordinates for Point 1: ").split(','))
# P2x, P2y = map(int, input("Enter the cartesian coordinates for Point 2: ").split(','))
# P1 = Point(P1x, P1y)
# P2 = Point(P2x, P2y)

P1 = Point(1,4)
print(P1)

P2 = Point(3,12)
print(P2)


class Distance:
    distanceType = "Euclidean Distance"
    
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.x1 = self.startPoint.axisX
        self.y1 = self.startPoint.axisY
        
        self.endPoint = endPoint
        self.x2 = self.endPoint.axisX
        self.y2 = self.endPoint.axisY
        
        
    def calculateDistance(self):
        # Euclidean Distance
        # D = ( x2 − x1 )2 + ( y2 − y1 )2 
        self.DistanceResult = math.sqrt( pow( (self.x2 - self.x1), 2) + pow( (self.y2 - self.y1), 2) )
        
        return self.DistanceResult
    
        
    def __str__(self):
        self.calculateDistance()
        
        return Distance.distanceType + ": P1(" +str(self.x1)+ ", " +str(self.y1)+ ") to P2(" +str(self.x2)+ "," +str(self.y2) +") = " + str(self.DistanceResult)




class manhattanDistance(Distance):
    def calculateDistance(self):
        # Manhattan Distance
        # D = |x2 − x1| + |y2 − y1|
        self.DistanceResult = abs(self.x2 - self.x1) + abs(self.y2 - self.y1)
        
        Distance.distanceType = "Manhattan Distance"
        
        return self.DistanceResult

    
class chebyshevDistance(Distance):
    def calculateDistance(self):
        # chebyshevDistance
        # D = max(|x2 − x1|, |y2 − y1|)
        self.DistanceResult = max( abs(self.x2 - self.x1) , abs(self.y2 - self.y1) )
        
        Distance.distanceType = "Chebyshev Distance"
        
        return self.DistanceResult

# return 'x1 = '+ str(self.x1) + '\ny2 = '+ str(self.y2) + '\nx2 = '+ str(self.x2) + '\ny2 = '+ str(self.y2)    
#     D = ( x2 − x1 )2 + ( y2 − y1 )2 
# Euclidean distance: P1(1, 2) to P2(3, 7) = 5.39
# Manhattan distance: P1(1, 2) to P2(3, 7) = 7.00
# Chebyshev distance: P1(1, 2) to P2(3, 7) = 5.00

print('')


# P1_P2 = Distance(P1,P2)
# print('Euclidean Distance: ')
print(Distance(P1,P2))


print('')
# print('Manhattan Distance: ')
print(manhattanDistance(P1,P2))


print('')
# print('Chebyshev Distance: ')
print(chebyshevDistance(P1,P2))
