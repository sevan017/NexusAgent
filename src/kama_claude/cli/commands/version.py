"""
@Author: wcy
@File: version.py
@Date: 2026/6/27 10:02
@Desc: 
"""
from src import kama_claude


# 打印当前kama_claude 包的版本
def cmd_version() -> None:
    print(kama_claude.__version__)