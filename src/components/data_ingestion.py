## Reading the data required for some module (components are the modules that we are going to be using in the project)
## Data Ingestion is very importent to read the data from a specific data source
## So, we have to read the data, spilt it into train and test data and then only data transformation will be happening

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## In my data ingestion component if any data input is required, we'll give it through this DataIngestionConfig class
@dataclass ## this decorator will help us to define class variables without using init (used only when we have just variables  to define, if you have function also using __init__ is better)
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts', 'train.csv') ## train data output will be given to this file
    test_data_path : str = os.path.join('artifacts', 'test.csv') ## test data output will be given to this file
    raw_data_path : str = os.path.join('artifacts', 'raw.csv') ## raw data output will be given to this file

class DataIngestion :
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        ## if data is stored in some database (for eg) then here the code to to connect and read from that data source
        logging.info('Entered the Data Ingestion method')
        try :
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            os.makedirs(os.path.dirname((self.ingestion_config.train_data_path)), exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)
            logging.info("Train Test Split Initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            logging.info("Ingestion of data is completed")

            return (
                ## returning this info for data transformation
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()