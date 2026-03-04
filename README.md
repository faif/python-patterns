# README.md — вставки с диаграммами Mermaid

> Ниже показаны **три блока**, которые нужно вставить в `README.md` перед таблицей каждого раздела.
> Каждый блок отделён от окружающего текста пустой строкой (требование GitHub Markdown renderer).

---

## 🔵 Вставка 1 — перед таблицей **Creational Patterns**

Место: сразу после строки `## Creational Patterns` и перед строкой `| Pattern | Description |`

```markdown
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
```

| Pattern | Description |
```

---

## 🟢 Вставка 2 — перед таблицей **Structural Patterns**

Место: сразу после строки `## Structural Patterns` и перед строкой `| Pattern | Description |`

```markdown
## Structural Patterns

> Patterns that define **how classes and objects are composed** to form larger, flexible structures.

```mermaid
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
```

| Pattern | Description |
```

---

## 🟠 Вставка 3 — перед таблицей **Behavioral Patterns**

Место: сразу после строки `## Behavioral Patterns` и перед строкой `| Pattern | Description |`

```markdown
## Behavioral Patterns

> Patterns concerned with **communication and responsibility** between objects.

```mermaid
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
```

| Pattern | Description |
```

---

> **Примечание для ревьюеров:** диаграммы намеренно упрощены — цель показать *ключевое взаимодействие* каждой группы, а не полную UML-схему каждого паттерна. Детали реализации — в `.py`-файлах.

