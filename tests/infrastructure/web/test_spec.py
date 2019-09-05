from typing import List
from instark.infrastructure.web.spec import ResourcePlugin


def test_resource_plugin():
    resource_plugin = ResourcePlugin()
    operations: List = []
    resource_plugin.path_helper("", operations=operations)
    assert len(operations) == 0
