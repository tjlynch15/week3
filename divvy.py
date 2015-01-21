# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import json
from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
stations = result['stationBeanList']
print(stations)

# The Young building has the following latitude and longitude: 41.793414,-87.600915.
# To measure surface distance, you can treat latitudes and longitudes like x and y coordinates, and calculate distance between locations with the usual Euclidean distance formula.

# 1. Modify the code above to display the station name and number of available bikes for the station closest to Young.

# You will likely want to consult the JSON stream from Divvy

# - http://www.divvybikes.com/stations/json
