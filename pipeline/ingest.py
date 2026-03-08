import pandas as pd 
import os 

def ingest_data(filepath: str)-> pd.DataFrame:

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")

    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    filepath = "../data/raw/user_clicks.csv" 
    df = ingest_data(filepath)
    print(df.head())