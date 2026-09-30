import sqlite3
from tache import Tache
import os

""" quand on utilise self.attribut donc on peut l'utiliser dans toutes les méthodes de la classe, c'est un attribut de l'objet. (global)
accessible depuis toutes les méthodes de la classe. via self.attribut dans toutes les méthodes de la classe."""


class TacheModel:
    
    def __init__(self, db_path = "taches.db"):
        # Create a connection to the SQLite database named "taches.db"
        self.cnx = sqlite3.connect(db_path)
        # Le curseur — l'objet qui exécute réellement les requêtes, curseur comme le stylo qui va écrire/lire dans la bd
        self.curs = self.cnx.cursor()
        self.create_table()

    def create_table(self):
        self.curs.execute("""
            CREATE TABLE IF NOT EXISTS taches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                texte TEXT NOT NULL,
                terminee INTEGER DEFAULT 0
            )
        """)
        self.cnx.commit()

    def ajouter(self, texte):
        self.curs.execute("INSERT INTO taches (texte, terminee) VALUES (?, 0)", (texte,))
        self.cnx.commit()
        
        #le moment ou on cree une tache dans la bd on cree aussi son obj 
        tache = Tache(texte) #initialisation d'un obj tache
        tache.id = self.curs.lastrowid #psq sqlite gère le id auto (id++)
        return tache
        

    def supprimer(self, id):
        self.curs.execute("""
        DELETE FROM taches WHERE id = ?
        """, (id,))
        self.cnx.commit()

    def marquer_terminer(self, id):
        self.curs.execute("""
                UPDATE taches SET terminee=1 WHERE id=?""", (id,))
        self.cnx.commit()    

    def get_toutes(self):
        self.curs.execute("""
        SELECT * FROM taches
        """)
        lignes = self.curs.fetchall() 
        
        #pour acceder a un attribut d'une ligne dans la bd ligne[1] ms attribut d'un objet obj.nomAttribut   
        taches = []
        for ligne in lignes:
            t= Tache(ligne[1]) #creation d'un objet tache
            t.id=ligne[0]
            t.terminee=bool(ligne[2])
            taches.append(t)
            
        return taches
    
 


#test de model
"""
if __name__ == "__main__":
    
    if os.path.exists("test.db"):
        os.remove("test.db")
    model = TacheModel("test.db")
    tache=(model.ajouter("Réviser Python"))
    model.supprimer(tache.id)
    tache=(model.ajouter("cooking"))
    model.marquer_terminer(tache.id)
    
    for i in range(1, 6):
        tache=(model.ajouter(f"tache{i}"))
        if tache.id%2==0:
            model.marquer_terminer(tache.id)  
    
    for t in model.get_toutes():
        print(t)
    #tache=model.ajouter("Faire les courses")
    #print(tache)
 
 """



#rq
"""
    curseur.execute("SELECT * FROM taches") #a ce stade, rien n'est encore récupéré en Python, la requête a juste été lancée.
    
    resultats = curseur.fetchall() #fetchall() récupère toutes les lignes trouvées, sous forme de liste de tuples : [(1, 'Acheter du pain', 0),...]
    print(resultats)
    
    resultats = curseur.execute("SELECT * FROM taches").fetchall() #on peut aussi faire ça en une seule ligne, mais c'est moins lisible.
    #Pour INSERT/UPDATE/DELETE — il faut valider avec commit()
    curseur.execute("INSERT INTO taches (texte, terminee) VALUES ('Acheter du pain', 0)")
    cnx.commit()
    //
    """