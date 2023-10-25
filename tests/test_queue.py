"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


class TestStack(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(Node(1, None).data, 1)
        self.assertEqual(Node(None, 4).next_node, 4)

    def test_pop(self):
        queue_test = Queue()
        queue_test.enqueue('data')
        queue_test.enqueue('something')

        self.assertEqual(queue_test.dequeue(), 'data')
        self.assertEqual(queue_test.tail.data, 'something')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), None)
