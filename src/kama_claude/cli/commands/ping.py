"""
@Author: wcy
@File: ping.py
@Date: 2026/6/27 10:01
@Desc: 
"""
import asyncio
import json
import sys
import time

import kama_claude
from kama_claude.core.config import KamaConfig


# 同步入口： 运行ping 协程，连接失败时打印错误并退出
def cmd_ping(config: KamaConfig) -> None:
    try:
        asyncio.run(_ping(config))
    except (ConnectionRefusedError, OSError) as e:
        print(f"error: core not running ({config.host:{config.port}})", file=sys.stderr)
        exit(1)


# 向 core 守护进程发送ping请求， 打印pong 响应和延迟
async def _ping(config: KamaConfig) -> None:
    t0 = time.monotonic()
    reader, writer = await asyncio.open_connection(config.host, config.port)

    req = {
        "jsonrpc": "2.0",
        "id": "cli-1",
        "method": "core.ping",
        "params": {"client": f"cli/{kama_claude.__version__}"},
    }
    writer.write((json.dumps(req) + "\n").encode())
    await writer.drain()

    line = await asyncio.wait_for(reader.readline(), timeout=10.0)
    latency_ms = (time.monotonic() - t0) * 1000

    writer.close()
    await writer.wait_closed()

    raw =json.loads(line)
    if "error" in raw:
        err = JsonRpcError.model_validate(raw)