import pytest
import pandas as pd
from scripts.data_processing import load_data, process_data, save_data

def test_load_data():
    df = load_data('data/test_user_data.csv')
    assert not df.empty

def test_process_data():
    data = {'age': [25, None, 30], 'weight': [70, 80, None], 'height': [175, None, 180]}
    df = pd.DataFrame(data)
    processed_df = process_data(df)
    assert not processed_df.isnull().values.any()

def test_save_data(tmpdir):
    data = {'age': [25, 30], 'weight': [70, 80], 'height': [175, 180]}
    df = pd.DataFrame(data)
    file_path = tmpdir.join('output.csv')
    save_data(df, file_path)
    saved_df = pd.read_csv(file_path)
    assert saved_df.equals(df)

