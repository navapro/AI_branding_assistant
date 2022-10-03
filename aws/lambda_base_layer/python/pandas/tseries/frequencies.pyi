from pandas._libs.tslibs.resolution import Resolution as Resolution
from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.tseries.offsets import DateOffset as DateOffset
from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Any, Optional

def get_period_alias(offset_str: str) -> Optional[str]: ...
def to_offset(freq: Any) -> Optional[DateOffset]: ...
def get_offset(name: str) -> DateOffset: ...
def infer_freq(index: Any, warn: bool=...) -> Optional[str]: ...

class _FrequencyInferer:
    index: Any = ...
    values: Any = ...
    warn: Any = ...
    is_monotonic: Any = ...
    def __init__(self, index: Any, warn: bool=...) -> None: ...
    def deltas(self) -> Any: ...
    def deltas_asi8(self) -> Any: ...
    def is_unique(self) -> bool: ...
    def is_unique_asi8(self) -> Any: ...
    def get_freq(self) -> Optional[str]: ...
    def day_deltas(self) -> Any: ...
    def hour_deltas(self) -> Any: ...
    def fields(self) -> Any: ...
    def rep_stamp(self) -> Any: ...
    def month_position_check(self) -> Any: ...
    def mdiffs(self) -> Any: ...
    def ydiffs(self) -> Any: ...

class _TimedeltaFrequencyInferer(_FrequencyInferer): ...