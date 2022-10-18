import string
from geopy.distance import geodesic

Chennai=(13.0827,80.2707)
Trivandrum=(8.5241,76.9366)

print(geodesic(Chennai, Trivandrum).km)

