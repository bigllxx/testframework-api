from typing import List
import pytest


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        # item表示每个测试用例，解决各种用例名称中文显示问题
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
