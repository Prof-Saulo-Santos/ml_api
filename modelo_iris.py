import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# 1️⃣ Treinar modelo simples
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)

# 2️⃣ Salvar modelo
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
