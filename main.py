import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# TensorFlow Model Prediction

def model_prediction(image):
    model = tf.keras.models.load_model('plant_disease_model.keras')

    # Convert UploadedFile → PIL Image
    img = Image.open(image)

    # Resize image
    img = img.resize((128, 128))

    # Convert to array
    input_arr = tf.keras.preprocessing.image.img_to_array(img)

    input_arr = np.array([input_arr])

    # Prediction
    prediction = model.predict(input_arr)

    predicted_class_no = np.argmax(prediction)

    return predicted_class_no


# Sidebar

st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])


# HOME PAGE

if app_mode == "Home":
    st.header("Plant Disease Recognition System")

    image_path = "plant2.jpg"
    st.image(image_path, use_container_width=True)

    st.markdown("""
# Welcome to the Plant Disease Recognition System  

Our mission is to help identify plant diseases efficiently. Upload an image of a plant, and our system will analyze it.

---

##  How It Works

1. Upload Image in Disease Recognition page  
2. AI analyzes the image  
3. Get prediction result instantly  

---

## Why Choose Us?

- High Accuracy  
- Fast Prediction  
- Easy to Use  

---

## Get Started

Go to **Disease Recognition** page from sidebar.
""")


# =========================
# ABOUT PAGE
# =========================
elif app_mode == "About":
    st.header("About")

    st.markdown("""
## About Dataset

This dataset is recreated using offline augmentation from the original dataset.  
It contains ~87K images of crop leaves categorized into 38 classes.

## Content
1. Train (70295 images)
2. Valid (17572 images)
3. Test (33 images)
""")


# =========================
# DISEASE RECOGNITION PAGE
# =========================
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")

    test_image = st.file_uploader("Upload an image of a plant leaf", type=['jpg', 'jpeg', 'png'])

    if test_image is not None:

        if st.button("Show Image"):
            st.image(test_image, use_container_width=True)

        if st.button("Predict"):
            st.balloons()

            st.write("Our Prediction:")

            result_index = model_prediction(test_image)

            class_names = [
                'Apple___Apple_scab',
                'Apple___Black_rot',
                'Apple___Cedar_apple_rust',
                'Apple___healthy',
                'Blueberry___healthy',
                'Cherry_(including_sour)___Powdery_mildew',
                'Cherry_(including_sour)___healthy',
                'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                'Corn_(maize)___Common_rust_',
                'Corn_(maize)___Northern_Leaf_Blight',
                'Corn_(maize)___healthy',
                'Grape___Black_rot',
                'Grape___Esca_(Black_Measles)',
                'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                'Grape___healthy',
                'Orange___Haunglongbing_(Citrus_greening)',
                'Peach___Bacterial_spot',
                'Peach___healthy',
                'Pepper,_bell___Bacterial_spot',
                'Pepper,_bell___healthy',
                'Potato___Early_blight',
                'Potato___Late_blight',
                'Potato___healthy',
                'Raspberry___healthy',
                'Soybean___healthy',
                'Squash___Powdery_mildew',
                'Strawberry___Leaf_scorch',
                'Strawberry___healthy',
                'Tomato___Bacterial_spot',
                'Tomato___Early_blight',
                'Tomato___Late_blight',
                'Tomato___Leaf_Mold',
                'Tomato___Septoria_leaf_spot',
                'Tomato___Spider_mites Two-spotted_spider_mite',
                'Tomato___Target_Spot',
                'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                'Tomato___Tomato_mosaic_virus',
                'Tomato___healthy'
            ]

            st.success(f"Prediction: {class_names[result_index]}")