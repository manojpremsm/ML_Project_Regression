# End to end ml project for student performance prediction.


This project aims to predict the final math score of students based on various features. The project encompasses data ingestion, transformation, model training, and prediction functionalities. The model is stored as a pickle file in the artifact folder after training, which is then utilized for making predictions on new data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Data Ingestion](#data-ingestion)
  - [Data Transformation](#data-transformation)
  - [Model Training](#model-training)
  - [Prediction](#prediction)
- [Requirements](#requirements)
- [License](#license)

## Introduction

Predicting students' final math scores can provide valuable insights for educators to understand factors influencing academic performance. This project offers a comprehensive pipeline for data processing, model training, and prediction to aid in this task.

## Features

- Data ingestion from various sources
- Transformation of raw data into a suitable format for model training
- Training machine learning models to predict students' math scores
- Storing trained models as pickle files for future use
- Prediction on new data using the trained model

## Project Structure

The project follows a structured approach with separate modules for different functionalities:
```
Root:

¦   README.md
¦   requirements.txt
¦   setup.py
¦   
+---artifacts
¦       model.pkl
¦       preprocessor.pkl
¦       raw.csv
¦       test.csv
¦       train.csv
¦           
+---data
¦       stud.csv
¦       
+---src
    ¦   exceptions.py
    ¦   logging.py
    ¦   utils.py
    ¦   __init__.py
    ¦   
    +---components
    ¦       data_ingestion.py
    ¦       data_transformation.py
    ¦       data_transformer.py
    ¦       model_trainer.py
    ¦       __init__.py
    ¦       
    +---pipeline
            predict_pipeline.py
            train_pipeline.py
            __init__.py
            
```
## Usage

### Data Ingestion

To ingest data into the project, place the raw data file  inside the `data/` directory and run the `data_ingestion.py`

### Data Transformation

Run the `data_transformation.py` script to transform the raw data into a suitable format for the training.

### Model Training

Execute the `model_trainer.py` script to train the machine learning model using the processed data. The trained model will be saved as a pickle file (`model.pkl`) in the `artifacts/` directory.

### Prediction

Utilize the trained model for making predictions on new data by running the `predict_pipeline.py` script. Ensure that the data follows the same format as the processed data used for training.

## Requirements

- Python 3.x
- Pandas
- Scikit-learn

Install the required packages using the following command:

`pip install -r requirements.txt`


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


