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
        print(f"Erreur lors de la connexion à mysql: {e}")
        return None

def check_user(username):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
            user = cursor.fetchone()
            if user is None:
                # Si l'utilisateur n'existe pas, l'ajouter à la table user
                cursor.execute("INSERT INTO user (username) VALUES (%s)", (username,))
                conn.commit()
            return True
        except Error as e:
            print(f"Erreur lors de la vérification de l'utilisateur: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

def log_action(username, action, table_name):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            message = f"{username} a réalisé l'action {action} sur la table {table_name}."
            cursor.execute("INSERT INTO log (message) VALUES (%s)", (message,))
            conn.commit()
        except Error as e:
            print(f"Erreur lors de l'enregistrement de l'action dans le journal: {e}")
        finally:
            cursor.close()
            conn.close()

def create_languageinfo(username, nom, Type, date):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO languageinfo (nom, date_creation, Type) VALUES (%s, %s, %s)"
            cursor.execute(query, (nom, date, Type))
            conn.commit()
            print(f"Langage '{nom}' ajouté avec succès.")
            log_action(username, "ajout", "languageinfo")
        except Error as e:
            print(f"Erreur lors de l'ajout du langage: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_languageinfo(username, languageinfo_ID):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM languageinfo WHERE ID = %s"
            cursor.execute(query, (languageinfo_ID,))
            conn.commit()
            print(f"Langage avec l'ID {languageinfo_ID} supprimé avec succès.")
            log_action(username, "suppression", "languageinfo")
        except Error as e:
            print(f"Erreur lors de la suppression du langage: {e}")
        finally:
            cursor.close()
            conn.close()

def update_languageinfo(username, languageinfo_ID, nom, date_creation, Type):
    conn = connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "UPDATE languageinfo SET nom = %s, date_creation = %s, Type = %s WHERE id = %s"
            cursor.execute(query, (nom, date_creation, Type, languageinfo_ID,))
            conn.commit()
            print(f"Langage avec l'ID {languageinfo_ID} mis à jour avec succès.")
            log_action(username, "modification", "languageinfo")
        except Error as e:
            print(f"Erreur lors de la mise à jour du langage: {e}")
        finally:
            cursor.close()
            conn.close()

# Exemple d'utilisation
username = "utilisateur1"
nom = "JavaScript"
Type = "Interprété"
date = "1995-12-04"

if check_user(username):
    create_languageinfo(username, nom, Type, date)
    # delete_languageinfo(username, 1)
    # update_languageinfo(username, 2, "Python", "1991-02-20", "Interprété")

def display_menu():
    print("Menu:")
    print("1. Ajouter un langage")
    print("2. Supprimer un langage")
    print("3. Modifier un langage")
    print("4. Quitter")

def get_user_choice():
    while True:
        choice = input("Entrez votre choix (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

def main():
    username = input("Entrez votre nom d'utilisateur: ")
    if check_user(username):
        while True:
            display_menu()
            choice = get_user_choice()

            if choice == 1:
                nom = input("Entrez le nom du langage: ")
                Type = input("Entrez le type du langage: ")
                date = input("Entrez la date de création du langage (YYYY-MM-DD): ")
                create_languageinfo(username, nom, Type, date)
            elif choice == 2:
                languageinfo_ID = input("Entrez l'ID du langage à supprimer: ")
                delete_languageinfo(username, languageinfo_ID)
            elif choice == 3:
                languageinfo_ID = input("Entrez l'ID du langage à modifier: ")
                nom = input("Entrez le nouveau nom du langage (laissez vide pour ne pas modifier): ")
                Type = input("Entrez le nouveau type du langage (laissez vide pour ne pas modifier): ")
                date = input("Entrez la nouvelle date de création du langage (laissez vide pour ne pas modifier): ")
                update_languageinfo(username, languageinfo_ID, nom, date, Type)
            elif choice == 4:
                print("Programme terminé.")
                break

if __name__ == "__main__":
    main()
