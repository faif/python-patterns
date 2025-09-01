from patterns.creational.pool import *

import queue

def test_object(queue):
    pool = ObjectPool(queue, True)
    print('Inside func: {}'.format(pool.item))

sample_queue = queue.Queue()

sample_queue.put('yam')
with ObjectPool(sample_queue) as obj:
    print('Inside with: {}'.format(obj))


print('Outside with: {}'.format(sample_queue.get()))

sample_queue.put('sam')
test_object(sample_queue)

print('Outside func: {}'.format(sample_queue.get()))

if not sample_queue.empty():
    print(sample_queue.get())
