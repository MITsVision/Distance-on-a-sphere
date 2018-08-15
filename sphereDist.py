import numpy as np
import math
def haversine_distance(lat1, long1, lat2, long2):
      R = 6371  #radius of earth in kilometers
      #R = 3959 #radius of earth in miles
      phi1 = np.radians(lat1)
      phi2 = np.radians(lat2)

      delta_phi = np.radians(lat2-lat1)
      delta_lambda = np.radians(long2-long1)

      #a = sin²((φB - φA)/2) + cos φA . cos φB . sin²((λB - λA)/2)
      a = np.sin(delta_phi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0) ** 2

      #c = 2 * atan2( √a, √(1−a) )
      c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))

      #d = R*c
      d = (R * c) #in kilometers
  return d
