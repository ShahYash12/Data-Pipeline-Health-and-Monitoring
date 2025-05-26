import pandas as pd
from datetime import datetime, timedelta

def check_data_freshness(file_path):
    df = pd.read_csv(file_path)
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    stale = df[df['last_updated'] < datetime.now() - timedelta(hours=6)]
    return stale
