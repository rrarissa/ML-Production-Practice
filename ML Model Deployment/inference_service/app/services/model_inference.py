import pickle as pk
from pathlib import Path

from loguru import logger

from config.config import settings


class ModelInferenceService:

    def __init__(self) -> None:
        """Initialize the ModelInferenceService."""
        self.model = None
        self.model_path = settings.model_path
        self.model_name = settings.model_name

    def load_model(self) -> None:

        logger.info(
            f'checking the existance of model config file at '
            f'{self.model_path}/{self.model_name}',
        )

        model_path = Path(
            f'{self.model_path}/{self.model_name}',
        )

        if not model_path.exists():
            raise FileNotFoundError('Model file does not exist!')

        logger.info(
            f'model {self.model_name} exists! -> '
            'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:

        logger.info('making prediction!')
        return self.model.predict([input_parameters]).tolist()