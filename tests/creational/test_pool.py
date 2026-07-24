import queue

from patterns.creational.pool import ObjectPool


class TestPool:
    def setup_method(self):
        self.sample_queue = queue.Queue()
        self.sample_queue.put("first")
        self.sample_queue.put("second")

    def test_items_recoil(self):
        with ObjectPool(self.sample_queue, True) as pool:
            assert pool == "first"
        assert self.sample_queue.get() == "second"
        assert not self.sample_queue.empty()
        assert self.sample_queue.get() == "first"
        assert self.sample_queue.empty()

    def test_frozen_pool(self):
        with ObjectPool(self.sample_queue) as pool:
            assert pool == "first"
            assert pool == "first"
        assert self.sample_queue.get() == "second"
        assert not self.sample_queue.empty()
        assert self.sample_queue.get() == "first"
        assert self.sample_queue.empty()


class TestNaitivePool:
    """def test_object(queue):
    queue_object = QueueObject(queue, True)
    print('Inside func: {}'.format(queue_object.object))"""

    def test_pool_behavior_with_single_object_inside(self):
        sample_queue = queue.Queue()
        sample_queue.put("yam")
        with ObjectPool(sample_queue) as obj:
            # print('Inside with: {}'.format(obj))
            assert obj == "yam"
        assert not sample_queue.empty()
        assert sample_queue.get() == "yam"
        assert sample_queue.empty()

    # sample_queue.put('sam')
    # test_object(sample_queue)
    # print('Outside func: {}'.format(sample_queue.get()))

    # if not sample_queue.empty():
