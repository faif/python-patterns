"""
*What is this pattern about?
This pattern is used when creating an object is costly (and they are
created frequently) but only a few are used at a time. With a Pool we
can manage those instances we have as of now by caching them. Now it
is possible to skip the costly creation of an object if one is
available in the pool.
A pool allows to 'check out' an inactive object and then to return it.
If none are available the pool creates one to provide without wait.

*What does this example do?
In this example queue.Queue is used to create the pool (wrapped in a
custom ObjectPool object to use with the with statement), and it is
populated with strings.
As we can see, the first string object put in "yam" is USED by the
with statement. But because it is released back into the pool
afterwards it is reused by the explicit call to sample_queue.get().
Same thing happens with "sam", when the ObjectPool created inside the
function is deleted (by the GC) and the object is returned.

*Where is the pattern used practically?

*References:
http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern
https://sourcemaking.com/design_patterns/object_pool

*TL;DR
Stores a set of initialized objects kept ready to use.
"""
from queue import Queue
from types import TracebackType
from typing import Union


class ObjectPool:
    def __init__(self, queue: Queue, auto_get: bool = False) -> None:
        self._queue = queue
        self.item = self._queue.get() if auto_get else None

    def __enter__(self) -> str:
        if self.item is None:
            self.item = self._queue.get()
        return self.item

    def __exit__(
        self,
        Type: Union[type[BaseException], None],
        value: Union[BaseException, None],
        traceback: Union[TracebackType, None],
    ) -> None:
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

    def __del__(self) -> None:
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None


def main():
    """
    >>> import queue

    >>> def test_object(queue):
    ...    pool = ObjectPool(queue, True)
    ...    print('Inside func: {}'.format(pool.item))

    >>> sample_queue = queue.Queue()

    >>> sample_queue.put('yam')
    >>> with ObjectPool(sample_queue) as obj:
    ...    print('Inside with: {}'.format(obj))
    Inside with: yam

    >>> print('Outside with: {}'.format(sample_queue.get()))
    Outside with: yam

    >>> sample_queue.put('sam')
    >>> test_object(sample_queue)
    Inside func: sam

    >>> print('Outside func: {}'.format(sample_queue.get()))
    Outside func: sam

    if not sample_queue.empty():
        print(sample_queue.get())
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
