import streamlit as st
import pandas as pd
import numpy as np
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import base64

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------------
# CUSTOM BACKGROUND CSS
# ---------------------------------------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        img = f.read()
    encoded = base64.b64encode(img).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            backdrop-filter: blur(2px);
        }}

        .glass-card {{
            background: rgba(255, 255, 255, 0.13);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            border-radius: 12px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.18);
        }}

        h1, h2, h3, h4, h5, h6, label {{
            color: #ffffff !important;
            text-shadow: 1px 1px 2px black;
        }}

        .stButton button {{
            background-color: #ffffffaa;
            color: black;
            font-size: 18px;
            padding: 8px 20px;
            border-radius: 10px;
        }}

        .stButton button:hover {{
            background-color: #ffffff;
            box-shadow: 0px 0px 10px white;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )

add_bg_from_local(r"C:\Users\ADITHYA\OneDrive\Desktop\student prediction\carlos-muza-hpjSkU2UYSU-unsplash.jpg")

# ---------------------------------------------------------
# LOAD MODEL + DATA
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    return pickle.load(open("best_student_model.pkl", "rb"))

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\ADITHYA\OneDrive\Desktop\student prediction\student-por.csv")
    return df

model = load_model()
df = load_data()

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------
st.markdown("<h1 class='glass-card'>🎓 Student Performance Predictor</h1>", unsafe_allow_html=True)
st.write(" ")

# ---------------------------------------------------------
# TABS LAYOUT
# ---------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📊 Dataset", "📈 EDA Visualizations", "🎯 Predict Score"])

# ---------------------------------------------------------
# TAB 1: SHOW DATASET
# ---------------------------------------------------------
with tab1:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📘 Dataset Preview")
    st.dataframe(df.head())
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 2: EDA PLOTS
# ---------------------------------------------------------
with tab2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("📈 EDA Visualizations")

    plot_option = st.selectbox(
        "Choose a Plot",
        ["Sex Count", "Grade Distribution (G3)", "Correlation Heatmap"]
    )

    if plot_option == "Sex Count":
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(x="sex", data=df, ax=ax)
        st.pyplot(fig)

    elif plot_option == "Grade Distribution (G3)":
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df["G3"], kde=True, color="skyblue", ax=ax)
        st.pyplot(fig)

    elif plot_option == "Correlation Heatmap":
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 3: PREDICT SCORE (✔ FIXED)
# ---------------------------------------------------------
with tab3:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("🎯 Predict Final Math Score (G3)")

    col1, col2 = st.columns(2)

    with col1:
        sex = st.selectbox("Gender", ["F", "M"])
        age = st.slider("Age", int(df["age"].min()), int(df["age"].max()), int(df["age"].median()))
        Medu = st.selectbox("Mother Education Level (0-4)", [0,1,2,3,4])
        Fedu = st.selectbox("Father Education Level (0-4)", [0,1,2,3,4])

    with col2:
        studytime = st.selectbox("Study Time (1-4)", [1,2,3,4])
        failures = st.selectbox("Past Class Failures (0-3)", [0,1,2,3])

    # ---------------------- FIXED INPUT -------------------------
    input_data = pd.DataFrame({
        "sex": [sex],
        "age": [age],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "studytime": [studytime],
        "failures": [failures]
    })
    # ------------------------------------------------------------

    if st.button("✨ Predict Score"):
        try:
            result = model.predict(input_data)[0]
            st.success(f"🎉 Predicted Final Math Score (G3): **{result:.2f}**")
        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
