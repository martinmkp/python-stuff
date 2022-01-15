import pandas as pd

def sanakoe(sanasto):
    sanat = pd.read_excel(sanasto, header = 0)
    sanat_vieras = list(sanat.iloc[:, 0])
    sanat_suomi = list(sanat.iloc[:, 1])

    pisteet = 0
    maksimi_pisteet = sanat.shape[0]

    for i in range(maksimi_pisteet):
        sana = input(f"Sana {i+1}/{maksimi_pisteet}: {sanat_vieras[i]}: ")
        if sana == sanat_suomi[i]:
            print("Oikein!")
            pisteet +=1
        else:
            print(f"Väärin. Oikea vastaus: {sanat_suomi[i]}")
    print(f"Tulos: {pisteet}/{maksimi_pisteet}")
