import os

dossier = '/home/mat/Bureau/dupdup'  # Remplacez ceci par le chemin vers votre dossier
liste_fichiers = os.listdir(dossier)
liste_fichiers = [f for f in liste_fichiers if f.endswith('.json')]
liste_fichiers.sort(key=lambda x: int(os.path.splitext(x)[0]))

nouveau_numero = 1
for fichier in liste_fichiers:
    nouveau_nom = f"{nouveau_numero}.json"
    chemin_complet_ancien = os.path.join(dossier, fichier)
    chemin_complet_nouveau = os.path.join(dossier, nouveau_nom)
    os.rename(chemin_complet_ancien, chemin_complet_nouveau)
    print(f"Renommage de {fichier} en {nouveau_nom}")
    nouveau_numero += 1

print("Tous les fichiers ont été renommés avec succès.")

