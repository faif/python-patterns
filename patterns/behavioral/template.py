from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()

    def base_operation1(self) -> None:
        print("AbstractClass: Doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass: Allowing subclasses to override operations")

    @abstractmethod
    def required_operations1(self) -> None: ...

    def hook1(self) -> None: ...


class ConcreteClass(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass: Implemented Operation1")


if __name__ == "__main__":
    template = ConcreteClass()
    template.template_method()
