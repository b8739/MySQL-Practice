import os
import pandas as pd
from app import engine

# EDA function
dataset_df = pd.read_csv(os.path.join('static','iris.csv'))
table_name = 'Dataset'
dataset_df.to_sql (
    table_name,
    engine,
    if_exists='fail',
    index=False,
    chunksize=500,
    method='multi'
)
