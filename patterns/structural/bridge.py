from __future__ import annotations
from typing import Protocol

class Implementation(Protocol):
    def operation_implementation(self) -> str: ...

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"

class ConcreteImplementationA:
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."

if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    print(abstraction.operation())
