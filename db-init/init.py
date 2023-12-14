import psycopg2
from sklearn import datasets

# Charger le dataset Iris
iris = datasets.load_iris()
data = iris.data
target = iris.target

# Établir une connexion à la base de données
conn = psycopg2.connect(
    dbname="iris", 
    user="alex", 
    password="notsure", 
    host="127.0.0.1"
)
cursor = conn.cursor()

# Insertion des données
for i in range(len(data)):
    cursor.execute(
        "INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (%s, %s, %s, %s, %s)",
        (data[i][0], data[i][1], data[i][2], data[i][3], iris.target_names[target[i]])
    )

# Valider la transaction
conn.commit()

# Fermer la connexion
cursor.close()
conn.close()
