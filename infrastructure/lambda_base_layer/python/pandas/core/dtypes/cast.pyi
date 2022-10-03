import numpy as np
from pandas._typing import Dtype as Dtype
from pandas.core.dtypes.common import ensure_int16 as ensure_int16, ensure_int32 as ensure_int32, ensure_int64 as ensure_int64, ensure_int8 as ensure_int8, ensure_object as ensure_object, ensure_str as ensure_str, is_bool as is_bool, is_bool_dtype as is_bool_dtype, is_complex as is_complex, is_complex_dtype as is_complex_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64_ns_dtype as is_datetime64_ns_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_datetime_or_timedelta_dtype as is_datetime_or_timedelta_dtype, is_dtype_equal as is_dtype_equal, is_extension_array_dtype as is_extension_array_dtype, is_float as is_float, is_float_dtype as is_float_dtype, is_integer as is_integer, is_integer_dtype as is_integer_dtype, is_numeric_dtype as is_numeric_dtype, is_object_dtype as is_object_dtype, is_scalar as is_scalar, is_string_dtype as is_string_dtype, is_timedelta64_dtype as is_timedelta64_dtype, is_timedelta64_ns_dtype as is_timedelta64_ns_dtype, is_unsigned_integer_dtype as is_unsigned_integer_dtype, pandas_dtype as pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype as DatetimeTZDtype, ExtensionDtype as ExtensionDtype, IntervalDtype as IntervalDtype, PeriodDtype as PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeArray as ABCDatetimeArray, ABCDatetimeIndex as ABCDatetimeIndex, ABCPeriodArray as ABCPeriodArray, ABCPeriodIndex as ABCPeriodIndex, ABCSeries as ABCSeries
from pandas.core.dtypes.inference import is_list_like as is_list_like
from pandas.core.dtypes.missing import isna as isna, notna as notna
from pandas.util._validators import validate_bool_kwarg as validate_bool_kwarg
from typing import Any, Optional

def maybe_convert_platform(values: Any) -> Any: ...
def is_nested_object(obj: Any) -> bool: ...
def maybe_downcast_to_dtype(result: Any, dtype: Any) -> Any: ...
def maybe_downcast_numeric(result: Any, dtype: Any, do_round: bool=...) -> Any: ...
def maybe_upcast_putmask(result: np.ndarray, mask: np.ndarray, other: Any) -> Any: ...
def maybe_promote(dtype: Any, fill_value: Any = ...) -> Any: ...
def infer_dtype_from(val: Any, pandas_dtype: bool=...) -> Any: ...
def infer_dtype_from_scalar(val: Any, pandas_dtype: bool=...) -> Any: ...
def infer_dtype_from_array(arr: Any, pandas_dtype: bool=...) -> Any: ...
def maybe_infer_dtype_type(element: Any) -> Any: ...
def maybe_upcast(values: Any, fill_value: Any = ..., dtype: Any = ..., copy: bool=...) -> Any: ...
def invalidate_string_dtypes(dtype_set: Any) -> None: ...
def coerce_indexer_dtype(indexer: Any, categories: Any) -> Any: ...
def coerce_to_dtypes(result: Any, dtypes: Any) -> Any: ...
def astype_nansafe(arr: Any, dtype: Any, copy: bool=..., skipna: bool=...) -> Any: ...
def maybe_convert_objects(values: np.ndarray, convert_numeric: bool=...) -> Any: ...
def soft_convert_objects(values: np.ndarray, datetime: bool=..., numeric: bool=..., timedelta: bool=..., coerce: bool=..., copy: bool=...) -> Any: ...
def convert_dtypes(input_array: Any, convert_string: bool=..., convert_integer: bool=..., convert_boolean: bool=...) -> Dtype: ...
def maybe_castable(arr: Any) -> bool: ...
def maybe_infer_to_datetimelike(value: Any, convert_dates: bool=...) -> Any: ...
def maybe_cast_to_datetime(value: Any, dtype: Any, errors: str=...) -> Any: ...
def find_common_type(types: Any) -> Any: ...
def cast_scalar_to_array(shape: Any, value: Any, dtype: Optional[Any] = ...) -> Any: ...
def construct_1d_arraylike_from_scalar(value: Any, length: int, dtype: Any) -> Any: ...
def construct_1d_object_array_from_listlike(values: Any) -> Any: ...
def construct_1d_ndarray_preserving_na(values: Any, dtype: Any = ..., copy: bool=...) -> Any: ...
def maybe_cast_to_integer_array(arr: Any, dtype: Any, copy: bool=...) -> Any: ...
