from typing import Dict, List, Any, TypeVar


ProviderDict = Dict[str, Any]

ProvidersDict = Dict[str, ProviderDict]

ProvidersList = List[ProviderDict]

Registry = Dict[str, Any]

Factory = TypeVar('Factory')

Factories = Dict[str, Factory]

Config = Dict[str, str]