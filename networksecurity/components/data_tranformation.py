import sys,os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constants.training_pipeline import TARGET_COLUMN,DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.entity.artifact_entity import DataTransformationArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.utils.main_utils.utils import save_numpy_array,save_obj

class DataTransformation:

    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        
        try:
            self.data_validation_artifact: DataValidationArtifact = data_validation_artifact
            self.data_tranformation_config: DataTransformationConfig = data_transformation_config

        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:

        try:
            return pd.read_csv(file_path)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def get_data_transformer_object(cls) -> Pipeline:

        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialised KNN imputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor: Pipeline = Pipeline([("imputer",imputer)])
            return processor
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_tranformation(self) -> DataTransformationArtifact:

        try:
            logging.info("Starting Data Transformation")
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            input_features_traindf=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_traindf=train_df[TARGET_COLUMN]
            target_feature_traindf= target_feature_traindf.replace(-1,0)

            input_features_testdf=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_testdf=test_df[TARGET_COLUMN]
            target_feature_testdf= target_feature_testdf.replace(-1,0)

            preprocessor=self.get_data_transformer_object()
            preprocessor_obj=preprocessor.fit(input_features_traindf)
            transformed_input_train_feature=preprocessor_obj.transform(input_features_traindf)
            transformed_input_test_feature=preprocessor_obj.transform(input_features_testdf)

            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_traindf)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_testdf)]

            save_numpy_array(self.data_tranformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array(self.data_tranformation_config.transformed_test_file_path,array=test_arr)
            save_obj(self.data_tranformation_config.transformed_object_file_path,preprocessor_obj)

            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_tranformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_tranformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_tranformation_config.transformed_test_file_path,
            )
            
            return data_transformation_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)