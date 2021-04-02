from apscheduler.schedulers.blocking import BlockingScheduler

from services.metrobus_service import MetrobusConsumer, MetrobusMapService
from models import Metrobus
from services.orm_service import ORMService
from services.geolocation_service import GeoLocationService
from constants.constants import DELEGATIONS, MEXICO_CITY

#Constant to determine the next range of metrobus records to retrieve from the dataframe
metrobus_data_range_n = 0


def storeMetrobusData():
    """
    Retrieve metrobus data from the dataset file and persist it in the DB
    """
    global metrobus_data_range_n
    metrobus_df = metrobus_consumer.read_metrobus_df_in_range(metrobus_data_range_n, metrobus_data_range_n + 3)
    metrobus_list = MetrobusMapService.map_metrobus_df_to_metrobus_models(metrobus_df)
    #for each metrobus model we find its delegation based on its coordinates and then store it in the DB
    for metrobus in metrobus_list:
        metrobus_coords = (metrobus.latitude, metrobus.longitude)
        closest_delegation = GeoLocationService.find_closest_location_name_from_coords(delegation_coords, metrobus_coords)
        metrobus.delegation = closest_delegation
        db.insert_data(metrobus)
    metrobus_data_range_n += 3

def get_delegations_coords(delegation_list):
    """
    Get the coordinates (latitude, longitude) for all the delegations

    params:
    - delegation_list(List[string]): List containing the name of all delegations

    returns:
    delegation_coords(dict) where each key is the name of the delegation and each value a tuple containing (latitude,longitude)
    """
    delegation_coords = {}
    for delegation in delegation_list:
        coords = GeoLocationService.get_geo_info_from_location_name(f"{delegation}, {MEXICO_CITY}")
        delegation_coords[delegation] = (float(coords["lat"]), float(coords["lon"]))
    return delegation_coords


if __name__ == "__main__":

    delegation_coords = get_delegations_coords(DELEGATIONS)

    db = ORMService()
    db.create_tables()

    metrobus_consumer = MetrobusConsumer("metrobus_data.csv")

    #Create scheduler job to persist storeMetrobusData every X amount of seconds
    scheduler = BlockingScheduler()
    scheduler.add_job(storeMetrobusData, 'interval', seconds=10)
    scheduler.start()
