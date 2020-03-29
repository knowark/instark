from typing import (Sequence, List, Dict, Union, Tuple, Any, 
TypeVar, MutableMapping)

#T = TypeVar('T')

TermTuple = Tuple[str, str, Union[str, int, float, bool, list, tuple]]

#QueryDomain = List[Union[str, TermTuple]]

QueryDomain = Sequence[Union[str, TermTuple]]

DataDict = MutableMapping[str, Any]

RecordList = List[DataDict]