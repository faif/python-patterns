from __future__ import annotations
import weakref
from typing import Tuple

class Card:
    _pool: weakref.WeakValueDictionary[Tuple[str, str], Card] = weakref.WeakValueDictionary()

    def __new__(cls, value: str, suit: str) -> Card:
        obj = cls._pool.get((value, suit))
        if not obj:
            obj = object.__new__(cls)
            cls._pool[(value, suit)] = obj
        return obj

    def __init__(self, value: str, suit: str) -> None:
        self.value = value
        self.suit = suit

    def __repr__(self) -> str:
        return f"<Card: {self.value}{self.suit}>"

if __name__ == "__main__":
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(f"c1 is c2: {c1 is c2}")
