from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

    joblib.dump(clf, 'ml-service/iris_classifier.pkl')

if __name__ == "__main__":
    train_model()
