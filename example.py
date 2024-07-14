from pathlib import Path
import pandas as pd
from VRCDataImporter.LogFileImporters import read_log_file_without_further_formatting, segregate_by_tag_to_dict, segregate_by_tag_to_dataframe_arrays, RawLogLine

# This just gets the example file path
current_path: Path = Path(__file__)
current_folder: Path = current_path.parent
file_name: Path = Path("example_log.txt")
example_log_file_path: Path = current_folder.joinpath(file_name)

# Read the log file into a list of RawLogLine objects, then show an example of segregating them by string tag into a dictionary, or given that the data is a float array, put them in a dataframe with labels
raw_line_objects: list[RawLogLine] = read_log_file_without_further_formatting(example_log_file_path)
filtered: dict = segregate_by_tag_to_dict(raw_line_objects)
data_frame: pd.DataFrame = segregate_by_tag_to_dataframe_arrays(raw_line_objects, "color", ["X", "Y", "Z"] )


print("Program End") # easy breakpoint