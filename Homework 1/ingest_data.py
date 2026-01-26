#!/usr/bin/env python
# coding: utf-8

import pandas as pd

from sqlalchemy import create_engine

from tqdm.auto import tqdm

import click # to get params from cli 

import inspect




dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

# @click.option('--year', help='Year of the data to ingest', default=2021, type=int)
# @click.option('--month', help='Month of the data to ingest', default=1, type=int)

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

def choosen_function(**kwargs):
    if kwargs.get('path', '').endswith('.csv'):
        #replace path with filepath_or_buffer for pandas function
        kwargs['filepath_or_buffer'] = kwargs.pop('path')
        func = pd.read_csv
    else:
        func = pd.read_parquet
    filtered_kwargs = filter(lambda k: k in inspect.signature(func).parameters.keys(), kwargs.keys())
    valid_kwargs = {k: kwargs[k] for k in filtered_kwargs}
    return func, valid_kwargs




@click.command() # allows us to run the function from the command line
@click.option('--path', help='Path to the CSV file to ingest', required=True)
@click.option('--pg-user', help='Postgres username', default='root')
@click.option('--pg-pass', help='Postgres password', default='root')
@click.option('--pg-host', help='Postgres host', default='localhost')
@click.option('--pg-port', help='Postgres port', default='5432')
@click.option('--pg-db', help='Postgres database name', default='ny_taxi')
# @click.option('--chunksize', help='Number of rows to process at a time', default=100, type=int)
@click.option('--tablename', help='Name of the table to write data to', default='yellow_taxi_data')

def run (path, pg_user, pg_pass, pg_host, pg_port, pg_db, tablename):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # if filepath.endswith('.csv'):
    #     func = pd.read_csv
    # else:
    #     func = pd.read_parquet

    # Read first row to get column names
    func, valid_kwargs = choosen_function(path=path, nrows=0)
    df_sample = func(**valid_kwargs)
    cols = df_sample.columns.tolist()
    
    # Filter dtype and parse_dates to only include columns that exist
    valid_dtype = {k: v for k, v in dtype.items() if k in cols}
    valid_parse_dates = [d for d in parse_dates if d in cols]

    func, valid_kwargs = choosen_function(path=path, dtype=valid_dtype, parse_dates=valid_parse_dates)

    df_to_ingest = func(
            **valid_kwargs
        )

    first = True
    for chunk in tqdm(range(0, len(df_to_ingest), 10)):
        if first:
            df_to_ingest.iloc[chunk:chunk+10].head(0).to_sql(name=tablename, con=engine, if_exists='replace')
            first = False
        df_to_ingest.iloc[chunk:chunk+10].to_sql(name=tablename, con=engine, if_exists='append')
    
    # df_to_ingest_tqdm = tqdm(df_to_ingest)

    # if file_type == 'csv':

    #     #CSV to Postgres
        

        
    #     first = True
    #     for df_chunk in tqdm(df_to_ingest):
    #         if first:
    #             df_chunk.head(0).to_sql(name=tablename, con=engine, if_exists='replace')
    #             first = False
    #         df_chunk.to_sql(name=tablename, con=engine, if_exists='append')
    # else:
 
    # # df.to_sql(name=tablename, con=engine, if_exists='replace')


if __name__ == '__main__':
    run()