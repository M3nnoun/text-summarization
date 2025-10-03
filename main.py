from src.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from src.pipelines.stage_02_data_validation import DataValidationPipeline
from src.pipelines.stage_03_data_transformation import DataTransformationPipeline
from src.logging import logger

STAGE_NAME = "Data Transformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
        #data_ingestion = DataIngestionPipeline()
        data_validation = DataValidationPipeline()
        data_transformation = DataTransformationPipeline()

        #data_ingestion.main()
        # data_validation.main()
        data_transformation.main()

        logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e