import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Cargar datos
df = pd.read_csv("data/zombie_data_binary.csv", low_memory=False)

# Selección de variables predictoras y target
X = df.drop(columns=["fecha_zombificacion", "grupo_supervivencia", "sobreviviente"])
y = df["sobreviviente"]

# Generar dummies
X_dummies = pd.get_dummies(X)

# Dividir el dataset
X_train, X_test, y_train, y_test = train_test_split(X_dummies, y, test_size=0.2, random_state=42)

# Entrenar modelo
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Crear carpeta si no existe
os.makedirs("model", exist_ok=True)

# Guardar modelo
joblib.dump(clf, "model/modelo_zombie.pkl")

# Guardar columnas utilizadas para hacer reindex luego
joblib.dump(X_dummies.columns.tolist(), "model/columnas_entrenamiento.pkl")
