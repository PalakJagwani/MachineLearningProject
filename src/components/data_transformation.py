## Data Transformation : Using pipeline to encode and standard scaling the data and storing into a pkl file
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object_as_pklfile

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl') ## this pkl file will contain the code to trasform the data as required 

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_tranformer_object(self):
        ## This function is reponsible for data transformation
        try :
            numerical_features = ['writing_score', 'reading_score']
            categorical_features = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]

            ## creating numerical pipeline
            numerical_pipeline = Pipeline(
                steps=[
                ("imputer", SimpleImputer(strategy="median")), ## to handle missing values and outliers
                ("scaler", StandardScaler(with_mean=False)) ## to standardize the data
                ]
            )

            logging.info("Numerical features standard scaling completed") 

            ## creating categorical pipeline
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical features encoding completed")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_features),
                    ("categorical_pipeline", categorical_pipeline, categorical_features)
                ]
            )
            return preprocessor
        
        except Exception as e :
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try :
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading train and test data completed")

            logging.info("Opening pre-processing object")

            preprocessing_obj = self.get_data_tranformer_object()
            target_column_name = 'math_score'

            ## getting x and y datasets on train and test data.
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Appling preprocessing object on train and test dataframe")

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_array, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_array, np.array(target_feature_test_df)
            ]

            save_object_as_pklfile(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            logging.info ("Saved Preprocessing object")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e :
            raise CustomException(e, sys)