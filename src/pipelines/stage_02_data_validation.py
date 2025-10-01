from src.components.data_validation import DataValidation
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logging import logger


class DataValidationPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config = ConfigurationManager().get_data_validation_config()
        data_validation = DataValidation(config=config)
        data_validation.validate_all_files_exist()