import pandas as pd 
import yaml 
import os 
import sys 
sys.path.append('..')
from pipeline.ingest import ingest_data

"""here i am loading the data and the schema.yaml file to validate everything"""
def load_schema():
 with open("../config/schema.yaml", "r") as f:
    schema = yaml.load(f, Loader=yaml.SafeLoader)
"""here i am checking columns to see if they match and if there is any ,issing values"""
def check_columns(data, schema):
  excepted_columns = schema['columns'].keys()
  actual_columns = data.columns
  if set(excepted_columns) == set(actual_columns):
    print("columns are valid ")
  else:
    missing = set(excepted_columns) - set(actual_columns)
    print(f"missing columns: {missing}")

#here i am checking to see if there is any null in both data and schema 
def check_null(data, schema):
  for each_columns in schema['columns'].keys():
    if schema['columns'] [each_columns] ['nullable']== False:
      nulls = data[each_columns].isnull().sum()
      if nulls > 0:
        print(f"{each_columns} has {nulls} null values")
      else:
        print(f"{each_columns} has no nulls valuse")

# here i am checking id the datatype match and printing if they don't

def check_type(data, schema):
    type_mapping = {
        'integer': 'int64',
        'string': 'object',
        'datetime': 'datetime64[ns]'
    }
    for each_column in schema['columns'].keys():
        expected_type =  schema['columns'][each_column]['type'].keys() # get type from schema, no .keys()
        expected_type = type_mapping[expected_type]  # convert it
        actual_type = data[each_column].dtype  # get dtype from data
        if expected_type == actual_type:
            print(f"{each_column} type is valid ✅")
        else:
            print(f"{each_column} expected {expected_type} but got {actual_type} ❌")

def 

def run_validation(filepath):
  df = ingest_data(filepath)
  schema = load_schema()
  check_columns(df, schema)
  check_null (df, schema)
  check_type (df, schema)
  check_allowed_values(df, schema)
