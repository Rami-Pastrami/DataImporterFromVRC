from pathlib import Path
import pandas as pd
from VRCDataImporter.LogFileImporters import read_log_file_without_further_formatting, segregate_by_tag_to_dict, segregate_by_tag_to_dataframe_raw_string, RawLogLine

current_path: Path = Path(__file__)
current_folder: Path = current_path.parent
file_name: Path = Path("example_log.txt")
example_log_file_path: Path = current_folder.joinpath(file_name)

raw_line_objects: list[RawLogLine] = read_log_file_without_further_formatting(example_log_file_path)
filtered: dict = segregate_by_tag_to_dict(raw_line_objects)
pd_string: pd.DataFrame = segregate_by_tag_to_dataframe_raw_string(raw_line_objects, "color", "coordinates_as_strings" )


print("Program End") # easy breakpoint

