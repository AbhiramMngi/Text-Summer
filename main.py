from textSummer.logging import logger
from textSummer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from textSummer.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from textSummer.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from textSummer.pipeline.stage04_model_train import ModelTrainingPipeline
from textSummer.pipeline.stage05_model_evaluation import ModelEvaluationPipeline


try:
  STAGE_NAME = 'Data Ingestion stage'

  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  data_ingestion = DataIngestionTrainingPipeline()
  data_ingestion.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

  STAGE_NAME = 'Data Validation stage'

  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  data_validation = DataValidationTrainingPipeline()
  data_validation.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

  STAGE_NAME = "Data Transformation stage"

  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  data_transformation = DataTransformationTrainingPipeline()
  data_transformation.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")
  
  STAGE_NAME = "Model Training stage"

  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  model_training = ModelTrainingPipeline()
  model_training.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")

  STAGE_NAME = "Model Evaluation stage"

  logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
  model_evaluation = ModelEvaluationPipeline()
  model_evaluation.main()
  logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===================x")
except Exception as e:
  raise e