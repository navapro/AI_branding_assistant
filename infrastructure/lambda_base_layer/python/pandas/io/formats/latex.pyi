from pandas.core.dtypes.generic import ABCMultiIndex as ABCMultiIndex
from pandas.io.formats.format import DataFrameFormatter as DataFrameFormatter, TableFormatter as TableFormatter
from typing import Any, IO, Optional

class LatexFormatter(TableFormatter):
    fmt: Any = ...
    frame: Any = ...
    bold_rows: Any = ...
    column_format: Any = ...
    longtable: Any = ...
    multicolumn: Any = ...
    multicolumn_format: Any = ...
    multirow: Any = ...
    caption: Any = ...
    label: Any = ...
    escape: Any = ...
    def __init__(self, formatter: DataFrameFormatter, column_format: Optional[str]=..., longtable: bool=..., multicolumn: bool=..., multicolumn_format: Optional[str]=..., multirow: bool=..., caption: Optional[str]=..., label: Optional[str]=...) -> None: ...
    clinebuf: Any = ...
    def write_result(self, buf: IO[str]) -> None: ...
