import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logging import logging
from src.exceptions import custom_error_handler

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise custom_error_handler(e, sys)
    
def evaluate(train_x,train_y,test_x,test_y,models):

    try:
        logging.info("i am inside the evaluate function")

        report = {}

        for i in range(len(list(models))):

            model = list(models.values())[i]
            model.fit(train_x,train_y)
            y_train_pred = model.predict(train_x)
            y_test_pred = model.predict(test_x)
            training_model_score = r2_score(train_y,y_train_pred)
            testing_model_score = r2_score(test_y,y_test_pred)
            report[list(models.keys())[i]] = testing_model_score
            
        return report
    except Exception as e:
        raise custom_error_handler(e,sys)
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
