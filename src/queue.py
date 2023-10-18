class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.all = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        self.head = Node(data, self.head)
        self.all.append(data)

    def revers_enqueue(self):
        if self.tail is None:
            if self.head is None:
                return None
            while self.head is not None:
                pop = self.head
                self.head = self.head.next_node
                self.tail = Node(pop.data, self.tail)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        self.revers_enqueue()
        return self.tail.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""

        return '\n'.join(self.all) if self.tail is not None else ''
