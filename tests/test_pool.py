#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
try:
    import queue
except ImportError:  # python 2.x compatibility
    import Queue as queue
from creational.pool import QueueObject


class TestPool(unittest.TestCase):

    def setUp(self):

        def test_object(queue):
            queue_object = QueueObject(queue, True)
            print('Inside func: {}'.format(queue_object.object))

    def test_pool_behavior(self):
        sample_queue = queue.Queue()
        sample_queue.put('yam')
        self.assertTrue(sample_queue.get() == 'yam')
        # with QueueObject(sample_queue) as obj:
        #     print('Inside with: {}'.format(obj))

#     sample_queue.put('sam')
#     test_object(sample_queue)
#     print('Outside func: {}'.format(sample_queue.get()))

#     if not sample_queue.empty():
#         print(sample_queue.get())


# if __name__ == '__main__':
#     main()

### OUTPUT ###
# Inside with: yam
# Outside with: yam
# Inside func: sam
# Outside func: sam

