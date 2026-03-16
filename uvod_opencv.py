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

def zmanjsaj_za_faktor_2(slika: np.ndarray) -> np.ndarray:
    visina = len(slika)
    sirina = len(slika[0])

    v_start = 0
    s_start = 0
    if(visina % 2 != 0):
        v_start += 1
    if(sirina % 2 != 0):
        s_start += 1

    nova_slika = np.ndarray((int((visina - v_start) / 2),int((sirina - s_start) / 2),3),np.float32)

    pos_v = 0
    pos_s = 0
    for i in range(v_start,len(slika),2):
        for j in range(s_start,len(slika[0]),2):
            nova_slika[pos_v,pos_s] = np.sum(np.sum(slika[i:i + 2,j:j + 2],1),0) / 4
            pos_s += 1
        pos_v += 1
        pos_s = 0

    return nova_slika

def prestej_piksle_z_barvo(slika: np.ndarray, spodnja_meja: tuple[int, int, int], zgornje_meja: tuple[int, int, int]) -> int:
    counter = 0
    spodnja_norm = np.asarray(list(spodnja_meja)) / 255
    zgornja_norm = np.asarray(list(zgornje_meja)) / 255

    for i in range(0,len(slika)):
        for j in range(0,len(slika[0])):
            if(all(slika[i][j] >= spodnja_norm)):
                if(all(slika[i][j] <= zgornja_norm)):
                    counter += 1

    return counter

