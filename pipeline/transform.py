#transorming the data we got 
import pandas as pd
from datetime import datetime
import sys
sys.path.append('..')
from pipeline.ingest import ingest_data

from pipeline.validate import check_columns

def convert_timestamp(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df


def remove_duplicates(df):
    df = df.drop_duplicates()
    return df
    


def strip_whitespace(df):
    for column in df.columns:

        if df[column].dtype == "object":
            df [column] = df[column].str.strip()
    return df

def extract_time_features(df):

    df ['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month
    return df
    
def save_processed(df):
    df.to_csv('../data/processed/user_clicks_clean.csv', index=False)

def run_transform(filepath):
    df = ingest_data(filepath)        # ← use ingest not pd.read_csv
    df = convert_timestamp(df)
    df = remove_duplicates(df)
    df = strip_whitespace(df)
    df = extract_time_features(df)
    save_processed(df)
    return df


if __name__ == "__main__":
    filepath = "../data/raw/user_clicks.csv"
    run_transform(filepath)  #  just call it, no df =

