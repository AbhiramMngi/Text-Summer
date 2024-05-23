import os 
from textSummer.entity import DataValidationConfig

class DataValidation:
  def __init__(
      self,
      config: DataValidationConfig
  ):
    self.config = config

  def validate_all_files_exist(self) -> bool:
    try:  
      validation_status = True 

      all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

      for file in self.config.ALL_REQUIRED_FILES:

        validation_status = file in all_files

        with open(self.config.STATUS_FILE, "w") as f:
          f.write(f"Validation Status: {validation_status}")

        if not validation_status: return validation_status

      return validation_status
    
    except Exception as e:
      raise e
      
