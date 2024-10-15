import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_tranformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=="__main__":
    
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)

        datatransformationconfig=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(datavalidationartifact,datatransformationconfig)
        logging.info("Initiate the data transformation")
        datatransformationartifact=data_transformation.initiate_data_tranformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)

        modeltrainerconfig=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(modeltrainerconfig,datatransformationartifact)
        logging.info("Initiate Model Training")
        modeltrainingartifact=model_trainer.initiate_model_trainer()
        logging.info("model Training Completed")
        print(modeltrainingartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)