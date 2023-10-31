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

    def test_exc(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 0, 'data': 0})
        ll.insert_at_end([1, 3, 2, 3])
        ll.insert_at_end({'id': 3, 'something': 1})
        ll.insert_at_end(1)

        lst = ll.to_list()
        self.assertEqual(lst[0], {'id': 0, 'data': 0})

        data = ll.get_data_by_id(3)
        self.assertEqual(data, {'id': 3, 'something': 1})

        data = ll.get_data_by_id(5)
        self.assertEqual(data, 'id отсутствует')
