from networkSecurity.components.data_ingestion import DataIngestion

from networkSecurity.exception.exception import NetworkSecurityException
from networkSecurity.logging.logger import logging

from networkSecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig

import sys 

if __name__== "__main__":
    try:
        training_config=TrainingPipelineConfig()

        data_ingestion_config = DataIngestionConfig(training_config)
        data_ingestion=DataIngestion(data_ingestion_config)


        logging.info("=inititate the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)