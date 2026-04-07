import time, random
from tp03_tris_simples import (
    bubble_sort, selection_sort, insertion_sort, insertion_sort_generic,
)
 
def mesurer(fonction, tableau):
    debut = time.perf_counter()
    fonction(tableau)
    return (time.perf_counter() - debut) * 1000   # résultat en millisecondes
 
for n in [500, 2000, 5000]:
    # Tableau aléatoire
    aleatoire = [random.randint(0, 1000) for _ in range(n)]
 
    # Faire des copies (important : les tris modifient le tableau !)
    arr1 = list(aleatoire)   # copie pour bubble_sort
    arr2 = list(aleatoire)   # copie pour selection_sort
    arr3 = list(aleatoire)   # copie pour insertion_sort
 
    t1 = mesurer(bubble_sort,    arr1)
    t2 = mesurer(selection_sort, arr2)
    t3 = mesurer(insertion_sort, arr3)
 
    print(f'n={n:5d} | bubble={t1:8.2f}ms | selection={t2:8.2f}ms | insertion={t3:8.2f}ms')


    """
    Réponses aux questions d'analyse :

    Le plus lent sur tableau aléatoire : bubble_sort en général, car il fait beaucoup d'échanges (pas seulement des décalages). insertion_sort est souvent le plus rapide des trois.
    Sur tableau déjà trié : bubble_sort et insertion_sort descendent à O(n) (quelques ms). selection_sort reste O(n²) car il cherche toujours le minimum.
    Sur tableau inversé : insertion_sort est le pire cas (chaque insertion décale tous les éléments).
    Quand n x 4 : le temps est multiplié par ~16, cohérent avec O(n²) : (4n)² = 16n².
    """
