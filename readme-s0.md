# KamaClaude s0阶段项目分析报告

## 一、项目概述

**KamaClaude** 是一个双进程本地AI Agent系统，由持久化后台守护进程（`kama-core`) 和客户端应用(`kama` CLI/kama tui TUI组成)，进程间通过TCP回环 + JSON-RPC 2.0 NDJSON 通信。 
项目采用Python 3.12 开发，当前处于 s0阶段一项目骨架和协议契约已全部搭建完成，`ping/pong` 往返验证通过。

```
kama CLI                            --请求: {jsonrpc:"2.0", "method":"core.ping", ...}
           --tcp 127.0.0.1:7437 -- 
kama-tui                            --请求: {jsonrpc:"2.0", "result":{...}}
```

---
## 二、项目目录架构
思维导图
https://app.xmind.cn/oqtYbvsa?utm_source=xmind_cn

## 三、src目录详细分析

### 3.1 包入口 - kama_claude/__init__.py
对外暴露__version__="0.0.1" 供整个代码库引用版本号

### 3.2 CLI 客户端
| 文件 | 功能说明 |
|------|------|
|__main__.py | 