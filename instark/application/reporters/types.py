from typing import Dict, List, Any, Union, Tuple

DeviceDict = Dict[str, Any]

DeviceDictList = List[DeviceDict]

ChannelDict = Dict[str, Any]

ChannelDictList = List[ChannelDict]

TermTuple = Tuple[str, str, Union[str, int, float, bool, list, tuple]]

SearchDomain = List[Union[str, TermTuple]]
