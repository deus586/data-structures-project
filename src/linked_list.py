class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, node):
        self.data = data
        self.next_node = node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]

    def to_list(self):
        """
        Вывод данных в виде списка
        """
        node = self.head
        if node is None:
            return [None]

        data_list = []
        while node:
            data_list.append(node.data)
            node = node.next_node
        return data_list

    def get_data_by_id(self, data_id):
        node = self.head
        while node:
            try:
                node.data['id']
            except TypeError:
                print('Данные не являются словарём или остутствует id')
            else:
                if node.data['id'] == data_id:
                    return node.data
            finally:
                node = node.next_node
        else:
            return 'id отсутствует'
