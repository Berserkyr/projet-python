import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='cours python',
    )
except mysql.connector.Error as e:
    print("Erreur lors de la conenxtion à mysql", e)
finally:
    pass
