from textSummer.config.configuration import ConfigurationManager
from textSummer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config_man = ConfigurationManager()
    data_validation_config = config_man.get_data_validation_config()
    data_validation = DataValidation(data_validation_config)
    data_validation.validate_all_files_exist()