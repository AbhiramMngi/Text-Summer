from textSummer.logging import logger
from textSummer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'

try:
  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")
except Exception as e:
  raise e