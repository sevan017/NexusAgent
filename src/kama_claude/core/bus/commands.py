"""
@Author: wcy
@File: commands.py
@Date: 2026/6/27 10:14
@Desc: 命令模型与 Command 联合类型定义——所有 JSON-RPC 请求/响应的类型入口，新增命令需在此扩展联合类型
"""
# 将全部注解转为延迟求值，避免前向引用问题（pydantic v2 推荐）
from __future__ import annotations

# Literal 限定 type 字段为精确字符串字面量；Annotated 构造带判别器的联合类型
from typing import Annotated, Literal

# BaseModel 为 pydantic 数据基类；Discriminator 根据字段值将联合类型路由到具体子类
from pydantic import BaseModel, Discriminator


# Ping 请求命令，客户端发送以探测 daemon 是否存活
class PingCommand(BaseModel):
    # 判别字段，标识请求类型
    type: Literal["core.ping"] = "core.ping"
    # 客户端标识（进程名/版本等，用于 daemon 日志区分不同客户端）
    client: str


# Ping 成功后返回的 JSON-RPC result 载荷
class PongResult(BaseModel):
    # daemon 端版本号
    server_version: str
    # daemon 自启动以来的运行时长（毫秒）
    uptime_ms: int
    # 收到 Ping 请求时的 UTC 时间，ISO 8601 格式
    received_at: str


# 命令联合类型——根据 type 字段值自动判别为具体命令类（当前仅有 PingCommand）
Command = Annotated[PingCommand, Discriminator("type")]
