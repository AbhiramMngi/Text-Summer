from textSummer.config.configuration import ConfigurationManager
from textSummer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
  def __init__(self):
    pass
  
  def main(self):
    config_man = ConfigurationManager()
    model_evaluation_config = config_man.get_model_evaluation_config()
    model_evaluation = ModelEvaluation(model_evaluation_config)
    model_evaluation.evaluate()