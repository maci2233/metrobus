from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
import math

def get_distance_between_two_points(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

class GeoLocationService:
    geolocator = Nominatim(user_agent="metrobus")

    @classmethod
    def get_coords_from_location_name(cls, location_name):
        return cls.geolocator.geocode(location_name, timeout=10).raw

    @staticmethod
    def find_closest_location_name_from_coords(location_coords, coords):
        min_distance = 9999999
        closest_location = ""
        for location_name, location_coords in location_coords.items():
            distance = get_distance_between_two_points(location_coords, coords)
            if distance < min_distance:
                min_distance = distance
                closest_location = location_name
        return closest_location
        