from __future__ import annotations
from typing import Any, Callable

class Dog:
    def __init__(self) -> None:
        self.name = "Dog"
    def bark(self) -> str: return "woof!"

class Cat:
    def __init__(self) -> None:
        self.name = "Cat"
    def meow(self) -> str: return "meow!"

class Adapter:
    def __init__(self, obj: Any, **adapted_methods: Callable) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr: str) -> Any:
        return getattr(self.obj, attr)

if __name__ == "__main__":
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, make_noise=dog.bark))
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))

    for obj in objects:
        print(f"A {obj.name} goes {obj.make_noise()}")
