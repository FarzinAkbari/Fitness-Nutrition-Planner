import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def process_data(df):
    df['age'] = df['age'].fillna(df['age'].mean())
    df['weight'] = df['weight'].fillna(df['weight'].mean())
    df['height'] = df['height'].fillna(df['height'].mean())
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    input_file = 'data/user_data.csv'
    output_file = 'data/processed_user_data.csv'

    df = load_data(input_file)
    df = process_data(df)
    save_data(df, output_file)

