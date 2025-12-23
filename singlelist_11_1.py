"""
Zadanie 11.1 z zestawu 11
Testy znajduja sie w pliku test_singlelist.py
"""

class Node:
    """Klasa reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
            return not self == other


class SingleList:
    """Klasa reprezentujaca cala liste jednokierunkowa."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    # --- ZADANIE 11.1 ----

    def remove_tail(self):
        """Usuwa ostatni element listy i zwraca go."""
        if self.is_empty():
            raise ValueError("pusta lista")

        if self.head == self.tail:
            node = self.tail
            self.tail = self.head = None
            self.length -= 1
            return node

        prev = self.head
        while prev.next != self.tail:
            prev = prev.next

        node = self.tail
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        return node

    def join(self, other):
        """Dolacza liste 'other' na koniec tej listy."""
        if other.is_empty():
            return

        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail

        self.length += other.length
        other.head = other.tail = None
        other.length = 0

    def clear(self):
        """Czysci liste."""
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
