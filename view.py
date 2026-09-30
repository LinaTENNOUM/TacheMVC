import sys
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget)

class TacheView(QMainWindow):
    
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Ma To-Do List")
        #(x,y,l3ord,tol)
        self.setGeometry(100, 100, 400, 500)

        # 1. Créer les widgets
        self.input_tache = QLineEdit() #champ de saisie
        self.input_tache.setPlaceholderText("Nouvelle tâche...")
        self.btn_ajouter = QPushButton("Ajouter") #bouton ajouter
        self.btn_supprimer = QPushButton ("supprimer") #bouton supprimer        
        self.liste_taches = QListWidget() #une liste verticale, où on affichera chaque tâche comme une ligne
        
        # 2. Organiser avec des layouts, layout = (arrangement) gestionnaire de positionnement automatique des widgets (pas besoin de coordonnées)
        layout_principal = QVBoxLayout() #QV empile les widgets verticalement (V = Vertical)
        layout_ajout = QHBoxLayout() #QH aligne les widgets horizontalement (H = Horizontal)
        
        # 3. Ajouter les widgets aux layouts
        layout_ajout.addWidget(self.input_tache) # ajoute le champ de saisie à l'horizontal
        layout_ajout.addWidget(self.btn_ajouter) # ajoute le bouton à l'horizontal
        layout_ajout.addWidget(self.btn_supprimer) 
        
        layout_principal.addLayout(layout_ajout) # ajouter le layout horizontal au layout vertical (le layout vertical contient donc le layout horizontal)
        layout_principal.addWidget(self.liste_taches) # ajoute la liste des tâches au layout vertical (en dessous du layout horizontal)
        
        # 4. Définir le layout principal comme layout du conteneur
        """Pourquoi un QWidget conteneur intermédiaire ?
        C'est une règle spécifique à QMainWindow : 
        elle ne peut pas recevoir un layout directement, elle a besoin d'un widget "central" qui, lui, contient le layout"""
        conteneur = QWidget() # une boîte vide
        conteneur.setLayout(layout_principal) #  on met notre layout dedans (le conteneur est un widget vide qui contient tous les autres widgets)
        self.setCentralWidget(conteneur) # on dit à la fenêtre "voici ton contenu central"
        
    
    
#test view
"""   
if __name__ == "__main__":
    
    app = QApplication(sys.argv)    
    #Crée ton objet fenêtre — mais à ce stade, rien ne s'affiche encore à l'écran.
    fenetre = TacheView()
    #Rend la fenêtre visible à l'écran.
    fenetre.show()
    sys.exit(app.exec_())
    """