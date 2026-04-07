"""
TP 06 — Diviser pour Régner
"""
import random


def merge(left: list, right: list) -> list:
    """
    Fusionne deux listes triées en une seule triée.
    Stable : les éléments égaux de left précèdent ceux de right.
    Complexité : O(n+m). TODO
    """
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Ajouter les éléments restants
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(arr: list) -> list:
    """
    Tri fusion — retourne un nouveau tableau trié.
    Complexité : O(n log n) temps, O(n) espace. TODO
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def partition_fixed(arr: list, lo: int, hi: int) -> int:
    """
    Partition avec arr[hi] comme pivot.
    Retourne la position finale du pivot. TODO
    """
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


def partition_random(arr: list, lo: int, hi: int) -> int:
    """
    Choisit un pivot aléatoire dans [lo, hi], l'échange avec arr[hi],
    puis appelle partition_fixed. TODO
    """
    random_index = random.randint(lo, hi)
    arr[random_index], arr[hi] = arr[hi], arr[random_index]
    return partition_fixed(arr, lo, hi)


def quick_sort(arr: list, lo: int = 0, hi: int = None) -> None:
    """
    Tri rapide en place avec pivot aléatoire.
    Complexité : O(n log n) espérance, O(n²) pire cas. TODO
    """
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        pi = partition_random(arr, lo, hi)
        quick_sort(arr, lo, pi - 1)
        quick_sort(arr, pi + 1, hi)


def quick_select(arr: list, lo: int, hi: int, k: int) -> int:
    """
    k-ième plus petit élément (0-indexé) dans arr[lo..hi].
    Complexité : O(n) espérance. TODO
    """
    if lo == hi:
        return arr[lo]
    
    pi = partition_random(arr, lo, hi)
    
    if k == pi:
        return arr[pi]
    elif k < pi:
        return quick_select(arr, lo, pi - 1, k)
    else:
        return quick_select(arr, pi + 1, hi, k)


def count_inversions_merge(left: list, right: list) -> tuple[list, int]:
    """
    Fusionne deux listes triées et compte les inversions entre elles.
    Une inversion = paire (i,j) avec i<j et arr[i]>arr[j], avec i dans left et j dans right.
    Complexité : O(n+m).
    """
    merged = []
    inversions = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # Tous les éléments restants dans left sont des inversions avec right[j]
            inversions += len(left) - i
            j += 1
    # Ajouter les éléments restants
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions


def count_inversions(arr: list) -> tuple[list, int]:
    """
    Retourne (arr_trié, nb_inversions).
    Une inversion = paire (i,j) avec i<j et arr[i]>arr[j].
    Complexité : O(n log n). TODO : modifier merge pour compter
    """
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_merge = count_inversions_merge(left, right)
    return merged, inv_left + inv_right + inv_merge
