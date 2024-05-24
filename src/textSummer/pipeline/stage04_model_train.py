from textSummer.entity import ModelTrainerConfig
from textSummer.config.configuration import ConfigurationManager
from textSummer.components.model_training import ModelTrainer

class ModelTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
      config_man = ConfigurationManager()
      model_trainer_config = config_man.get_model_trainer_config()
      model_trainer = ModelTrainer(model_trainer_config)
      model_trainer.train()
