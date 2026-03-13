"""
TP 04 — Listes Doublement Chaînées
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Liste doublement chaînée avec head, tail et taille."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_front(self, val) -> None:
        node = Node(val)
        node.next = self.head

        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node
        self._size += 1


    def push_back(self, val) -> None:
        node = Node(val)
        node.prev = self.tail

        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        self._size += 1


    def pop_front(self):
        if not self.head:
            raise IndexError("list empty")

        node = self.head
        self.head = node.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self._size -= 1
        return node.data

    def pop_back(self):
        if not self.tail:
            raise IndexError("list empty")

        node = self.tail
        self.tail = node.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self._size -= 1
        return node.data


    def insert_after(self, node: Node, val) -> Node:
        new_node = Node(val)

        new_node.prev = node
        new_node.next = node.next

        if node.next:
            node.next.prev = new_node
        else:
            self.tail = new_node

        node.next = new_node
        self._size += 1

        return new_node


    def remove(self, node: Node) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self._size -= 1


    def find(self, val) -> Node | None:
        current = self.head

        while current:
            if current.data == val:
                return current
            current = current.next

        return None


    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def to_list(self) -> list:
        return list(self)


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def reverse_iterative(lst: DoublyLinkedList) -> None:
    """
    Inverse la liste en place — O(n) temps, O(1) espace.
    Pour chaque nœud, échange prev et next, puis swap head et tail.
    TODO
    """
    current = lst.head

    while current:
        current.prev, current.next = current.next, current.prev
        current = current.prev

    lst.head, lst.tail = lst.tail, lst.head


# ── Exercice 3 — Algorithme de Floyd ─────────────────────────────────────────
 
class SNode:
    """Nœud de liste simplement chaînée pour l'exercice Floyd."""
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head: SNode | None) -> bool:
    """
    Détecte un cycle dans une liste simplement chaînée.
    Algorithme du lièvre et de la tortue — O(n) temps, O(1) espace.
    TODO : slow avance de 1, fast avance de 2
    """
    if not head:
        return False
    
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# ── Exercice 4 ────────────────────────────────────────────────────────────────

def kth_from_end(head: SNode | None, k: int) -> int:
    if not head:
        raise ValueError("k is larger than the length of the list")

    slow = fast = head

    for _ in range(k):
        if not fast:
            raise ValueError("k is larger than the length of the list")
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.val
