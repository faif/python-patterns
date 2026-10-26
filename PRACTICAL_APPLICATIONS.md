# Practical Applications of Design Patterns

## Overview

This document demonstrates how the design patterns implemented in this repository
can be applied to real-world software systems. Each pattern is mapped to practical
use cases across different domains, helping developers understand **when** and **why**
to use each pattern — not just **how**.

---

## 1. Observer Pattern (Behavioral)

### What It Does
Allows an object (Subject) to notify multiple dependent objects (Observers)
automatically when its state changes, without tight coupling between them.

### Real-World Applications

| System | Subject | Observers | Trigger |
|--------|---------|-----------|---------|
| Library Management | Book | Waiting users, Email service | Book returned |
| E-Commerce | Product | Price alert subscribers | Price drops |
| Social Media | User account | Followers | New post published |
| Stock Trading | Stock price | Traders, Alert systems | Price changes |
| IoT / Smart Home | Temperature sensor | AC unit, Dashboard, Phone app | Temperature changes |

### When to Use
- When multiple parts of your system need to react to the same event
- When you want to add new reactions without modifying the event source
- When the number of dependent objects may change at runtime

### When NOT to Use
- When there is only one object that needs to be notified
- When the order of notification matters strictly
- When observers need to respond synchronously in a guaranteed order

### SOLID Principles Applied
- **Open/Closed Principle**: New observers can be added without modifying the Subject
- **Dependency Inversion**: Subject depends on the Observer abstraction, not concrete classes
- **Single Responsibility**: Each observer handles its own reaction logic

---

## 2. Null Object Pattern (Behavioral)

### What It Does
Provides a default do-nothing object instead of returning None/null,
eliminating the need for null checks throughout the codebase.

### Real-World Applications

| System | Real Object | Null Object | Benefit |
|--------|-------------|-------------|---------|
| Library Management | RegisteredUser | GuestUser | Guest can browse without errors |
| E-Commerce | PremiumCustomer | NullCustomer | No crashes on missing accounts |
| Logging System | FileLogger | NullLogger | Disable logging without code changes |
| Payment System | CreditCardProcessor | NullProcessor | Skip payment in test mode |
| Notification System | EmailSender | NullSender | Disable notifications cleanly |

### When to Use
- When you find yourself writing `if obj is not None` repeatedly
- When you want to provide a safe default behavior for missing objects
- When None checks are scattered across multiple modules

### When NOT to Use
- When None/null is a meaningful and expected state
- When the absence of an object should genuinely raise an error
- When performance is critical and even empty method calls matter

### SOLID Principles Applied
- **Liskov Substitution**: NullObject can replace the real object anywhere
- **Open/Closed Principle**: No need to modify existing code to handle null cases
- **Interface Segregation**: Null object implements the same interface

### Code Comparison

**Without Null Object (fragile):**
```python
customer = find_customer(id)
if customer is not None:
    if customer.email is not None:
        customer.send_notification("Hello")
```

**With Null Object (clean):**
```python
customer = find_customer(id)  # Returns NullCustomer if not found
customer.send_notification("Hello")  # Always safe
```

---

## 3. Singleton Pattern (Creational)

### What It Does
Ensures a class has only one instance throughout the entire program
and provides a global access point to that instance.

### Real-World Applications

| System | Singleton Class | Why Only One? |
|--------|----------------|---------------|
| Any Application | DatabaseConnection | One connection pool shared everywhere |
| Any Application | AppConfig | One consistent configuration source |
| Online Exam Platform | ExamConfig | All modules read the same settings |
| ERP System | LicenseManager | One license check for the whole system |
| Game Engine | GameState | One game state shared by all systems |
| Web Server | Logger | One log file, one writer |

### When to Use
- When exactly one instance is needed to coordinate actions across the system
- When that instance needs to be accessible from many different places
- When creating multiple instances would waste resources or cause conflicts

### When NOT to Use
- When you need multiple independent instances
- When unit testing requires isolated instances (use dependency injection instead)
- When the singleton holds mutable state that causes hidden coupling

### SOLID Principles Applied
- **Single Responsibility**: The singleton manages its own instantiation
- **Open/Closed Principle**: Subclasses can extend behavior while maintaining single instance

---

## 4. Specification Pattern (Behavioral)

### What It Does
Encapsulates business rules as standalone objects that can be combined
using boolean logic (AND, OR, NOT) to create complex selection criteria.

### Real-World Applications

| System | Specifications | Combined Rule Example |
|--------|---------------|----------------------|
| Inventory Management | LowStock, InCategory, FromSupplier | Low stock electronics from TechCorp |
| E-Commerce | PriceBelow, InStock, HasDiscount | Cheap available items on sale |
| Library Management | AvailableBook, InGenre, PublishedAfter | Available sci-fi books after 2020 |
| HR System | InDepartment, SeniorityAbove, HasCertification | Senior certified engineers |
| Banking | HighBalance, ActiveAccount, NoOverdraft | Eligible accounts for premium services |

### When to Use
- When filtering logic is complex and changes frequently
- When the same business rules are reused across different modules
- When you need to combine rules dynamically at runtime

### When NOT to Use
- When filtering logic is simple and unlikely to change
- When you have only one or two conditions
- When performance is critical and object creation overhead matters

### SOLID Principles Applied
- **Single Responsibility**: Each specification encapsulates exactly one rule
- **Open/Closed Principle**: New rules are added as new classes, no existing code changes
- **Interface Segregation**: Each specification has one method: is_satisfied_by()

---

## Pattern Selection Guide

### How to Choose the Right Pattern

Do multiple parts of your system need to react to the same event?

└── YES → Observer Pattern
Are you checking if something is None/null in many places?

└── YES → Null Object Pattern
Do you need exactly one shared instance of a resource?

└── YES → Singleton Pattern
Do you have complex, changeable filtering or validation rules?

└── YES → Specification Pattern

---

## Cross-Pattern Integration

In real-world systems, patterns work together. Here is an example of how
all four patterns could be used in a single Library Management System:

- **Singleton**: `LibraryConfig` — one shared configuration for the entire system
- **Observer**: `Book` notifies `WaitingUser` objects when returned
- **Null Object**: `GuestUser` replaces None for unauthenticated visitors
- **Specification**: `AvailableBookSpec.and_(InGenreSpec("science"))` filters the catalog

Each pattern solves a different problem, and together they create a clean,
maintainable, and extensible architecture.

---

## References

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns:
  Elements of Reusable Object-Oriented Software*. Addison-Wesley.
- Martin, R. C. (2003). *Agile Software Development, Principles, Patterns,
  and Practices*. Prentice Hall.
- Python Patterns Repository: https://github.com/faif/python-patterns