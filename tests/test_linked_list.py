"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


class TestStack(unittest.TestCase):

    def test_Node(self):
        self.assertEqual(Node(1, None).data, 1)
        self.assertEqual(Node(None, 4).next_node, 4)

    def test_ll(self):
        ll = LinkedList()
        ll.insert_beginning({'data': 0})
        ll.insert_at_end({'something': 1})

        self.assertEqual(str(ll), "{'data': 0} -> {'something': 1} -> None")
        self.assertEqual(ll.head.data, {'data': 0})
        self.assertEqual(ll.tail.data, {'something': 1})
        self.assertEqual(ll.head.next_node.data, {'something': 1})
