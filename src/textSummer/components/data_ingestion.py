import os 
import urllib.request as request 
import zipfile 
from textSummer.logging import logger 
from textSummer.utils.common import get_size 
from textSummer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
  def __init__(self, config: DataIngestionConfig):
    self.config = config

  def download_file(self):
    if os.path.exists(self.config.local_data_file):
      logger.info(f"{self.config.local_data_file} already exists of size: {get_size(Path(self.config.local_data_file))}")
      return 

    filename, headers = request.urlretrieve(
      url = self.config.source_url,
      filename = self.config.local_data_file
    )

    logger.info(f"{filename} downloaded successfully. info: {headers}")
  
  def extract_zip_file(self):
    unzip_path = self.config.unzip_dir

    if not os.path.exists(unzip_path): os.makedirs(unzip_path)

    with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
      zip_ref.extractall(unzip_path)