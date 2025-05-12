import pandas as pd
from sqlalchemy import create_engine

try:
    engine = create_engine('postgresql://postgres:admin@localhost:8080/ny_taxi')
    engine.connect()
except Exception as e:
    print(e)
    print('Could not connect to database')
    exit(1)

data = pd.read_parquet('../data/yellow_tripdata_2024-01.parquet')

pd.io.sql.get_schema(data,name="nyc_yellow_taxi_data",con=engine)

if __name__ == "__main__":
    print(pd.io.sql.get_schema(data,name="nyc_taxi_yellow_data"))
