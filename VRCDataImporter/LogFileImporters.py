from pathlib import Path
from enum import Enum

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

class RawLogLine:
    def __init__(self, line: str):
        if not RawLogLine.is_line_export_line(line):
            raise Exception("This line does not seem to be a log exported line!")
        isolated_line: str = line.split( EXPORT_IDENTIFIER)[1]
        components: list[str] = isolated_line.split(EXPORT_SEPERATOR)
        self.tag: str = components[0]
        self.partition_type: DATA_PARTITION = DATA_PARTITION(int(components[1]))
        self.data_type: HEADER_TYPE = HEADER_TYPE(int(components[2]))
        self.raw_string: str = components[3]
        self.processed_value = None
        match self.data_type:
            case HEADER_TYPE.HEADER_CSV:
                self.processed_value = self._process_string_as_csv(self.raw_string)
            case _:
                raise NotImplementedError

    @staticmethod
    def is_line_export_line(line: str) -> bool:
        return EXPORT_IDENTIFIER in line


    def _process_string_as_csv(self, raw_string: str) -> list:
        elements: list = raw_string.split(",")
        ## Try converting to float, then int, then leave as string
        for i in range(len(elements)):
            try:
                cache = float(elements[i])
                elements[i] = cache
                continue
            except:
                try:
                    cache = int(elements[i])
                    elements[i] = cache
                    continue
                except:
                    continue
        return elements


def read_log_file_without_further_formatting(log_file_path: Path) -> list[RawLogLine]:
    f = open(log_file_path, 'r', encoding='utf8')
    output: list[RawLogLine] = []
    for line in f:
        line_stripped: str = line.strip()
        if not RawLogLine.is_line_export_line(line_stripped):
            continue
        output.append(RawLogLine(line_stripped))
    return output



