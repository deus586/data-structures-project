"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(Node(1, None).data, 1)
        self.assertEqual(Node(None, 4).next_node, 4)

    def test_pop(self):
        stack_test = Stack()
        stack_test.push('data')
        stack_test.push('something')
        self.assertEqual(stack_test.pop(), 'something')
        self.assertEqual(stack_test.pop(), 'data')
