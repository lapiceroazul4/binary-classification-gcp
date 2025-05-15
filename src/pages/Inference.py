import streamlit as st
import torch
import os 

from io import BytesIO
from google.cloud import storage
from PIL import Image
from torchvision import transforms
from model import CNNModel  # Asegúrate de tener el modelo definido en model.py


##### GCS

storage_client = storage.Client()

# Bucket y archivo en GCS
bucket_name = 'inferencia-test-gcp'
blob_name = 'model_checkpoint.pth'
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)


# Cargar el modelo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNNModel(num_classes=2).to(device)

# Leer el archivo desde GCS
checkpoint_data = blob.download_as_string()
checkpoint = torch.load(BytesIO(checkpoint_data), map_location=device)

checkpoint_path = os.path.join(os.path.dirname(__file__), '..', "model_checkpoint.pth")
checkpoint = torch.load(checkpoint_path, map_location=device)

model.load_state_dict(checkpoint["model_state_dict"])
model.eval()

# Transformaciones
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.CenterCrop(128),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Función de inferencia
def infer_image(image):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    return predicted.item()

# Interfaz de usuario
st.title("Inferencia: Clasificación de Imagen")
uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagen subida", use_container_width=True)

    if st.button("Clasificar"):
        prediction = infer_image(image)
        label = "Makeup" if prediction == 1 else "No Makeup"
        st.success(f"Predicción: {label}")
