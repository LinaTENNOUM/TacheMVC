import sys
from PyQt5.QtWidgets import QApplication # pour cette ligne app = QApplication(sys.argv)
import os
from view import TacheView
from model import TacheModel
from controller import TacheController

if __name__ == "__main__":   
    
    app = QApplication(sys.argv)  ## ← crée l'application
    """elle initialise l'environnement nécessaire pour créer et gérer ta fenêtre, les boutons, les champs input, les événements clavier/souris, etc. 
        Une seule instance de QApplication doit exister par programme.
        sys.argv = les arguments passés au script depuis la ligne de commande (souvent vide, mais PyQt5 en a besoin techniquement)."""
         
    view = TacheView()
    if os.path.exists("taches.db"):
            os.remove("taches.db")
    model = TacheModel()
    controller = TacheController(view, model)
    
    view.show() #Rend la fenêtre visible à l'écran.
    sys.exit(app.exec_())  # ← lance la boucle de l'application