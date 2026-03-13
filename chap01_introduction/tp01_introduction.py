"""
TP 01 — Analyse de Complexité & Benchmarks
Complétez les sections marquées TODO
"""
import time
import random


# ── Exercice 1 ────────────────────────────────────────────────────────────────

def func_a(n: int) -> int:
    """
    Complexité : O(n²)
    Justification : Deux boucles imbriquées où la boucle interne dépend de i.
    Pour chaque i de 0 à n-1, la boucle j va de i à n-1, soit n-i itérations.
    Nombre total d'opérations : sum_{i=0}^{n-1} (n-i) = n(n+1)/2, donc O(n²).
    """
    s = 0
    for i in range(n):
        for j in range(i, n):
            s += 1
    return s


def func_b(n: int) -> int:
    """
    Complexité : O(log n)
    Justification : La boucle double i à chaque itération (i *= 2) jusqu'à ce que i >= n.
    Le nombre d'itérations est le nombre de fois qu'on peut multiplier par 2 pour atteindre n,
    ce qui est approximativement log2(n), donc O(log n).
    BigO : O(log n)
    """
    c, i = 0, 1
    while i < n:
        c += 1
        i *= 2
    return c


# ── Exercice 2 ────────────────────────────────────────────────────────────────

def find_pair_naive(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n²)
    TODO: deux boucles imbriquées
    """
    Found =False
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                Found = True
                return Found
    if not Found:
        return Found


   


def find_pair_fast(arr: list, target: int) -> bool:
    """
    Retourne True si deux éléments distincts de arr somment à target.
    Complexité attendue : O(n)
    TODO: une passe avec un set — pour chaque x, chercher (target-x)
    """
    seen = set()
    for x in arr:
        if (target - x) in seen:
            return True
        seen.add(x)
    return False


# ── Exercice 3 ────────────────────────────────────────────────────────────────

def run_benchmark():
    """Mesure et affiche les temps d'exécution des deux versions."""
    print(f"{'n':>8}  {'naïf (ms)':>12}  {'rapide (ms)':>12}")
    print("-" * 40)
    for n in [1_000, 5_000, 10_000, 50_000]:
        arr = random.sample(range(n * 10), n)
        target = arr[0] + arr[n // 2]

        # TODO: mesurez find_pair_naive avec time.perf_counter()
        t_naive = 0.0   # TODO

        # TODO: mesurez find_pair_fast
        t_fast = 0.0    # TODO

        print(f"{n:>8}  {t_naive * 1000:>12.3f}  {t_fast * 1000:>12.3f}")


if __name__ == "__main__":
    run_benchmark()
