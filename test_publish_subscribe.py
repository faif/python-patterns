#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import version_info
from publish_subscribe import Provider, Publisher, Subscriber

if version_info < (2, 7):
    import unittest2 as unittest

else:
    import unittest

class TestProvider(unittest.TestCase):
    """
    Integration tests ~ provider class with as little mocking as possible.
    """
    def test_subscriber_shall_be_attachable(cls):
        pro = Provider()
        cls.assertEqual(len(pro.subscribers), 0)
        sub = Subscriber('sub name', pro)
        sub.subscribe('sub msg')
        cls.assertEqual(len(pro.subscribers), 1)

#    def test_subscriber_shall_be_detachable(cls):
#        pro = Provider()
#        sub = Subscriber('sub name', pro)
#        sub.subscribe('sub msg')
#        cls.assertEqual(len(pro.subscribers), 1)
#        pro.unsubscribe('sub msg', sub)
#        cls.assertEqual(len(pro.subscribers), 0)

    def test_publisher_shall_append_message(cls):
        ''' msg_queue ~ Provider.notify(msg) ~ Publisher.publish(msg) '''
        expected_msg = 'expected msg'
        pro = Provider()
        pub = Publisher(pro)
        sub = Subscriber('sub name', pro)
        cls.assertEqual(len(pro.msg_queue), 0)
        pub.publish(expected_msg)
        cls.assertEqual(len(pro.msg_queue), 1)
        cls.assertEqual(pro.msg_queue[0], expected_msg)

if __name__ == "__main__":
    unittest.main()

