from VRCDataImporter import (EXPORT_IDENTIFIER, EXPORT_SEPERATOR,
                             DATA_PARTITION,
                             HEADER_TYPE)

class RawLogLine:
    def __init__(self, line: str):
        if EXPORT_IDENTIFIER not in line:
            raise Exception("This line does not seem to be a log exported line!")
        isolated_line: str = line.split(EXPORT_IDENTIFIER)[1]
        components: list[str] = isolated_line.split(EXPORT_SEPERATOR)
        self.tag: str = components[0]
        self.partition_type: DATA_PARTITION = DATA_PARTITION(components[1])
        self.data_type: HEADER_TYPE = HEADER_TYPE(components[2])
        self.raw_string: str = components[3]
        self.processed_value = None
        match(self.data_type):
            case HEADER_TYPE.HEADER_CSV:
                self.processed_value = self._process_string_as_csv(self.raw_string)
            case _:
                raise NotImplementedError


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
                except
                    continue
        return elements


