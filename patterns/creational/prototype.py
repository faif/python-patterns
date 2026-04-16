from __future__ import annotations
import copy
from typing import Any, Dict

class Prototype:
    def __init__(self) -> None:
        self._objects: Dict[str, Any] = {}

    def register_object(self, name: str, obj: Any) -> None:
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        del self._objects[name]

    def clone(self, name: str, **attrs: Any) -> Any:
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class A:
    def __str__(self) -> str:
        return "I am A"

if __name__ == "__main__":
    prototype = Prototype()
    prototype.register_object('a', A())
    b = prototype.clone('a', name='I am B')
    print(b.name)
