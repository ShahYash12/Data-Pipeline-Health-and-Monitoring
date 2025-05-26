import pandas as pd

def parse_errors(file_path):
    df = pd.read_csv(file_path)
    failed_jobs = df[df['status'] == 'FAILED']
    return failed_jobs
