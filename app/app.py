import streamlit as st
import pandas as pd
import joblib
from styles import get_custom_css

# Cargar modelo
modelo = joblib.load("model/modelo_zombie.pkl")

# Archivo con estilos
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Cargar datos para obtener columnas de referencia
df = pd.read_csv("data/zombie_data_binary.csv", low_memory=False)
X = df.drop(columns=["fecha_zombificacion", "grupo_supervivencia", "sobreviviente"])

columnas_entrenamiento = joblib.load("model/columnas_entrenamiento.pkl")
X_dummies = pd.get_dummies(X).reindex(columns=columnas_entrenamiento, fill_value=0)

st.title("🧟‍♀️ Clasificador de Supervivencia Zombi")

with st.form("formulario_prediccion"):
    zona_infectada = st.radio("Zona infectada", ['Zona infectada', 'Zona segura'], index=0)
    unidad_refugio = st.radio("Unidad de refugio", ['Centro de contención A', 'Centro de contención B', 'Refugio improvisado', 'Unidad móvil de emergencia'], index=0)
    genero = st.radio("Género", ['Femenino', 'Masculino'], index=0)
    tipo_contacto = st.radio("Tipo de contacto", ['Directo', 'Indirecto'], index=0)
    mordido = st.radio("¿Fue mordido?", ['No', 'Si', 'Desconocido'], index=0)
    infeccion_zombie = st.radio("¿Está infectado?", ['No', 'Si', 'Desconocido'], index=0)
    edad = st.slider("Edad", min_value=0, max_value=121, value=30)
    inmunidad_baja = st.radio("¿Tiene inmunidad baja?", ['No', 'Si', 'Desconocido'], index=0)
    movilidad_reducida = st.radio("¿Tiene movilidad reducida?", ['No', 'Si', 'Desconocido'], index=0)
    resistencia_baja = st.radio("¿Tiene resistencia baja?", ['No', 'Si', 'Desconocido'], index=0)
    unidad_critica = st.radio("¿Está en unidad crítica?", ['No', 'Si', 'Desconocido'], index=0)
    estado_mental = st.radio("Condición emocional/mental", ['Alterado', 'Estable'], index=0)
    arma_defensa = st.radio("Arma de defensa", ['Sin arma', 'Cuchillo', 'Bate', 'Pistola', 'Arma improvisada', 'Ballesta'], index=0)

    submit = st.form_submit_button("Predecir supervivencia")

    if submit:
        map_yn = {'No': 0, 'Si': 1, 'Desconocido': -1}
        map_gender = {'Femenino': 1, 'Masculino': 2}
        map_zone = {'Zona infectada': 0, 'Zona segura': 1}
        map_mental = {'Alterado': 0, 'Estable': 1}
        map_contacto = {'Indirecto': 0, 'Directo': 1}
        map_arma = {'Sin arma': 0, 'Cuchillo': 1, 'Bate': 2, 'Pistola': 3, 'Arma improvisada': 4, 'Ballesta': 5}
        map_refugio = {
            'Centro de contención A': 1,
            'Centro de contención B': 2,
            'Refugio improvisado': 3,
            'Unidad móvil de emergencia': 4
        }

        entrada = pd.DataFrame([{
            "zona_infectada": map_zone[zona_infectada],
            "unidad_refugio": map_refugio[unidad_refugio],
            "genero": map_gender[genero],
            "tipo_contacto": map_contacto[tipo_contacto],
            "mordido": map_yn[mordido],
            "infeccion_zombie": map_yn[infeccion_zombie],
            "edad": edad,
            "inmunidad_baja": map_yn[inmunidad_baja],
            "movilidad_reducida": map_yn[movilidad_reducida],
            "resistencia_baja": map_yn[resistencia_baja],
            "unidad_critica": map_yn[unidad_critica],
            "estado_mental": map_mental[estado_mental],
            "arma_defensa": map_arma[arma_defensa]
        }])

        entrada_dummies = pd.get_dummies(entrada)
        entrada_dummies = entrada_dummies.reindex(columns=X_dummies.columns, fill_value=0)

        # Predecir
        prediccion = modelo.predict(entrada_dummies)[0]
        proba_sobrevive = modelo.predict_proba(entrada_dummies)[0][1]

        # Mostrar resultado 
        if proba_sobrevive >= 0.6:
            st.markdown(
                f"""
                <div class="survive-box">
                    <h2>🟢 ¡Supervivencia probable!</h2>
                    <p>Este individuo muestra <strong>buenas probabilidades</strong> de sobrevivir al apocalipsis.</p>
                    <p><strong>Probabilidad estimada:</strong> {proba_sobrevive:.2%}</p>
                    <p><strong>Clasificación del modelo:</strong> {"Sobrevive" if prediccion == 1 else "No sobrevive"}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="nosurvive-box">
                    <h2>🔴 Supervivencia poco probable</h2>
                    <p>Este individuo tiene <strong>bajas probabilidades</strong> de sobrevivir.</p>
                    <p><strong>Probabilidad estimada:</strong> {proba_sobrevive:.2%}</p>
                    <p><strong>Clasificación del modelo:</strong> {"Sobrevive" if prediccion == 1 else "No sobrevive"}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


