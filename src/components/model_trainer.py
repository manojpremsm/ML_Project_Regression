import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

#from src import exceptions
from src.logging import logging
from src import utils

from src.utils import save_object,evaluate

from src.exceptions import custom_error_handler

@dataclass
class ModelTrainerConfig:

    model_object_path = os.path.join('artifacts','model.pkl')

class model_initiate:

    def __init__(self):

        self.model_path_obj = ModelTrainerConfig()

    def Model_trainer_initialization(self,train_arr,test_arr):

        try:
            logging.info("splitting the train and test data into input and output features")
            X_train,Y_train,X_test,Y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report = evaluate(X_train,Y_train,X_test,Y_test,models)
            logging.info(f"model report is : {model_report}")
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_path_obj.model_object_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(Y_test, predicted)
            return r2_square
        except Exception as e:
            raise custom_error_handler(e,sys)
            





