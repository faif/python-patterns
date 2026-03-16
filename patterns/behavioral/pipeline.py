"""
Pipeline / Functional Pipeline (Pythonic)

This implements the Pipeline pattern using a functional approach, 
where each stage is a callable transforming an iterable. The goal 
is to demonstrate a Pythonic alternative to class-based pipelines 
using generators and composition.

TL;DR:
    Build data processing flows by chaining small functions.
    In Python, pipelines are best expressed with callables + iterables
    (often generators), not heavy class hierarchies.

References:
    - https://martinfowler.com/articles/collection-pipeline/
    - https://en.wikipedia.org/wiki/Pipeline_(software)


"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")
U = TypeVar("U")

# A stage transforms an Iterable[T] into an Iterable[U].
Stage = Callable[[Iterable[T]], Iterable[U]]


def compose(*stages: Stage) -> Stage:
    """Compose stages left-to-right into a single stage."""
    def _composed(data: Iterable):
        out = data
        for stage in stages:
            out = stage(out)
        return out
    return _composed


@dataclass(frozen=True)
class Pipeline:
    """Convenience wrapper around composed stages."""
    stages: tuple[Stage, ...]

    def __call__(self, data: Iterable[T]) -> Iterable:
        fn = compose(*self.stages)
        return fn(data)

    def then(self, stage: Stage) -> "Pipeline":
        """Return a new Pipeline with an extra stage appended."""
        return Pipeline(self.stages + (stage,))



def map_stage(fn: Callable[[T], U]) -> Stage:
    """Create a mapping stage."""
    def _stage(data: Iterable[T]) -> Iterator[U]:
        for item in data:
            yield fn(item)
    return _stage


def filter_stage(pred: Callable[[T], bool]) -> Stage:
    """Create a filtering stage."""
    def _stage(data: Iterable[T]) -> Iterator[T]:
        for item in data:
            if pred(item):
                yield item
    return _stage


def take(n: int) -> Stage:
    """Take the first n items from the stream."""
    if n < 0:
        raise ValueError("n must be >= 0")

    def _stage(data: Iterable[T]) -> Iterator[T]:
        count = 0
        for item in data:
            if count >= n:
                break
            yield item
            count += 1
    return _stage


if __name__ == "__main__":
    # Example: numbers -> keep evens -> square -> take first 3
    p = Pipeline((
        filter_stage(lambda x: x % 2 == 0),
        map_stage(lambda x: x * x),
        take(3),
    ))

    print(list(p(range(100))))  # [0, 4, 16]
