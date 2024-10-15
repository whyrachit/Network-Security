import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN= "Result"
PIPELINE_NAME : str = "Network Security"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

DATA_INGESTION_COLLECTION_NAME: str = "Network_Data"
DATA_INGESTION_DATABASE_NAME: str = "Whyrachit"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = .2

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    'missing_values': np.nan,
    'n_neighbors': 3,
    "weights": 'uniform'
}