import numpy as np
import pandas as pd
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.config import mongo_client

def get_collection_as_dataframe(database_name: str,collection_name: str) -> pd.DataFrame:
    """
    Description : This function returns collection as a dataframe.
    --------------------------------------------------------------
    Params:
    database_name : Name of the database.
    collection_name : Name of the collection
    --------------------------------------------------------------
    returns pandas datafrane of a collection.
    """
    try:
        logging.info(
            f"Reading data from database: {database_name} and collection: {collection_name}")
        #converting the collection of data into dataframe as df
        df = pd.DataFrame(
            list(mongo_client[database_name][collection_name].find()))

        # Droping the ID column as it is not relevant
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id", axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        
        return df

    except Exception as e:
        raise SensorException(e, sys)
    
    