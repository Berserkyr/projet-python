import mysql.connector
from mysql.connector import Error

def connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='cours python',
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erreur lors de la conenxtion à mysql: {e}")
        return None

def create_languageinfo(nom,Type,date):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO languageinfo (nom,date_creation,Type) VALUES (%s,%s,%s)"
            cursor.execute(query, (nom,date,Type))
            conn.commit()
            print(f"user  '{nom}' added successfully.")
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur: {e}")
        finally:
            cursor.close()
            conn.close()

create_languageinfo( "js", 1, "1995-01-01")

def delete_languageinfo(languageinfo_ID):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM languageinfo WHERE ID = %s"
            cursor.execute(query, (languageinfo_ID,))
            conn.commit()
            print(f"user  ID {languageinfo_ID} deleted successfully.")
        except Error as e:
            print(f"Erreur lors de la suppresion de l'utilisateur: {e}")
        finally:
            cursor.close()
            conn.close()

def update_user(languageinfo_ID,nom,date_creation,Type):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if nom != None and date_creation != None and Type != None:
                query = "UPDATE languageinfo SET nom = %s, date_creation = %s, Type = %s WHERE id = %s"
                cursor.execute(query, (nom, date_creation,Type,languageinfo_ID,))
                conn.commit()
                print(f"User ID {languageinfo_ID} has been updated to '{nom}'.")
            elif  nom != None and date_creation != None and Type == None:
                print("kfjgkfjgkfjgkfgjkfgjf")
                query = "UPDATE languageinfo SET nom = %s, date_creation = %s WHERE id = %s"
                cursor.execute(query, (nom, date_creation, languageinfo_ID,))
                conn.commit()
                print(f"User ID {languageinfo_ID} has been updated to '{nom}'.")
            elif  nom != None and date_creation == None and Type == None:
                query = "UPDATE languageinfo SET nom = %s WHERE id = %s"
                cursor.execute(query, (nom,  languageinfo_ID,))
                conn.commit()
                print(f"User ID {languageinfo_ID} has been updated to '{nom}'.")
        except Error as e:
            print(f"Erreur lors de la mise à jour de l'utilisateur: {e}")
        finally:
            cursor.close()
            conn.close()

def all_languages():
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nom,date_creation FROM languageinfo")
            return cursor.fetchall()  # Fetch all rows from the cursor
        except Error as e:
            print(f"Erreur lors de la lecture des utilisateurs: {e}")
            return None
        finally:
            conn.close()  # Close the connection when done with it



data = all_languages()
if data is not None:
    for (nom, date_creation) in data:
        print(f"nom: {nom}, date_creation: {date_creation}")
else:
    print("Aucune donnée disponible.")
#create_langage("JS",1,"1994-01-01")
#delete_langage(1)
#update_user(2,"Python",None,None)
