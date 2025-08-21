import streamlit as st
import pickle

# -------------------------------
# Load the saved models
# -------------------------------
diabetes_model = pickle.load(open("saved_models/diabetes_model.sav", "rb"))
heart_model = pickle.load(open("saved_models/heart_model.sav", "rb"))
# parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))

# -------------------------------
# Sidebar navigation
# -------------------------------
st.sidebar.title("Disease Prediction System")
selected = st.sidebar.radio("Choose a disease to predict:",("Diabetes", "Heart Disease"))

# -------------------------------
# Diabetes Prediction
# -------------------------------
if selected == "Diabetes":
    st.title("Diabetes Prediction")
    
    # Inputs
    Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    Glucose = st.number_input("Glucose Level", min_value=0)
    BloodPressure = st.number_input("Blood Pressure value", min_value=0)
    SkinThickness = st.number_input("Skin Thickness value", min_value=0)
    Insulin = st.number_input("Insulin Level", min_value=0)
    BMI = st.number_input("BMI value", min_value=0.0, format="%.2f")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    Age = st.number_input("Age", min_value=1)

    if st.button("Predict Diabetes"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = diabetes_model.predict([user_input])
        if prediction[0] == 1:
            st.error("⚠️ The person is likely to have Diabetes.")
        else:
            st.success("✅ The person is not likely to have Diabetes.")

# -------------------------------
# Heart Disease Prediction
# -------------------------------
elif selected == "Heart Disease":
    st.title("Heart Disease Prediction")

    Age = st.number_input("Age", min_value=1)
    Sex = st.selectbox("Sex", [0, 1])  # 0 = female, 1 = male
    Cp = st.number_input("Chest Pain types (0-3)", min_value=0, max_value=3)
    Trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    Chol = st.number_input("Serum Cholestoral in mg/dl", min_value=0)
    Fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    Restecg = st.number_input("Resting Electrocardiographic results (0-2)", min_value=0, max_value=2)
    Thalach = st.number_input("Maximum Heart Rate achieved", min_value=0)
    Exang = st.selectbox("Exercise Induced Angina", [0, 1])
    Oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, format="%.1f")
    Slope = st.number_input("Slope of the peak exercise ST segment (0-2)", min_value=0, max_value=2)
    Ca = st.number_input("Major vessels colored by flourosopy (0-4)", min_value=0, max_value=4)
    Thal = st.number_input("Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)", min_value=0, max_value=2)

    if st.button("Predict Heart Disease"):
        user_input = [Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]
        prediction = heart_model.predict([user_input])
        if prediction[0] == 1:
            st.error("⚠️ The person is likely to have Heart Disease.")
        else:
            st.success("✅ The person is not likely to have Heart Disease.")

