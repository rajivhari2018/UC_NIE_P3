#! /usr/bin/python
import simplekml
import ConfigParser

import doctest
from itertools import permutations
from shapely.geometry import MultiPoint
from shapely.geometry import Point
from  shapely.geometry.polygon import Polygon
from pykml import parser




def readMinDistanceFromConfig():
	configParser = ConfigParser.ConfigParser()
	configParser.readfp(open(r'distanceConfigFile.txt'))
	return float(configParser.get('distanceBetweenTwoWaypoints', 'distance'))



#...........................................................

point= [12.290,76.636]
def isInside(point):
    pointab=Point(point)
    return polygon.contains(pointab)



points=[[12.296261,76.631927],[12.295263,76.641976],[12.284882,76.640571],[12.286098,76.630758]]




polygon= MultiPoint(points).convex_hull
wayPoints=[]
unit=readMinDistanceFromConfig()
unit1=unit/111
unit2=unit/102
def plotWP(point,wayPoints):
    point1=[(point[0]-unit1),point[1]]
    point2=[(point[0]+unit1),point[1]]
    point3=[(point[0]),(point[1]-unit2)]
    point4=[(point[0]),(point[1]+unit2)]
    if not(isInside(point1) and isInside(point2) and isInside(point3) and isInside(point4)):
        point1=[(point[0]-unit1+0.00001),point[1]]
        point2=[(point[0]+unit1-0.00001),point[1]]
        point3=[(point[0]),(point[1]-unit2)+0.00001]
        point4=[(point[0]),(point[1]+unit2-0.00001)]
        if not(isInside(point1) and isInside(point2) and isInside(point3) and isInside(point4)):       
            return None
        wayPoints.append(point)
              
        return None   
    elif point in wayPoints:
        return None
    else:    
        wayPoints.append(point)
        plotWP(point1,wayPoints)
        plotWP(point2,wayPoints)
        plotWP(point3,wayPoints)
        plotWP(point4,wayPoints)
        return None
      
plotWP(point,wayPoints)
for i in wayPoints:
    i.append(0)






#....................................................










def distance(point1, point2):
    return (((point1[0] - point2[0])*111)**2 + ((point1[1] - point2[1])*102)**2+(point1[2]-point2[2])**2) ** 0.5


def total_distance(points):
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])

"""
def travelling_salesman(points):
    start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)
"""
def travelling_salesman(points, start=None):
   
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path

#n=int(input("Enter number of waypoints:"))
#print ("Enter coordinates of waypoints\n")

#points= []
"""
for i in range(n):
    temp=[]
    temp.append(float(input("Enter coordinates of "+str(i+1)+"th point:\n")))
    temp.append(float(input()))
    temp.append(float(input()))
    points.append(temp)
    del(temp)
"""

points1=wayPoints[:]
print ("Way points are:\n")

print (points1)

print("\n\n\n")
path1= travelling_salesman(points1)

print ("Optimal  path is:",path1, "Distance is:", (total_distance(path1)+distance(path1[-1],path1[0])),"kms")




#---------------------------------------------------------------------------


kml = simplekml.Kml()
pointCount = 1
for row in path1:
  kml.newpoint(description="Point"+ str(pointCount),
      coords=[(row[1], row[0],row[2])])          # lon, lat, optional height
  pointCount += 1
kml.save("finalWayPoint.kml")
