"""
@Author: wcy
@File: events.py
@Date: 2026/6/27 10:14
@Desc: 事件模型与 Event 联合类型定义——daemon 向客户端推送的事件入口，新增事件需在此扩展联合类型
"""
from __future__ import annotations
# Literal 用于限定 type 字段为精确字符串字面量；Annotated 用于构造带判别器的联合类型
from typing import Literal, Annotated

# BaseModel 为 pydantic 数据基类；Discriminator 根据字段值将联合类型路由到具体子类
from pydantic import BaseModel, Discriminator

# 核心启动事件，daemon 完成监听后广播
class CoreStartedEvent(BaseModel):
    # 判别字段，固定为 "core.started"，用于联合类型路由
    type: Literal["core.started"] = "core.started"
    # daemon 实际监听的地址（host:port 格式）
    listen_addr: str
    # 当前核心版本号
    version: str

# 事件联合类型——根据 type 字段值自动判别为具体事件类（当前仅有 CoreStartedEvent）
Event = Annotated[CoreStartedEvent, Discriminator("type")]
