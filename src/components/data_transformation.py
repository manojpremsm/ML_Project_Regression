import pandas as pd
import numpy as np
import os
from src.components.data_ingestion import dataingestion
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

@dataclass
class dataTransformationConfig:

    preprocessor_obj_file_path = os.path.join("artifact","preprocessor.pkl")
class dataTransformation:

    def __init__(self):

        self.train_data_path = dataingestion().initiate_data_ingestion()[0]
        self.test_data_path = dataingestion().initiate_data_ingestion()[1]

    def data_encoding(self,data_frame):

        num_features = data_frame.select_dtypes(exclude="object").columns
        cat_features = data_frame.select_dtypes(include="object").columns



        numeric_transformer = StandardScaler()
        oh_transformer = OneHotEncoder()

        preprocessor = ColumnTransformer(
            [
                ("OneHotEncoder", oh_transformer, cat_features),
                ("StandardScaler", numeric_transformer, num_features),        
            ]
        )
        data_frame_processed = preprocessor.fit_transform(data_frame)

        return data_frame_processed


    def data_processing(self):

        df_train = pd.read_csv(self.train_data_path)
        df_test = pd.read_csv(self.test_data_path)
        X_train = df_train.drop(columns=['math_score'],axis=1)
        X_test = df_test.drop(columns=['math_score'],axis=1)
        Y_train = df_train['math_score']
        Y_test = df_test['math_score']
        X_train_processed = self.data_encoding(X_train)
        X_test_processed = self.data_encoding(X_test)

        return (X_train_processed,X_test_processed,Y_train,Y_test)


if __name__=='__main__':
    obj1 = dataTransformation()
    x,x1,y,y1 = obj1.data_processing()
    print(x)