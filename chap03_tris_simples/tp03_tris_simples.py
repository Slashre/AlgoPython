"""
TP 03 — Les Tris Simples
Toutes les fonctions trient en place (modifient arr).
"""


def bubble_sort(arr: list) -> None:
    """
    Tri à bulles avec optimisation flag swapped.
    Complexité : O(n²) pire, O(n) meilleur (tableau déjà trié).
    TODO
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr: list) -> None:
    """
    Tri par sélection du minimum.
    Complexité : toujours O(n²), au plus n-1 échanges.
    TODO
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



def insertion_sort(arr: list) -> None:
    """
    Tri par insertion.
    Complexité : O(n²) pire, O(n) meilleur.
    TODO : pour i=1..n-1 : key=arr[i], décaler droite tant que arr[j]>key
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_generic(arr: list, key=None, reverse: bool = False) -> None:
    """
    Tri par insertion avec comparateur.
    key   : fonction d'extraction de clé (défaut : identité)
    reverse : si True, tri décroissant
    Complexité : O(n²)
    TODO
    """
    if key is None:
        key = lambda x: x
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        current_key = key(arr[i])
        j = i - 1
        while j >= 0 and ((key(arr[j]) > current_key) if not reverse else (key(arr[j]) < current_key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element
