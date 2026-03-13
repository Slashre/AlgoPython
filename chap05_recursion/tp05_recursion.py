"""
TP 05 — La Récursion
"""


def power(x: float, n: int) -> float:
    """
    x^n en O(log n) — exponentiation rapide.
    Si n pair : (x^(n//2))^2 ; si impair : x * x^(n-1).
    TODO
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half


def gcd(a: int, b: int) -> int:
    """
    PGCD par algorithme d'Euclide récursif.
    gcd(a, b) = gcd(b, a % b) ; gcd(a, 0) = a.
    TODO
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def is_palindrome(s: str, l: int, r: int) -> bool:
    """
    True si s[l..r] est un palindrome (récursif).
    Cas de base : l >= r → True.
    TODO
    """
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return is_palindrome(s, l + 1, r - 1)


def hanoi(n: int, from_: str, to: str, via: str) -> list[tuple]:
    """
    Retourne la liste des mouvements pour résoudre les Tours de Hanoï.
    Chaque mouvement est (from_, to).
    Complexité : O(2^n) mouvements.
    TODO
    """
    if n == 1:
        return [(from_, to)]
    return hanoi(n-1, from_, via, to) + [(from_, to)] + hanoi(n-1, via, to, from_)


# compteur global pour mesurer les appels
_call_count = 0

def fib_naive(n: int) -> int:
    """Fibonacci naïf — O(2^n). Incrémente _call_count à chaque appel."""
    global _call_count
    _call_count += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n: int, memo: dict = None) -> int:
    """
    Fibonacci avec mémoïsation — O(n).
    TODO : if n in memo: return memo[n] ; memo[n] = fib_memo(n-1)+fib_memo(n-2)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def permutations(arr: list) -> list[list]:
    """
    Retourne toutes les permutations de arr (backtracking).
    Complexité : O(n! * n).
    TODO
    """
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)
    return result


def subsets(arr: list) -> list[list]:
    """
    Retourne tous les sous-ensembles de arr (2^n au total).
    TODO : récursion — sans arr[idx] puis avec arr[idx]
    """
    if not arr:
        return [[]]
    first = arr[0]
    rest = arr[1:]
    subsets_rest = subsets(rest)
    return subsets_rest + [[first] + s for s in subsets_rest]
