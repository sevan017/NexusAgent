"""
@Author: wcy
@File: main.py
@Date: 2026/6/26 19:31
@Desc: cli 主入口，使用argparse 解析命令行，支持--version和ping子命令
"""
import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(prog="kama_claude", description="KamaClaude CLI")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("ping", help="Ping the core daemon")

    args = parser.parse_args()
    if args.version:
        cmd_version()
        return
    if args.command == "ping":
        config = get_config()
        setup_logging(config)
        cmd_ping(config)
    else:
        parser.print_help()
        sys.exit(1)