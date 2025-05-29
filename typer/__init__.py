"""Minimal Typer stub."""

from __future__ import annotations

import argparse
from typing import Any, Callable


class Typer:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.subparsers = self.parser.add_subparsers(dest="command")

    def command(self, name: str | None = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            cmd_name = name or func.__name__
            sub = self.subparsers.add_parser(cmd_name)
            sub.set_defaults(func=func)
            return func
        return decorator

    def __call__(self) -> None:
        args = self.parser.parse_args()
        if hasattr(args, "func"):
            args.func()


def run(app: Typer) -> None:
    app()
