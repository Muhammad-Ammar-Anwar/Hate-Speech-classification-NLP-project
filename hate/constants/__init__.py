import os 

from datetime import datetime 

TIMESTAMP:str=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFICATS_DIR=os.path.join("artificats",TIMESTAMP)
BUCKET_NAME='NLP HATE-SPEECH'
ZIP_FILE_NAME='dataset.zip'
LABEL='label'
TWEET='tweet'

DATA_INGESTION_ARTIFACTS_DIR="DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR="imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR="raw_data.csv"