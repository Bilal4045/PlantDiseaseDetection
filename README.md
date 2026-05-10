#  Plant Disease Recognition System

> AI-powered plant disease detection from leaf images using Deep Learning & Streamlit

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

##  Features
-  Detects **38 plant disease classes**
-  Fast real-time predictions
-  Upload any leaf image and get instant results
-  Simple and user-friendly interface
-  Powered by CNN-based deep learning model

---

##  How It Works
1. Upload a plant leaf image
2. Image is resized to 128×128 pixels
3. Preprocessed and fed to the model
4. Model predicts the disease class
5. Result is displayed instantly

---

##  Dataset Information

| Property | Details |
|---|---|
| Total Images | ~87,000 |
| Classes | 38 disease categories |
| Train Set | 70,295 images |
| Validation Set | 17,572 images |
| Test Set | 33 images |

---

##  Tech Stack
- **Python**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy**
- **PIL (Pillow)**

---

## 📂 Project Structure

```
Plant Disease Detection/
│
├── main.py                          # Streamlit app
├── plant_disease_model.tflite       # Optimized model
├── requirements.txt                 # Dependencies
└── README.md                        # Documentation
```

## Installation & Setup

**1. Clone Repository**
```bash
git clone https://github.com/Bilal4045/PlantDiseaseDetection.git
cd PlantDiseaseDetection
```

**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run Application**
```bash
streamlit run main.py
```

---

## Supported Disease Classes (38)
The model detects diseases across Apple, Tomato, Corn, Potato, Grape and more.

| Crop | Example Disease |
|---|---|
| Apple | Apple Scab, Black Rot, Cedar Apple Rust |
| Tomato | Early Blight, Late Blight, Leaf Mold |
| Potato | Early Blight, Late Blight |
| Corn | Common Rust, Northern Leaf Blight |
| Grape | Black Rot, Esca, Leaf Blight |

---

## 🔮 Future Improvements
- Improve model accuracy with transfer learning
- Add treatment recommendations for each disease
- Mobile-friendly UI
- REST API for third-party integration

---

## 👨‍💻 Author
**Bilal Mehmood** — AI / Machine Learning Developer
- GitHub: [@Bilal4045](https://github.com/Bilal4045)
