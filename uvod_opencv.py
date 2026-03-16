import numpy as np

def razrezi_sliko(slika: np.ndarray, sirina_ps: int, visina_ps: int) -> list[np.ndarray]:
    arr = []
    pos_visina = 0
    pos_sirina = 0
    for i in range(0,len(slika),visina_ps):
        for j in range(0,len(slika[0]),sirina_ps):
            arr.append(slika[pos_visina:pos_visina + visina_ps,pos_sirina:pos_sirina + sirina_ps])
            pos_sirina += sirina_ps
        pos_sirina = 0
        pos_visina += visina_ps
    return arr
