from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage03_model_training import ModelTraingPipeline
from cnnClassifier.pipeline.stage04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<")
    
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "prepare base model"

try:
    logger.info(f"***********************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"************************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<")

except Exception as e:
     logger.exception(e)
     raise e

STAGE_NAME ="Training"

try:
    logger.info(f"***********************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
    model_trainer = ModelTraingPipeline()
    model_trainer.main()
    logger.info(f"************************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed <<<<<<<<<<<")

except Exception as e:
     logger.exception(e)
     raise e



STAGE_NAME ="Evaluation Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<")
    
    except Exception as e:
        logger.exception(e)
        raise e