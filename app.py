from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# 1️⃣ Carregar modelo
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 2️⃣ Criar app FastAPI
app = FastAPI(
    title="API de Machine Learning - Iris Classifier",
    description="API simples que prevê a classe de uma flor Iris usando um modelo de Machine Learning treinado em Python.",
    version="1.0.0"
)

# 3️⃣ Definir o formato dos dados de entrada
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 4️⃣ Rota raiz
@app.get("/")
def home():
    return {"mensagem": "API de Machine Learning ativa! Acesse /docs para testar."}

# 5️⃣ Rota de previsão
@app.post("/predict")
def predict(data: IrisData):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)
    classes = ['setosa', 'versicolor', 'virginica']
    result = classes[prediction[0]]
    return {"classe_prevista": result}
