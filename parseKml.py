from pykml import parser

filename = "./waypts.kml"
with open(filename) as f:
  folder = parser.parse(f).getroot().Document.Placemark

lst = []
points = []

for pm in folder:
  lst.append(pm.Point.coordinates)
  points.append(lst)
  lst=[]

print(points)
#for x in range(len(lstlarge)): 
#print points
    #print "\n" 
'''

root = parser.fromstring(open(filename, 'r').read())
print root.Document.Placemark.Point.coordinates

'''



'''
filename = "./waypts.kml"
with open(filename) as f:
  folder = parser.parse(f).getroot().Document.Placemark

lst = []
points = []
largelist = []
for pm in folder:
  lst.append(pm.Point.coordinates)
  largelist.append(lst)
  lst=[]

print (largelist)
'''

'''
pnt=[]
n=[]
for i in points:
    for j in i:
         print(j)
         n=j.split(',')
         y=[]
         for k in n:
             y.append(float(k))
         pnt.append(y)
print (pnt)

'''
