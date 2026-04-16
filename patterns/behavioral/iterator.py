from __future__ import annotations

from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class AlphabeticalOrderIterator(Iterator[T], Generic[T]):
    def __init__(self, collection: List[T]) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self) -> T:
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable[T], Generic[T]):
    def __init__(self, collection: List[T] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator[T]:
        return AlphabeticalOrderIterator(self._collection)

    def add_item(self, item: T) -> None:
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection[str]()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    print("\n".join(collection))
