
import unittest
from modele_classes import *

from gestion_projet import *

class TestGestionProjet(unittest.TestCase):

    def test_ajouter_tache(self):
        projet = Projet("Projet Test", "Description", "2024-01-01", "2024-12-31", 100000)
        tache = Tache("Tâche Test", "Description Tâche", "2024-02-01", "2024-03-01", "Responsable")
        ajouter_tache(projet, tache)
        self.assertIn(tache, projet.taches)

    def test_ajouter_risque(self):
        projet = Projet("Projet Test", "Description", "2024-01-01", "2024-12-31", 100000)
        risque = Risque("Risque Test", 0.5, "Moyen")
        ajouter_risque(projet, risque)
        self.assertIn(risque, projet.risques)

    def test_ajouter_jalon(self):
        projet = Projet("Projet Test", "Description", "2024-01-01", "2024-12-31", 100000)
        jalon = Jalon("Jalon Test", "2024-06-01")
        ajouter_jalon(projet, jalon)
        self.assertIn(jalon, projet.jalons)

    def test_ajouter_changement(self):
        projet = Projet("Projet Test", "Description", "2024-01-01", "2024-12-31", 100000)
        changement = Changement("Changement Test", "1.0", "2024-07-01")
        ajouter_changement(projet, changement)
        self.assertIn(changement, projet.changements)

    def test_ajouter_membre_equipe(self):
        projet = Projet("Projet Test", "Description", "2024-01-01", "2024-12-31", 100000)
        membre = Membre("Membre Test", "Rôle Test")
        ajouter_membre_equipe(projet, membre)
        self.assertIn(membre, projet.equipe.membres)

if __name__ == "__main__":
    unittest.main()
