import pymongo
import pandas as pd
# Decorator function
from dataclasses import dataclass
import os


@dataclass
class EnvironmentVariable:
    mongo_db_url: str = os.getenv("MONGO_DB_URL")
    # just for example
    aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str =os.getenv("AWS_SECRET_ACCESS_KEY")


# Creating object of class EnvironmentVariable
env_var = EnvironmentVariable()

# Creating client to interect with the database
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"


