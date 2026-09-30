
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
class TacheController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.connecter_signaux()
        self.rafraichir_liste()   # affiche les tâches déjà en BDD au démarrage
    
    def connecter_signaux(self):
        
        self.view.btn_ajouter.clicked.connect(self.on_ajouter_clicked)
        """Décomposons : "le bouton btn_ajouter, qui appartient à self.view, quand il émet le signal clicked, doit appeler la méthode self.on_ajouter_clicked".
        Remarque : on écrit self.on_ajouter_clicked sans les parenthèses.
        avec les parenthèses (self.on_ajouter_clicked()), tu exécuterais la méthode immédiatement, une seule fois, à la création du Controller. 
        Sans les parenthèses, tu donnes juste la référence à la méthode, pour que PyQt5 l'appelle plus tard, à chaque clic réel."""
           
    def on_ajouter_clicked (self):
        texte = self.view.input_tache.text() #recuperer le texte
        
        if texte.strip() == "":   # évite d'ajouter une tâche vide. strip() enlève les espaces au début/à la fin.
            return
        
        self.model.ajouter(texte) #ajouter la tache dans la bd
        self.view.input_tache.clear()   # vider le champ de saisie après ajout
        self.rafraichir_liste()

    def on_supprimer_clicked (self):
        item = self.view.liste_taches.currentItem()
        if item is None:
           return # rien n'est sélectionné, on ne fait rien
        id_tache = item.data(Qt.UserRole)   # ← récupère l'id caché
        self.model.supprimer(id_tache)
        self.rafraichir_liste()
        
    def tache_termine (self):
        id = self.view.liste_taches.currentItem().id
        #if: 
        self.model.marquer_terminer(id)
        self.rafraichir_liste()
        
    def rafraichir_liste (self):
        self.view.liste_taches.clear()   # vider l'affichage actuel
        taches = self.model.get_toutes()
        for tache in taches:
            etat = "✓ " if tache.terminee else ""
            item = QListWidgetItem(f"{etat}{tache.texte}") #crée un élément de la liste
            item.setData(Qt.UserRole, tache.id)   # ← on "attache" l'id à cet item
            self.view.liste_taches.addItem(item)
            
  
  

