import streamlit as st
import os

from PIL import Image


# Mostrar imagen explicativa
image_path = os.path.join(os.getcwd(), "src", "assets", "Arquitectura.png")
image = Image.open(image_path)
st.image(image, caption="Arquitectura de la Red Neuronal")

st.title("Arquitectura de la Red Neuronal")
st.write("""
    La arquitectura utilizada es una **CNN** (Convolutional Neural Network) que consta de 3 capas convolucionales seguidas de capas de pooling. 
    Al final, tenemos 2 capas completamente conectadas para la clasificación.

    ### Capas:
    1. **Conv1**: Convolución 3x3, 32 filtros
    2. **Conv2**: Convolución 3x3, 64 filtros
    3. **Conv3**: Convolución 3x3, 128 filtros
    4. **Pooling**: Max Pooling 2x2 para reducir las dimensiones
    5. **FC1**: Capa completamente conectada con 512 neuronas
    6. **FC2**: Capa de salida con 2 neuronas (para las clases: Makeup y No Makeup)
""")
