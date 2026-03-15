from ingest import ingest_data
from validate import run_validation
from transform import run_transform
from featur_store import run_feature_pipeline

def run_pipeline():
    filepath = "../data/raw/user_clicks.csv"
    
    print("Starting pipeline... 🚀")
    run_validation(filepath)
    print("Validation done ✅")
    
    run_transform(filepath)
    print("Transform done ✅")
    
    run_feature_pipeline()
    print("Features stored ✅")
    
    print("Pipeline complete! 🎉")

if __name__ == "__main__":
    run_pipeline()
    