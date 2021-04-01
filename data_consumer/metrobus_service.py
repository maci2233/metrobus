import pandas
from pandas import read_csv
from constants.constants import DATE_UPDATED, VEHICLE_ID, LATITUDE, LONGITUDE
from models import Metrobus

class MetrobusConsumer:
    """
    Class used to consume metrobus data coming from csv files
    """

    def __init__(self, filename):
        """
        MetrobusConsumer constructor
        Create a metrobus dataframe with the columns of interest
        
        params:
            - filename(string): Path for csv file containing the metrobus data
        """
        cols = [DATE_UPDATED, VEHICLE_ID, LATITUDE, LONGITUDE]
        self.metrobus_df = read_csv(filename, usecols=cols)


    def read_metrobus_df_in_range(self, start, end):
        """
        Slice the metrobus dataframe for a given range of values

        params:
            - start(int): Starting row for the slice(inclusive)
            - end(int): Ending row for the slice(exclusive)

        returns:
            Sliced metrobus dataframe(Pandas Dataframe) for the given range
        """
        return self.metrobus_df.iloc[start:end]
        

class MetrobusMapService:
    """
    Utility static class to map metrobus data between different structures.
    """
    
    @staticmethod
    def map_metrobus_df_to_metrobus_models(metrobus_df):
        """
        Staticmethod used to map metrobus data in a dataframe to instances of the Metrobus model class

        params:
            - metrobus_df(Pandas Dataframe): Dataframe containing metrobus data

        returns:
        metrobus_list(List[Metrobus]) containing Metrobus models mapped from a metrobus dataframe
        """
        metrobus_list = []
        for ind in metrobus_df.index:
            metrobus = Metrobus()
            metrobus.mayor = "CDMX"
            metrobus.id_metrobus = int(metrobus_df[VEHICLE_ID][ind])
            metrobus.latitute = float(metrobus_df[LATITUDE][ind])
            metrobus.longitude = float(metrobus_df[LONGITUDE][ind])
            metrobus_list.append(metrobus)
        return metrobus_list