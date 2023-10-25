import pandas as pd
import numpy as np
from src.exceptions import custom_error_handler
from src.logging import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import sys 
import os

@dataclass
class dataIngestionConfig():
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")

class dataingestion:
    def __init__(self):

        self.ingestionpath = dataIngestionConfig()
    
    def initiate_data_ingestion(self):


        logging.info("starting the data ingestion")

        
        try:
            df = pd.read_csv("data\stud.csv")
            #os.makedirs(os.path.dirname(self.ingestionpath.test_data_path),exist_ok=True)

            os.makedirs(os.path.dirname(self.ingestionpath.train_data_path),exist_ok=True)

            logging.info("successfully read the data into dataframe")

            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)

            logging.info("data is split into train and test data sets")

            df.to_csv(self.ingestionpath.raw_data_path)

            train_data.to_csv(self.ingestionpath.train_data_path)
            
            test_data.to_csv(self.ingestionpath.test_data_path)

            logging.info("saved the data into the artifacts folder")
        except Exception as e:
            raise custom_error_handler(e,sys)

if __name__ == '__main__':
    obj = dataingestion()
    obj.initiate_data_ingestion()
    