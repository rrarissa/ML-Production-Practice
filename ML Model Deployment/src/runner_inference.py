from model.model_inference import ModelInferenceService
from loguru import logger


@logger.catch
def main():
    ml_svc = ModelInferenceService()
    ml_svc.load_model()
    pred = ml_svc.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
    logger.info(f"prediction = {pred}")


if __name__ == '__main__':
    main()