import ConfigParser

configParser = ConfigParser.ConfigParser()
configParser.readfp(open(r'distanceConfigFile.txt'))
distance = configParser.get('distanceBetweenTwoWaypoints', 'distance')
print (distance)
