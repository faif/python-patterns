from __future__ import annotations
from functools import wraps
from typing import Callable, Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def bold(fn: F) -> F:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return f"<b>{fn(*args, **kwargs)}</b>"

    return wrapper  # type: ignore


def italic(fn: F) -> F:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return f"<i>{fn(*args, **kwargs)}</i>"

    return wrapper  # type: ignore


@bold
@italic
def hello() -> str:
    return "hello world"


if __name__ == "__main__":
    print(hello())
