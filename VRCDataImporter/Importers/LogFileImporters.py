from pathlib import Path

# Following Settings affect parsing of log data.
# Ensure this matches the export settings Unity side
EXPORT_IDENTIFIER: str = "!DATA!"
EXPORT_SEPERATOR: str = "|!"
HEADER_STRING: str = "STR"
HEADER_CSV: str = "CSV"
HEADER_2DCSV: str = "2D_CSV"
HEADER_JSON: str = "JSON"


def read_log_file_without_further_formatting(log_file_path: Path):
    f = open(log_file_path, 'r', encoding='utf8')
    output: list[LogFileObjects.RawLogLine] = []
    for line in f:
        line_stripped: str = line.strip()
        if not LogFileObjects.RawLogLine.is_line_export_line(line_stripped):
            continue
        output.append(LogFileObjects.RawLogLine(line_stripped))




