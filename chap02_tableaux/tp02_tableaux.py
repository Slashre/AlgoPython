"""
TP 02 — Les Tableaux
Complétez les fonctions marquées TODO
"""


def rotate(arr: list, k: int) -> None:
    """
    Rotation circulaire droite de k positions, en place.
    Complexité attendue : O(n) temps, O(1) espace.
    Astuce : triple reverse.
    TODO
    """
    k = k % len(arr)
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr



def remove_duplicates(arr: list) -> int:
    """
    Supprime les doublons d'un tableau TRIÉ en place.
    Retourne la nouvelle longueur.
    Complexité attendue : O(n).
    TODO
    """
    if not arr:
        return 0
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    return write_index


def merge_arrays(a: list, b: list) -> list:
    """
    Fusionne deux tableaux triés en un seul tableau trié.
    Complexité attendue : O(n+m).
    TODO
    """
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


def binary_search(arr: list, target: int) -> int:
    """
    Recherche binaire dans un tableau trié.
    Retourne l'indice de target ou -1 si absent.
    Complexité attendue : O(log n).
    TODO
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def lower_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] >= target.
    Retourne len(arr) si target > tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(arr: list, target: int) -> int:
    """
    Premier indice i tel que arr[i] > target.
    Retourne len(arr) si target >= tous les éléments.
    Complexité attendue : O(log n).
    TODO
    """
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def transpose(m: list) -> None:
    """
    Transposée d'une matrice n×n en place.
    Complexité attendue : O(n²).
    TODO : échanger m[i][j] et m[j][i] pour j > i
    """
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m

def rotate_90(m: list) -> None:
    """
    Rotation 90° sens horaire en place.
    Étapes : transposer, puis inverser chaque ligne.
    TODO
    """
    transpose(m)
    for row in m:
        row.reverse()
    return m


def max_subarray(arr: list) -> int:
    """
    Sous-tableau contigu de somme maximale (algorithme de Kadane).
    Complexité attendue : O(n).
    TODO : cur = max(arr[i], cur + arr[i]) ; best = max(best, cur)
    """
    best = float('-inf')
    cur = 0
    for x in arr:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
