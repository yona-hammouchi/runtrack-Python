def time_to_text(minute):
    if isinstance(minute, int) and minute >= 0:
        heure = minute // 60  # Calculer les heures entières
        minu = minute % 60    # Reste des minutes après conversion en heures

        # Gestion des pluriels pour heure(s) et minute(s)
        heure_text = "heure" if heure == 1 else "heures"
        minu_text = "minute" if minu == 1 else "minutes"

        # Affichage du résultat formaté
        print(f"{heure} {heure_text} {minu} {minu_text}")
    else:
        print("Erreur : le nombre de minutes doit être un entier positif.")

# Tests
time_to_text(130)
time_to_text(45)
time_to_text(0)
def time_to_text(minute):
    if isinstance(minute, int) and minute >= 0:
        heure = minute // 60 # // pour return un nombre entier
        minu = minute - (heure * 60) # convertir les heures en minute - le nombre de minute rentré
        print(str(heure) + "h" + str(minu))
    else:
        print('Erreur')


time_to_text(130)
time_to_text(45)
time_to_text(0)
time_to_text(-20)