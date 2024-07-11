from pathlib import Path
from VRCDataImporter.LogFileImporters import read_log_file_without_further_formatting, RawLogLine

current_path: Path = Path(__file__)
current_folder: Path = current_path.parent
file_name: Path = Path("example_log.txt")
example_log_file_path: Path = current_folder.joinpath(file_name)

raw_line_objects: list[RawLogLine] = read_log_file_without_further_formatting(example_log_file_path)

print("Program End") # easy breakpoint

