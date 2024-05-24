from textSummer.config.configuration import ConfigurationManager
from textSummer.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config_man = ConfigurationManager()
    data_transformation_config = config_man.get_data_transformation_config()
    data_transformation = DataTransformation(data_transformation_config)
    data_transformation.convert()