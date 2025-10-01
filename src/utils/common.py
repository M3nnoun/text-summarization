import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any,List


@ensure_annotations
def read_yaml(path_to_yaml :Path) -> ConfigBox:
    """Reads a yaml file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    Raises:
        BoxValueError: If the yaml file is empty.
        Exception: If there is an error reading the yaml file.
    Returns:
        ConfigBox: Contents of the yaml file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise BoxValueError("YAML file is empty")
            logger.info(f"YAML file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as box_error:
        raise box_error
    except Exception as e:
        raise e


def create_directories(path_to_directories: List[Path], verbose: bool = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"Created directory at: {path}")
    
@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB, MB, or GB.

    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in KB, MB, or GB.
    """
    size_in_bytes = os.path.getsize(path)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024
    return f"{size_in_bytes:.2f} PB"
