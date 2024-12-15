import pandas as pd
from config.config import settings
from loguru import logger


def load_data(path = settings.data_file_name ):
    logger.info(f"loading csv file at path {path}")
    data = pd.read_csv(path)
    return data

