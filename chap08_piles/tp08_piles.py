"""TP 08 — Les Piles (LIFO)"""


class Stack:
    """Pile générique basée sur une liste Python."""

    def __init__(self):
        self._data = []

    def push(self, val) -> None:
        """Empile val — O(1). TODO"""
        self._data.append(val)

    def pop(self):
        """Dépile et retourne le sommet — O(1). Lève IndexError si vide. TODO"""
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Retourne le sommet sans dépiler — O(1). Lève IndexError si vide. TODO"""
        if not self._data:
            raise IndexError("peek into empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


def is_balanced(expr: str) -> bool:
    """
    Vérifie que les parenthèses/accolades/crochets sont équilibrés — O(n).
    TODO
    """
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in '([{':
            s.push(char)
        elif char in ')]}' :
            if s.is_empty() or s.pop() != pairs[char]:
                return False
    return s.is_empty()


def eval_rpn(tokens: list[str]) -> int:
    """
    Évalue une expression en notation polonaise inverse (RPN).
    Opérateurs supportés : +, -, *, /  (division entière tronquée vers 0).
    TODO
    """
    s = Stack()
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            b = s.pop()
            a = s.pop()
            if token == '+':
                s.push(a + b)
            elif token == '-':
                s.push(a - b)
            elif token == '*':
                s.push(a * b)
            elif token == '/':
                # Division entière tronquée vers 0
                s.push(int(a / b))
        else:
            s.push(int(token))
    return s.pop()


class MinStack:
    """Pile avec get_min() en O(1) — deux piles internes."""

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        """TODO"""
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        else:
            self._min_stack.append(min(val, self._min_stack[-1]))

    def pop(self) -> int:
        """TODO"""
        self._min_stack.pop()
        return self._stack.pop()

    def top(self) -> int:
        """TODO"""
        return self._stack[-1]

    def get_min(self) -> int:
        """Retourne le minimum actuel en O(1). TODO"""
        return self._min_stack[-1]


def sort_stack(s: Stack) -> None:
    """
    Trie la pile s (croissant en haut) avec UNE SEULE pile auxiliaire.
    Algorithme d'insertion — O(n²).
    TODO
    """
    aux = Stack()
    
    while not s.is_empty():
        temp = s.pop()
        # Déplacer les éléments de aux qui sont > temp vers s
        while not aux.is_empty() and aux.peek() > temp:
            s.push(aux.pop())
        # Insérer temp dans aux
        aux.push(temp)
    
    # Copier le résultat de aux vers s
    while not aux.is_empty():
        s.push(aux.pop())
