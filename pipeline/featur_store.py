import pandas as pd

def load_clean_data():
    # Step 1 — load the cleaned data
    df = pd.read_csv("../data/processed/user_clicks_clean.csv")
    return df


def select_features(df):
    # Step 2 — choose only the columns needed for modeling
    feature_columns = [
        "user_id",
        "hour",
        "day",
        "month",
        "page"
    ]

    df = df[feature_columns]
    return df


def save_features(df):
    # Step 3 — save the feature dataset
    df.to_csv("../data/features/user_clicks_features.csv", index=False)


def run_feature_pipeline():
    df = load_clean_data()
    df = select_features(df)
    save_features(df)


if __name__ == "__main__":
    run_feature_pipeline()