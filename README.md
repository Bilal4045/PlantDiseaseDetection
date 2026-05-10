Plant Disease Recognition System

An AI-powered web application built with Streamlit and TensorFlow that detects plant diseases from leaf images using a trained deep learning model.

 Features
 Detects 38 plant disease classes
 Fast real-time predictions
 Upload image and get instant results
 Simple and user-friendly interface
 Powered by CNN-based deep learning model
 How It Works
Upload a plant leaf image
Image is resized to 128×128 pixels
Preprocessed using TensorFlow
Model predicts disease class
Result is displayed instantly
 Dataset Information
Total Images: ~87,000
Classes: 38 plant disease categories
Split:
Train: 70,295 images
Validation: 17,572 images
Test: 33 images
 Tech Stack
Python 
TensorFlow / Keras 
Streamlit 
NumPy 
PIL (Pillow) 
📂 Project Structure
Plant Disease Detection/
│
├── plant_disease_model.keras   # Trained model
├── main.py                     # Streamlit app
├── plant2.jpg                 # Home page image
├── requirements.txt
└── README.md
 Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/PlantDiseaseDetection.git
cd PlantDiseaseDetection
2. Install Dependencies
pip install -r requirements.txt
3. Run Application
streamlit run main.py
 Usage
Home Page
Overview of system
About Page
Dataset details
Disease Recognition Page
Upload a leaf image
Click Predict
Get disease result instantly
 Model Classes (38)

The model can detect diseases across Apple, Tomato, Corn, Potato, Grapes, etc.

Example:

Apple___Apple_scab
Tomato___Late_blight
Potato___Early_blight
Corn_(maize)__Common_rust
...and more
 Important Notes
Model file plant_disease_model.keras must be in the root directory
Input image is automatically resized to 128x128
Ensure good quality leaf images for better accuracy
 Author

Bilal Mehmood
AI / Machine Learning Developer

⭐ Future Improvements
Add confidence percentage
Deploy on cloud (Streamlit Cloud / HuggingFace)
Improve model accuracy with transfer learning
Add mobile-friendly UI

If you want, I can also:
✔ make a requirements.txt
✔ optimize your model loading (right now it reloads every prediction)
✔ help you deploy it online free (Streamlit Cloud / HuggingFace Spaces)

Just tell me 👍
