import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Configure Streamlit page
st.set_page_config(page_title='Prediction of Disease Outbreaks', 
                   layout='wide', 
                   page_icon="🧪💉🧫")

# Load models
diabetes_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\parkinsons_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreak System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# =================== Diabetes Prediction ===================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', "0")
    with col2:
        Glucose = st.text_input('Glucose Level', "0")
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value', "0")
    with col1:
        Skinthickness = st.text_input('Skin Thickness Value', "0")
    with col2:
        Insulin = st.text_input('Insulin Level', "0")
    with col3:
        BMI = st.text_input('BMI Value', "0")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', "0")
    with col2:
        Age = st.text_input('Age of the person', "0")

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(Bloodpressure), float(Skinthickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])
            
            diab_diagnosis = 'The Person is Diabetic' if diab_prediction[0] == 1 else 'The Person is Not Diabetic'
        
        except ValueError:
            diab_diagnosis = "Error: Please enter valid numerical values."

        st.success(diab_diagnosis)

# =================== Heart Disease Prediction ===================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', "0")
    with col2:
        sex = st.text_input('Gender (1 = Male, 0 = Female)', "0")
    with col3:
        cp = st.text_input('Chest Pain Type (CP)', "0")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', "0")
    with col2:
        chol = st.text_input('Cholesterol Level', "0")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (1 = True, 0 = False)', "0")
    with col1:
        restecg = st.text_input('Resting ECG Results', "0")
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved', "0")
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)', "0")
    with col1:
        oldpeak = st.text_input('ST Depression Induced', "0")
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment', "0")
    with col3:
        ca = st.text_input('Number of Major Vessels', "0")
    with col1:
        thal = st.text_input('Thalassemia (0-3)', "0")

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), 
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), 
                          float(ca), float(thal)]
            
            heart_prediction = heart_model.predict([user_input])
            
            heart_diagnosis = 'The Person has Heart Disease' if heart_prediction[0] == 1 else 'The Person does NOT have Heart Disease'
        
        except ValueError:
            heart_diagnosis = "Error: Please enter valid numerical values."

        st.success(heart_diagnosis)

# =================== Parkinson's Prediction ===================
if selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction Using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        MDVP_fo = st.text_input('MDVP:Fo(Hz)', "0")
    with col2:
        MDVP_fhi = st.text_input('MDVP:Fhi(Hz)', "0")
    with col3:
        MDVP_flo = st.text_input('MDVP:Flo(Hz)', "0")
    with col1:
        MDVP_jit = st.text_input('MDVP:Jitter(%)', "0")
    with col2:
        MDVP_jitter = st.text_input('MDVP:Jitter(Abs)', "0")
    with col3:
        MDVP_rap = st.text_input('MDVP:RAP', "0")
    with col1:
        MDVP_ppq = st.text_input('MDVP:PPQ', "0")
    with col2:
        Jitter_ddp = st.text_input('Jitter:DDP', "0")
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', "0")
    with col1:
        MDVP_Shimmerdb = st.text_input('MDVP:Shimmer(dB)', "0")
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3', "0")
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5', "0")
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ', "0")
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA', "0")
    with col3:
        NHR = st.text_input('NHR', "0")
    with col1:
        HNR = st.text_input('HNR', "0")
    with col2:
        RPDE = st.text_input('RPDE', "0")
    with col3:
        DFA = st.text_input('DFA', "0")

    parkinsons_diagnosis = ''

    if st.button('Parkinson’s Test Result'):
        try:
            user_input = [float(MDVP_fo), float(MDVP_fhi), float(MDVP_flo), float(MDVP_jit), float(MDVP_jitter),
                          float(MDVP_rap), float(MDVP_ppq), float(Jitter_ddp), float(MDVP_Shimmer),
                          float(MDVP_Shimmerdb), float(Shimmer_APQ3), float(Shimmer_APQ5), float(MDVP_APQ),
                          float(Shimmer_DDA), float(NHR), float(HNR), float(RPDE), float(DFA)]
            
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            parkinsons_diagnosis = 'The Person has Parkinson’s Disease' if parkinsons_prediction[0] == 1 else 'The Person does NOT have Parkinson’s Disease'
        
        except ValueError:
            parkinsons_diagnosis = "Error: Please enter valid numerical values."

        st.success(parkinsons_diagnosis)
