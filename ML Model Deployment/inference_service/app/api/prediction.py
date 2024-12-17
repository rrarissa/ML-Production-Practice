from flask import Blueprint, abort, request
from pydantic import ValidationError

from schema.apartment import Apartment
from services.model_inference import ModelInferenceService


bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction():
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError as e:
        abort(code=400, description=f'Bad input params: {e.errors()}') 

    model_inference_service = ModelInferenceService()
    model_inference_service.load_model()

    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    return {'prediction': prediction}

