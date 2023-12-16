import psycopg2
import time
from sklearn import datasets

time.sleep(2)

iris = datasets.load_iris()
data = iris.data
target = iris.target

conn = psycopg2.connect(
    dbname="iris", 
    user="alex", 
    password="notsure", 
    host="db"
    # host='localhost'
)
cursor = conn.cursor()

for i in range(len(data)):
    cursor.execute(
        "INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (%s, %s, %s, %s, %s)",
        (data[i][0], data[i][1], data[i][2], data[i][3], iris.target_names[target[i]])
    )

conn.commit()

cursor.close()
conn.close()
