"""TP 07 — Les Tris Linéaires"""


def counting_sort(arr: list, k: int) -> list:
    """
    Tri par dénombrement stable pour des entiers dans [0, k].
    Complexité : O(n+k) temps et espace.
    TODO :
    1. count[0..k] = 0
    2. count[arr[i]] += 1 pour tout i
    3. prefix sum : count[i] += count[i-1]
    4. de droite à gauche : output[--count[arr[i]]] = arr[i]
    """
    count = [0] * (k + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(1, k + 1):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output


def count_sort_by_digit(arr: list, exp: int) -> None:
    """
    Counting sort stable sur le chiffre de rang exp (base 10), en place.
    TODO
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Compter les occurrences de chaque chiffre
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    # Calculer les positions cumulées
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construire le résultat en parcourant de droite à gauche pour la stabilité
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copier le résultat dans arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr: list) -> None:
    """
    Radix Sort LSD pour entiers positifs — en place.
    Complexité : O(d*(n+10)) où d = nombre de chiffres du max.
    TODO : for exp=1, 10, 100... tant que max//exp > 0
    """
    if not arr:
        return
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        count_sort_by_digit(arr, exp)
        exp *= 10


def bucket_sort(arr: list) -> None:
    """
    Bucket Sort pour flottants dans [0.0, 1.0) — en place.
    Complexité : O(n) moyen.
    TODO :
    1. n buckets
    2. distribuer arr[i] dans bucket[int(n * arr[i])]
    3. trier chaque bucket (insertion sort ou sorted)
    4. concaténer
    """
    if not arr:
        return
    
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Distribuer les éléments dans les buckets
    for num in arr:
        index = int(n * num)
        # Gérer le cas limite où num == 1.0
        if index >= n:
            index = n - 1
        buckets[index].append(num)
    
    # Trier chaque bucket et remplir arr
    idx = 0
    for bucket in buckets:
        bucket.sort()  # Peut utiliser insertion sort in pour la stabilité
        for num in bucket:
            arr[idx] = num
            idx += 1
