from typing import Dict, List, Any, Union, Tuple

DeviceDict = Dict[str, Any]

DeviceDictList = List[DeviceDict]

TermTuple = Tuple[str, str, Union[str, int, float, bool, list, tuple]]

SearchDomain = List[Union[str, TermTuple]]
