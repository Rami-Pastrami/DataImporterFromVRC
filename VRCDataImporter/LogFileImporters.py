from enum import Enum
from pathlib import Path
from InitialLogFileImporting import RawLogLine

# Following Settings affect parsing of log data.
# Ensure this matches the export settings Unity side
EXPORT_IDENTIFIER: str = "!DATA!"
EXPORT_SEPERATOR: str = "|!"
HEADER_STRING: str = "STR"
HEADER_CSV: str = "CSV"
HEADER_2DCSV: str = "2D_CSV"
HEADER_JSON: str = "JSON"

class DATA_PARTITION(Enum):
    FULL: int = 0
    START: int = 1
    MIDDLE: int = 2
    END: int = 3
    DYNAMIC: int = 4

class HEADER_TYPE(Enum):
    HEADER_STRING: int = 0
    HEADER_CSV: int = 1
    HEADER_2DCSV: int = 2
    HEADER_JSON: int = 3

class ReadLogFile:
    def __init__(self, log_file_path: Path):
        f = open(log_file_path, 'r', encoding='utf8')
        


