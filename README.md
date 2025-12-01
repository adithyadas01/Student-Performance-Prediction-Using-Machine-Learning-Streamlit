# 🎓 Student Performance Prediction (ML + Streamlit Web App)

A complete Machine Learning project that predicts a student's final performance score (G3) using demographic, academic, and study-related features.  
The project includes:

✅ Data Cleaning & Preprocessing  
✅ Full Exploratory Data Analysis (EDA)  
✅ Feature Engineering  
✅ Random Forest Regression Model  
✅ Pipeline-based Model Deployment  
✅ Interactive Streamlit Web App  
---

## 🚀 Project Overview
This project predicts a student's **final academic performance (G3)** using important factors such as:

- Gender  
- Age  
- Mother & Father Education  
- Study Time  
- Past Class Failures  

The application uses a **preprocessing + model pipeline** so that the Streamlit app works reliably without feature mismatch errors.

---

## 🧠 Machine Learning Workflow

### **1. Dataset**
The dataset used is **student-por.csv**, which contains student academic performance data.

### **2. Preprocessing**
- OneHotEncoding for categorical column (`sex`)
- StandardScaler for numerical features
- ColumnTransformer to combine both
- Pipeline ensures consistent feature transformation during prediction

### **3. Model Used**
A **Random Forest Regressor** was trained to predict the student’s final grade.

### **4. Saved Model**
The pipeline + model is saved as:

best_student_model.pkl


This ensures the model:
- Accepts only 6 user inputs  
- Automatically handles encoding/scaling  
- Avoids feature mismatch issues  

---

## 📊 Exploratory Data Analysis (EDA)
The Streamlit app displays:

### ✔ Sex Count Plot  
Shows gender distribution of students.

### ✔ Grade Distribution  
Histogram of the final grade (G3).

### ✔ Correlation Heatmap  
Shows how numerical features correlate with G3.

---

## 🌐 Streamlit Web App Features

### **1. Dataset Viewer**
Preview the dataset in a clean table format.

### **2. EDA Visualizations**
Interactive charts using Seaborn & Matplotlib.

### **3. Student Score Predictor**
Users can input:
- Gender  
- Age  
- Parent Education  
- Study Time  
- Past Failures  

The app predicts the expected **G3 score** instantly.

---

## 🛠 Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn**
- **Pickle**

---

## 📁 Project Structure


│── app.py # Streamlit web app
│── best_student_model.pkl # Trained ML model + preprocessing pipeline
│── student-por.csv # Dataset
│── training_pipeline.ipynb # Training notebook (optional)
│── README.md # Project documentation


---

## ▶️ How to Run the Project

### **1. Install Dependencies**


pip install -r requirements.txt(optional)


### **2. Run Streamlit**


streamlit run app.py


The app will open in your browser automatically.

---

## 📌 Key Features

✔ Beautiful UI with glassmorphism  
✔ Custom background  
✔ Model trained with preprocessing pipeline  
✔ No feature mismatch errors  
✔ Easy to extend & deploy  
✔ Suitable for resume & portfolio projects  

---

## 🏁 Conclusion
This project shows how Machine Learning can be integrated with a modern web app to make real-time predictions.  
It demonstrates:

- EDA skills  
- ML model development  
- Data preprocessing  
- Pipeline management  
- Streamlit app creation  
- UI/UX design  

A great addition to your **GitHub portfolio**, **LinkedIn**, and **resume**.
