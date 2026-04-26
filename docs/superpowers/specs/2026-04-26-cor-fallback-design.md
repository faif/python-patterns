---
title: Chain of Responsibility — Fallback Mechanism
date: 2026-04-26
status: approved
---

## Summary

Enhance `patterns/behavioral/chain_of_responsibility.py` by integrating a proper fallback mechanism using the Template Method pattern. Add a test suite and real-world documentation.

## Problem

The current `FallbackHandler` must be manually chained at the end of every chain. If a developer forgets it, unhandled requests are silently dropped with no feedback. `handle()` returns `None`, so callers have no way to know whether a request was processed.

## Design

### Pattern Composition: CoR + Template Method

`Handler.handle()` becomes a Template Method that owns the full flow:

```
check_range(request)
    ↓ not handled
successor exists?
    ├── yes → successor.handle(request)
    └── no  → self.handle_fallback(request)   ← fires automatically
```

Subclasses fill in `check_range`. The base class calls `handle_fallback` automatically when the chain exhausts — developers never silently drop requests again.

### Handler base class changes

- `handle()` returns `bool` (was `None`)
- New `handle_fallback(request: int) -> bool` — default is a no-op returning `False`. Subclasses can override.

### FallbackHandler — two modes

```python
FallbackHandler(mode="log")    # default — prints warning, returns False
FallbackHandler(mode="strict") # raises ValueError — for production systems
```

Constructor arg is preferred over subclasses: simpler, more Pythonic at this scale.

### Documentation

Replace abstract docstring with a **support ticket escalation** real-world analogy:
- L1 Support → L2 Support → L3 Support → fallback fires if none handle it

Add ecosystem reference: Django middleware chain.

### Tests — `tests/behavioral/test_chain_of_responsibility.py`

| Test | What it verifies |
|---|---|
| `test_handler_routes_correctly` | Each handler processes requests in its own range |
| `test_fallback_log_mode` | Unhandled request triggers log fallback, returns `False` |
| `test_fallback_strict_mode` | Unhandled request raises `ValueError` |
| `test_handle_returns_true_on_success` | `handle()` returns `True` when handled |
| `test_handle_returns_false_on_fallback` | `handle()` returns `False` when fallback fires |
| `test_chain_without_fallback_handler` | Chain exhausts gracefully via base no-op (no crash) |

## Files Changed

| File | Change |
|---|---|
| `patterns/behavioral/chain_of_responsibility.py` | Template Method integration, FallbackHandler modes, return types, docstring |
| `tests/behavioral/test_chain_of_responsibility.py` | New file — full pytest suite |

## Non-Goals

- No changes to concrete handlers (ConcreteHandler0/1/2)
- No new dependencies
- Existing doctest in `main()` remains valid
