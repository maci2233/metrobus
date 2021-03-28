from apscheduler.schedulers.blocking import BlockingScheduler
from orm_service import ORMService
from models import Metrobus

def storeMetrobusData():
    print(">> storeMetrobusDATA Job triggered")
    metrobus = Metrobus()
    metrobus.name = "123"
    metrobus.mayor = "CDMX"
    db.insert_data(metrobus)
    print("<< storeMetrobusDATA Job done")

db = ORMService()
db.create_tables()

scheduler = BlockingScheduler()
scheduler.add_job(storeMetrobusData, 'interval', seconds=20)
scheduler.start()