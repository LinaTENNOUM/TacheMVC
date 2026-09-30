
class Tache ():
    
    def __init__(self, texte):
        self.id=None
        self.texte=texte
        self.terminee=False
    
    #__str__: méthode spéciale que Python appelle automatiquement dès que tu fais print(objet) ou str(objet).   
    def __str__(self):
        etat = "terminée" if self.terminee else "en cours"
        #apres f c juste du str affiché (jp ecrire c que jv)
        return f"Tache(id={self.id}, texte='{self.texte}', {etat})" #f c pour un str qui contient des var (a la place d'utiliser la concatenation)