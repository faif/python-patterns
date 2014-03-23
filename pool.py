#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""http://stackoverflow.com/questions/1514120/python-implementation-of-the-object-pool-design-pattern"""


class QueueObject():

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.object = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.object is None:
            self.object = self._queue.get()
        return self.object

    def __exit__(self, Type, value, traceback):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None

    def __del__(self):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None


def main():
    try:
        import queue
    except ImportError:  # python 2.x compatibility
        import Queue as queue

    def test_object(queue):
        queue_object = QueueObject(queue, True)
        print('Inside func: {}'.format(queue_object.object))

    sample_queue = queue.Queue()

    sample_queue.put('yam')
    with QueueObject(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)
    print('Outside func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam
