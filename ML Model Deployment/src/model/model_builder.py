from loguru import logger

from model.pipelines.model import build_model
from config.config import settings


class ModelBuilderService:
    def __init__(self):
        self.model_path = settings.model_path
        self.model_name = settings.model_name

    def train_model(self):
        logger.info(
            f'building the model at'
            f'{self.model_path}/{self.model_name}',
        )
        build_model()