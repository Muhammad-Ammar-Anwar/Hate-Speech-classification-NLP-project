from dataclasses import dataclass

@dataclass 
class DataIngersionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str