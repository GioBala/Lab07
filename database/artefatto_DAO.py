from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_epoca(self):
        epoca=[]
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor()
        query="SELECT DISTINCT epoca FROM `artefatto` ORDER BY epoca"
        cursor.execute(query)
        for row in cursor:
            epoca.append(row[0])
        cursor.close()
        cnx.close()
        return epoca

    def get_artefatti(self, nome,epoca):
        artefatti=[]
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor()
        query= "SELECT * FROM artefatto JOIN museo ON artefatto.id_museo = museo.id WHERE artefatto.epoca = COALESCE(%s, artefatto.epoca) AND museo.nome = COALESCE(%s, museo.nome);"
        cursor.execute(query,(epoca,nome))
        for row in cursor:
            artefatti.append(Artefatto(row[0],row[1],row[2],row[3],row[4]))
        cursor.close()
        cnx.close()
        return artefatti