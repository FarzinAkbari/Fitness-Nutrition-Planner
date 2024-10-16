import pytest
import pandas as pd
from scripts.model_training import load_data, train_model

def test_load_data():
    df = load_data('data/test_processed_user_data.csv')
    assert not df.empty

def test_train_model():
    data = {'age': [25, 30, 35], 'weight': [70, 80, 90], 'height': [175, 180, 185], 'calories_needed': [2000, 2200, 2400]}
    df = pd.DataFrame(data)
    model, error = train_model(df)
    assert model is not None
    assert isinstance(error, float)

