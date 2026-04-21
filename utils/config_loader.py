import logging
import yaml # pyright: ignore[reportMissingModuleSource]
from pathlib import Path
from typing import Dict, Any, Union

# Set up a logger for this module
logger = logging.getLogger(__name__)

def load_config(config_path: Union[str, Path] = "config/config.yaml") -> Dict[str, Any]: 
    """
    Loads and parses a YAML configuration file.
    """
    # Convert string to a Path  
    path = Path(config_path)
    
    # Pre-check if the file exists to provide a clearer error message
    if not path.is_file():
        error_msg = f"Configuration file not found at: {path.resolve()}"
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)

    try:
        with open(path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config if config is not None else {}    
    except yaml.YAMLError as exc:
        logger.error(f"Failed to parse YAML syntax in {path}:\n{exc}")
        raise
    except Exception as exc:
        logger.error(f"An unexpected error occurred while loading {path}: {exc}")
        raise