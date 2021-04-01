from apscheduler.schedulers.blocking import BlockingScheduler
from orm_service import ORMService
from models import Metrobus
from metrobus_service import MetrobusConsumer, MetrobusMapService

#Constant to determine the next range of metrobus records to retrieve from the dataframe
metrobus_data_range_n = 0

def storeMetrobusData():
    """
    Retrieve metrobus data from the dataset file and persist it in the DB
    """
    global metrobus_data_range_n
    metrobus_df = metrobus_consumer.read_metrobus_df_in_range(metrobus_data_range_n, metrobus_data_range_n + 3)
    metrobus_list = MetrobusMapService.map_metrobus_df_to_metrobus_models(metrobus_df)
    for metrobus in metrobus_list:
        db.insert_data(metrobus)
    metrobus_data_range_n += 3

db = ORMService()
db.create_tables()

metrobus_consumer = MetrobusConsumer("metrobus_data.csv")

#Create scheduler job to persist storeMetrobusData every X amount of seconds
scheduler = BlockingScheduler()
scheduler.add_job(storeMetrobusData, 'interval', seconds=20)
scheduler.start()