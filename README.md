# Data Pipeline

A reusable, production-style data pipeline that ingests raw clickstream data, validates it against a schema, transforms it, and stores structured features ready for downstream analytics or machine learning.

---

## Project Overview

This pipeline processes synthetic user behavior data containing events such as `view`, `click`, and `purchase` across different devices, pages, and countries. It is designed to be modular, readable, and extensible.

---

## Technologies Used

- **Python 3.11**
- **Pandas** — data manipulation and transformation
- **PyYAML** — schema validation configuration
- **CSV** — raw and processed data storage

---

## Project Structure
```
Data_pipline/
├── config/
│   └── schema.yaml          # Validation rules and column definitions
├── data/
│   ├── raw/
│   │   └── user_clicks.csv  # Raw generated clickstream data
│   ├── processed/
│   │   └── user_clicks_clean.csv  # Cleaned and transformed data
│   └── features/
│       └── user_clicks_features.csv  # Feature set for analytics/ML
├── notebooks/
│   └── generate_data.py     # Script to generate synthetic data
├── pipeline/
│   ├── ingest.py            # Data ingestion
│   ├── validate.py          # Schema validation
│   ├── transform.py         # Data cleaning and transformation
│   ├── featur_store.py      # Feature selection and storage
│   └── run_pipeline.py      # Runs the full pipeline end to end
├── .gitignore
├── requirements.txt
└── README.md
```

---

## What Each File Does

| File | Description |
|------|-------------|
| `ingest.py` | Loads raw CSV data into a Pandas DataFrame |
| `validate.py` | Validates data against `schema.yaml` — checks columns, nulls, data types, and allowed values |
| `transform.py` | Converts timestamps, removes duplicates, strips whitespace, and extracts time features (hour, day, month) |
| `featur_store.py` | Selects relevant feature columns and saves them to `data/features/` |
| `run_pipeline.py` | Orchestrates all pipeline steps in order with a single command |

---

## How to Install and Run

### 1. Clone the repository
```bash
git clone https://github.com/ahmedbacaad/Data_pipline.git
cd Data_pipline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate the raw data
```bash
python3 notebooks/generate_data.py
```

### 4. Run the full pipeline
```bash
cd pipeline
python3 run_pipeline.py
```

### Output
- Cleaned data → `data/processed/user_clicks_clean.csv`
- Feature set → `data/features/user_clicks_features.csv`