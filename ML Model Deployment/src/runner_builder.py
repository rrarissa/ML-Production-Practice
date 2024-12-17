from model.model_builder import ModelBuilderService
from loguru import logger


@logger.catch
def main():
    logger.info("train model")
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == '__main__':
    main()