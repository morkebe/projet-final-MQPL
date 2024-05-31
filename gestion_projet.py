from modele_classes import Projet, Tache, Risque, Jalon, Changement, Membre
def ajouter_tache(projet, tache):
    projet.ajouter_tache(tache)

def ajouter_risque(projet, risque):
    projet.ajouter_risque(risque)

def ajouter_jalon(projet, jalon):
    projet.ajouter_jalon(jalon)

def ajouter_changement(projet, changement):
    projet.ajouter_changement(changement)

def ajouter_membre_equipe(projet, membre):
    projet.ajouter_membre_equipe(membre)

def calculer_chemin_critique(projet):
    # Implémentation simplifiée pour calculer le chemin critique
    pass

def generer_rapport(projet):
    # Générer un rapport détaillé du projet
    pass
