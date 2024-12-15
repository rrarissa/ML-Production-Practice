from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath

from loguru import logger


class Settings(BaseSettings):
    """
    BaseSettings is used for creating a settings class to handle configurations
    DirectoryPath & FilePath: These are types from Pydantic that ensure validation for directory paths and file paths.
    """
    model_config = SettingsConfigDict(env_file='config/.env', 
                                      env_file_encoding='utf-8')

    data_file_name: FilePath
    model_path: DirectoryPath
    model_name: str


settings = Settings()

logger.remove()
logger.add("logs/app.log", rotation="1 day", retention="2 days")