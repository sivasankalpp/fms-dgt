# Standard
from typing import Any, Dict, Iterable, Union
import os

# Third Party
from datasets import Dataset
import pandas as pd

DATASET_ROW_TYPE = Union[Dict[str, Any], pd.Series]
DATASET_TYPE = Union[Iterable[DATASET_ROW_TYPE], pd.DataFrame, Dataset]

TYPE_KEY = "type"
NAME_KEY = "name"

DGT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
