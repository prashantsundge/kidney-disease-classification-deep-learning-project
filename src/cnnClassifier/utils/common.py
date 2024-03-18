import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import path
from typing import Any
import base64



@ensure_annotations

def read_yaml(path_to_yaml : path) -> ConfigBox:
    """
    reads yaml file and returns 

    Args:
        path to yaml (str): path like input

    raises:
         valueError : if yaml file is empty 
         e: empty file

    return :
    configeBox: configBox type
    """

    try:
        with open (path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise valueError("Yaml file is emtpy ")
    except exceptions as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    '''
    create list of diredtories

    Args:
        path_to_directories(list): list of path of directories 
        ignore_log(bool, optional): ignore if multiple dirs is to be created. 
    '''

    for path in path_to_directories:
        os.makdirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")
    
@ensure_annotations
def save_json(path:path,data:dict):
    """Save json data

    Args: 
        path(path):path to json file
        data(dict): data  to be saved in json file
    """
    with open(path, 'W') as f:
        json.dump(data, f, indent-4)

    logger.info(f"json file saved : {path}")

@ensure_annotations
def load_json(path:path) ->ConfigBox:
    """Load json files data 
    Args:
        path(path):path to json file

    return:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content =json.load(f)

    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:path):
    """Save binary file

    Args:
        data(Any): data to be saved as binary    
        path(path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'Binary files saved at {path}')


@ensure_annotations
def load_bin(path:path) -> Any:
    """Load Binary data
    Args:
        path(path): path to binary file
    returns:
        any object stored in the file 
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path:path) ->str
    """get size in kb

    Args:
        path(path): path of the file

    return:
    str: sixe in kb
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring, filename):
    imgdata =base64.b64decode(imgstring)
    with open(filename,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64decode(f.read())
        