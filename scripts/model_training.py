import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(df):
    X = df[['age', 'weight', 'height']]
    y = df['calories_needed']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    error = mean_absolute_error(y_test, y_pred)
    return model, error

if __name__ == "__main__":
    data_file = 'data/processed_user_data.csv'
    df = load_data(data_file)
    model, error = train_model(df)
    print(f"Model trained with MAE: {error}")

