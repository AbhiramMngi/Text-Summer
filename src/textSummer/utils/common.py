import os 
from box.exceptions import BoxValueError
import yaml 
from textSummer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  """
  Read a yaml file and return a ConfigBox object.

  Args:
    path_to_yaml (Path): Path to the yaml file.

  Raises:
    ValueError: If the yaml file is empty.

  Returns:
    ConfigBox: A ConfigBox object.
  """
  try:
    with open(path_to_yaml, "r") as yaml_file:
      config = yaml.safe_load(yaml_file)
      logger.info("yaml file: {} loaded successfully".format(path_to_yaml))
      return ConfigBox(config)

  except BoxValueError:
    raise ValueError("YAML file is empty")
  
  except Exception as e:
    raise e
  

print("helooo")
def create_directories(path_to_directories: list, verbose = True) -> int:
  """ create list of directories

    Args: 

      path_to_directories (list): list of directories to be created
      
      verbose (bool, optional): whether or not to print the directory path. Defaults to True.
  """
  for path in path_to_directories:
    if path.strip() != "": os.makedirs(path, exist_ok=True)
    if verbose:
      logger.info(f"Created directory: {path}")
  return 0


@ensure_annotations
def get_size(path: Path) -> str:
  """ get the size of a file or directory

    Args:
      path (Path): path to the file or directory

    Returns:
      str: the size of the file or directory
  """
  size_in_kb = round(os.path.getsize(path)/1024)
  return f"{size_in_kb} KB"

