## Code to train the model (and pushing the file to the cloud)
import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object_as_pklfile, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try :
            logging.info("Splitting training and test input data")
            X_train, Y_train, X_test, Y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest" : RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-Neighbors Regressor" : KNeighborsRegressor(),
                "XGBRegressor" : XGBRegressor(),
                "CatBoosting Regressor" : CatBoostRegressor(verbose=False),
                "AdaBoost Regressor" : AdaBoostRegressor()
            }
            
            model_report : dict = evaluate_models(X_train = X_train, y_train = Y_train, X_test = X_test, y_test = Y_test, models = models )

            #Best model selection depending on the r2 score
            best_model_score = max(sorted(model_report.values()))

            ## Getting the best model's name
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6 : ## threshold setting
                raise CustomException("No best model found")
            
            save_object_as_pklfile(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )
            
            ## Predicted output 
            predicted_output = best_model.predict(X_test)
            r2_sc = r2_score(Y_test, predicted_output)
            return r2_sc
        
        except Exception as e :
            raise CustomException(e, sys)