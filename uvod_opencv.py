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

def povecaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:
    visina = len(slika)
    sirina = len(slika[0])

    nova_slika = np.ndarray((visina * 2,sirina * 2,3),np.float32)

    pos_s = 0
    pos_v = 0
    for i in range(0,len(slika)):
        for j in range(0,len(slika[0])):
            nova_slika[pos_v:pos_v + 2,pos_s:pos_s + 2] = slika[i][j]
            pos_s += 2
        pos_v += 2
        pos_s = 0
    return nova_slika
