import streamlit as st

from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Clasificación de Imagen", page_icon=":guardsman:", layout="wide")

# Definición de las páginas
pages = {
    "Arquitectura": "pages/arquitectura.py",
    "Inferencia": "pages/inferencia.py",
}

st.title("Contextualización")
st.write("""
    En el marco de la vision computacional, existen diversas tareas que pueden ser abordadas mediante diferentes métodos como redes neuronales convolucionales (CNNs), 
    Los vision Transformers (ViTs) y otros enfoques. En este proyecto, nos enfocamos en la tarea de **Clasificación de Imagen** utilizando una CNN.
    """)

st.title("Clasificación de Imagen")
st.write("""
    La clasificación de imagen es una tarea fundamental en la visión por computadora que consiste en asignar una etiqueta a una imagen dada. 
    Esta tarea se puede abordar mediante diferentes enfoques, siendo las redes neuronales convolucionales (CNNs) uno de los métodos más populares y efectivos.
    Las CNNs son uno de los principales métodos para la clasificación de imágenes debido a su capacidad para aprender características jerárquicas y espaciales de las imágenes,
    lo que les permite identificar patrones y objetos en diferentes escalas y posiciones.
    En este proyecto, utilizamos una CNN para clasificar imágenes de personas en dos categorías: **Makeup** y **No Makeup**.""")

st.write("""
    A continuación, se presenta una imagen que muestra la diferencia entre la detección de objetos y la clasificación de imágenes:
    - **Clasificación de Imagen**: Asigna una etiqueta a toda la imagen.
    - **Detección de Objetos**: Identifica y localiza objetos dentro de la imagen, asignando etiquetas a cada uno de ellos.
    En este proyecto, nos enfocamos en la clasificación de imagen, donde el objetivo es determinar si una persona tiene maquillaje o no.""")

# Mostrar imagen explicativa
image = Image.open("assets/classification-object-detection.png")
st.image(image, caption="Classification vs Object Detection")

st.title("Clasificación Makeup vs No Makeup")
st.write("""
    En este proyecto, nos enfocamos en la clasificación de imágenes de personas en dos categorías: **Makeup** y **No Makeup**. 
    Utilizamos una red neuronal convolucional (CNN) para aprender a distinguir entre estas dos clases a partir de un conjunto de datos de imágenes.
    La tarea consiste en entrenar el modelo con imágenes etiquetadas y luego utilizarlo para clasificar nuevas imágenes.
    
    Es importante mencionar que la imagen puede tener cualquier dimensión
    """)

st.subheader("Ejemplo de entrada")
image2 = Image.open("assets/makeup-933.png")
st.image(image2, caption="Input Example")