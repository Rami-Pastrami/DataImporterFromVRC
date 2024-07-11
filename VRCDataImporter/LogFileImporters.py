from enum import Enum
from pathlib import Path
from LogFileObjects import RawLogLine

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


def read_log_file_without_further_formatting(log_file_path: Path):
    f = open(log_file_path, 'r', encoding='utf8')
    output: list[RawLogLine] = []
    for line in f:
        line_stripped: str = line.strip()
        if not RawLogLine.is_line_export_line(line_stripped):
            continue
        output.append(RawLogLine(line_stripped))




