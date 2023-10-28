import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exceptions import custom_error_handler
from src.logging import logging
import os

from src.utils import save_object

@dataclass
class dataTransformationConfig:

    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class dataTransformation:

    def __init__(self):

        self.data_transformation_object = dataTransformationConfig()

    def get_data_transformer(self):

        try:

            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                    "gender",
                    "race_ethnicity",
                    "parental_level_of_education",
                    "lunch",
                    "test_preparation_course",
                ]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]

            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoding",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(

                 [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]
                )


            return preprocessor

        except Exception as e:
            raise custom_error_handler(e,sys)


    def initiate_data_processing(self,train_data_path,test_data_path):

        try:

            df_train = pd.read_csv(train_data_path)
            df_test = pd.read_csv(test_data_path)
            
            logging.info("training and test data read")

            preprocessing_obj = self.get_data_transformer()

            print("value of preprocessing object",preprocessing_obj)

            input_train_df = df_train.drop(["math_score"],axis=1)
            target_train_df = df_train["math_score"]

            input_test_df = df_test.drop(["math_score"],axis=1)
            target_test_df = df_test["math_score"]

            logging.info("seperated the input and target for training and test data")

            input_train_feature = preprocessing_obj.fit_transform(input_train_df)
            input_test_feature = preprocessing_obj.transform(input_test_df)

            train_arr = np.c_[
                input_train_feature,np.array(target_train_df)

            ]

            test_arr = np.c_[
                input_test_feature,np.array(target_test_df)
                ]

            save_object(

                file_path=self.data_transformation_object.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_object.preprocessor_obj_file_path
            )
        except Exception as e:
            raise custom_error_handler(e,sys)


