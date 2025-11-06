from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def get_musei(self):
        musei=[]
        cnx=ConnessioneDB.get_connection()
        cursor=cnx.cursor()
        query="SELECT * FROM museo"
        cursor.execute(query)
        for row in cursor:
            musei.append(Museo(row[0],row[1],row[2]))
        cursor.close()
        cnx.close()
        return musei


