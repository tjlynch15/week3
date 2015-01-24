# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:
import math
import json
from urllib.request import urlopen

def distance(lat, long):
	dist = math.sqrt((41.793414 - lat)**2 + (-87.600915 - long)**2)
	return dist



webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']
#print(stations)


distances = []
for station in stations:
	#print(station['stationName'])
	#print(station['latitude'])
	#print(station['longitude'])
	#print(distance(station['latitude'], station['longitude']))
	distances.append({'station': station['stationName'],
	 'distance': distance(station['latitude'], station['longitude']),
	  'available_bikes': station['availableBikes']})


min_dist = distances[0]['distance']
#min_station = distances[0]['station']
#min_bikes = distances[0]['available_bikes']


for entry in distances:
	if entry['distance'] < min_dist:
 		min_dist = entry['distance']
 		min_station = entry['station']
 		min_bikes = entry['available_bikes']

#print(min_station, min_dist, min_bikes)
print()
print('The closest station to Young is: ', min_station)
print('There are {0} bikes currently available.'.format(min_bikes))
print()





# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes like x and y coordinates, and calculate distance between locations with the usual Euclidean distance formula.

# 1. Modify the code above to display the station name and number of available bikes for the station closest to Young.

# You will likely want to consult the JSON stream from Divvy

# - http://www.divvybikes.com/stations/json
