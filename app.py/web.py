import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks', 
                   layout='wide', 
                   page_icon="💉🧪🧫")

# Load trained ML models
diabetes_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\vidhy\OneDrive\Documents\disease outbreak\training_model\parkinsons_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreak System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0
    )

# ================= Diabetes Prediction =================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value="0")
    with col2:
        Glucose = st.text_input('Glucose Level', value="0")
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value', value="0")
    with col1:
        Skinthickness = st.text_input('Skin Thickness Value', value="0")
    with col2:
        Insulin = st.text_input('Insulin Level', value="0")
    with col3:
        BMI = st.text_input('BMI Value', value="0")
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value', value="0")
    with col2:
        Age = st.text_input('Age of the person', value="0")

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            user_input = [float(Pregnancies), float(Glucose), float(Bloodpressure), float(Skinthickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            diab_prediction = diabetes_model.predict([user_input])
            
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is Not Diabetic'
        
        except ValueError:
            diab_diagnosis = "Error: Please enter valid numerical values."

        st.success(diab_diagnosis)

# ================= Heart Disease Prediction =================
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of the person', value="0")
    with col2:
        sex = st.text_input('Gender (1 = Male, 0 = Female)', value="0")
    with col3:
        cp = st.text_input('Chest Pain Type (CP)', value="0")
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (Trestbps)', value="0")
    with col2:
        chol = st.text_input('Cholesterol Level', value="0")
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (1 = True, 0 = False)', value="0")
    with col1:
        restecg = st.text_input('Rest ECG Result', value="0")
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved (Thalach)', value="0")
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)', value="0")
    with col1:
        oldpeak = st.text_input('ST Depression (Oldpeak)', value="0")
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment', value="0")
    with col3:
        ca = st.text_input('Number of Major Vessels (Ca)', value="0")
    with col1:
        thal = st.text_input('Thalassemia Type (Thal)', value="0")

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                          float(ca), float(thal)]
            
            heart_prediction = heart_model.predict([user_input])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person has Heart Disease'
            else:
                heart_diagnosis = 'The Person does not have Heart Disease'
        
        except ValueError:
            heart_diagnosis = "Error: Please enter valid numerical values."

        st.success(heart_diagnosis)

# ================= Parkinson’s Prediction =================
elif selected == 'Parkinsons Prediction':
    st.title('Parkinson’s Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_fo = st.text_input('MDVP:Fo(Hz) Value', value="0")
    with col2:
        MDVP_fhi = st.text_input('MDVP:Fhi(Hz) Value', value="0")
    with col3:
        MDVP_flo = st.text_input('MDVP:Flo(Hz) Value', value="0")
    with col1:
        MDVP_jit = st.text_input('MDVP:Jitter(%) Value', value="0")
    with col2:
        MDVP_jitter = st.text_input('MDVP:Jitter(Abs) Value', value="0")
    with col3:
        MDVP_rap = st.text_input('MDVP:RAP Value', value="0")
    with col1:
        MDVP_ppq = st.text_input('MDVP:PPQ Value', value="0")
    with col2:
        Jitter_ddp = st.text_input('Jitter:DDP Value', value="0")
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer Value', value="0")
    with col1:
        MDVP_Shimmerdb = st.text_input('MDVP:Shimmer(dB) Value', value="0")
    with col2:
        NHR = st.text_input('NHR Value', value="0")
    with col3:
        HNR = st.text_input('HNR Value', value="0")
    with col1:
        RPDE = st.text_input('RPDE Value', value="0")
    with col2:
        DFA = st.text_input('DFA Value', value="0")
    with col3:
        spread1 = st.text_input('Spread1 Value', value="0")
    with col1:
        spread2 = st.text_input('Spread2 Value', value="0")
    with col2:
        D2 = st.text_input('D2 Value', value="0")
    with col3:
        PPE = st.text_input('PPE Value', value="0")

    parkinsons_diagnosis = ''

    if st.button('Parkinson’s Test Result'):
        try:
            user_input = [float(MDVP_fo), float(MDVP_fhi), float(MDVP_flo), float(MDVP_jit), float(MDVP_jitter),
                          float(MDVP_rap), float(MDVP_ppq), float(Jitter_ddp), float(MDVP_Shimmer),
                          float(MDVP_Shimmerdb), float(NHR), float(HNR), float(RPDE), float(DFA),
                          float(spread1), float(spread2), float(D2), float(PPE)]
            
            parkinsons_prediction = parkinsons_model.predict([user_input])
            
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = 'The Person has Parkinson’s Disease'
            else:
                parkinsons_diagnosis = 'The Person does not have Parkinson’s Disease'
        
        except ValueError:
            parkinsons_diagnosis = "Error: Please enter valid numerical values."

        st.success(parkinsons_diagnosis)
