import pytest
from scripts.model import load_model, predict_calories_needed

def test_load_model():
    model = load_model()
    assert model is not None

def test_predict_calories_needed():
    model = load_model()
    age, weight, height = 30, 70, 175
    prediction = predict_calories_needed(model, age, weight, height)
    assert prediction is not None
    assert isinstance(prediction, float)

