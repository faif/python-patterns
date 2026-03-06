# python-patterns

A collection of design patterns and idioms in Python.

## Creational Patterns

> Patterns that deal with **object creation** — abstracting and controlling how instances are made.

```mermaid
graph LR
    Client -->|requests object| AbstractFactory
    AbstractFactory -->|delegates to| ConcreteFactory
    ConcreteFactory -->|produces| Product

    Builder -->|step-by-step| Director
    Director -->|returns| BuiltObject

    FactoryMethod -->|subclass decides| ConcreteProduct
    Pool -->|reuses| PooledInstance
graph TD
    Client --> Facade
    Facade --> SubsystemA
    Facade --> SubsystemB
    Facade --> SubsystemC

    Client2 --> Adapter
    Adapter --> LegacyService

    Client3 --> Proxy
    Proxy -->|controls access to| RealSubject

    Component --> Composite
    Composite --> Leaf1
    Composite --> Leaf2
graph LR
    Sender -->|sends event| Observer1
    Sender -->|sends event| Observer2

    Request --> Handler1
    Handler1 -->|passes if unhandled| Handler2
    Handler2 -->|passes if unhandled| Handler3

    Context -->|delegates to| Strategy
    Strategy -->|executes| Algorithm

    Originator -->|saves state to| Memento
    Caretaker -->|holds| Memento
