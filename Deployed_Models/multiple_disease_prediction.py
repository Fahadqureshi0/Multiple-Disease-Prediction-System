import os
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading saved Models
diabetes_disease_model = pickle.load(open('C:/Users/Fahad Qureshi/Downloads/Deployed_Models/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Fahad Qureshi/Downloads/Deployed_Models/saved_models/heart_model.sav', 'rb'))

parkinsons_disease_model = pickle.load(open('C:/Users/Fahad Qureshi/Downloads/Deployed_Models/saved_models/parkinson_model.sav', 'rb'))

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                            ['Diabetes Disease Prediction',
                             'Heart Disease Prediction',
                             'Parkinsons Disease Prediction'],

                             icons = ['activity','heart','person'],

                            default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Disease Prediction':
    st.title('Diabetes Disease Prediction System')


    # Getting Input Data: 
    # Columns for Input Fields: 
    col1, col2, col3 = st.columns(3)

    with col1: 
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2: 
        Glucose = st.text_input('Glucose Level')
    # Getting input data from user: 
    
    with col3: 
        BloodPressure = st.text_input('BloodPressure Value')
    with col1: 
        SkinThickness = st.text_input('SkinThickness value')
    with col2: 
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreePrediction = st.text_input('Diabetes Pedigree Function ')
    with col1:
        Age = st.text_input('Age of Person')

    # Code for Prediction
    diab_diagnosis = ""

    # Button
    if st.button('Diabetes Test'):
        diab_prediction = diabetes_disease_model.predict([[
            float(Pregnancies),
            float(Glucose),
            float(BloodPressure),
            float(SkinThickness),
            float(Insulin),
            float(BMI),
            float(DiabetesPedigreePrediction),
            float(Age)
        ]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'Person is Diabetic'
        else:
            diab_diagnosis = 'Person is not Diabetic'

    st.success(diab_diagnosis)



# Heart Disease Prediction Page# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction System')

    # Columns for Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Person Age')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        Chest_Pain = st.text_input('Chest Pain Value')
    with col1:
        Resting_Blood_Pressure = st.text_input('BloodPressure Value')
    with col2:
        chol = st.text_input('chol Value')
    with col3:
        Fasting_Blood_Pressure = st.text_input('Fasting Blood Sugar')
    with col1:
        restecg = st.text_input('restecg Value')
    with col2:
        thalach = st.text_input('thalach Value')
    with col3:
        exang = st.text_input('exang Value')
    with col1:
        oldpeak = st.text_input('oldpeak Value')
    with col2:
        slope = st.text_input('slope value')
    with col3:
        ca = st.text_input('ca value')
    with col1:
        thal = st.text_input('thal')

    # Code for Prediction
    heart_diagnosis = ""

    # Button
    if st.button('Heart Test'):
        heart_prediction = heart_disease_model.predict([[
            float(Age),
            float(Sex),
            float(Chest_Pain),
            float(Resting_Blood_Pressure),
            float(chol),
            float(Fasting_Blood_Pressure),
            float(restecg),
            float(thalach),
            float(exang),
            float(oldpeak),
            float(slope),
            float(ca),
            float(thal)
        ]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'Person has Heart Disease'
        else:
            heart_diagnosis = 'Person does not have Heart Disease'

    st.success(heart_diagnosis)

# Parkinsons Disease Prediction Page
elif selected == 'Parkinsons Disease Prediction':
    st.title('Parkinsons Disease Prediction System')

    # Columns for Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RAP = st.text_input('MDVP:RAP')
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    with col2:
        DDP = st.text_input('Jitter:DDP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR Value')
    with col1:
        HNR = st.text_input('HNR Value')
    with col2:
        RPDE = st.text_input('RPDE Value')
    with col3:
        DFA = st.text_input('DFA Value')
    with col1:
        spread1 = st.text_input('Spread1 Value')
    with col2:
        spread2 = st.text_input('Spread2 Value')
    with col3:
        D2 = st.text_input('D2 Value')
    with col1:
        PPE = st.text_input('PPE Value')

    # Code for Prediction
    parkinsons_diagnosis = ""

    # Button
    if st.button('Parkinsons Test'):
        parkinsons_prediction = parkinsons_disease_model.predict([[
            float(fo),
            float(fhi),
            float(flo),
            float(Jitter_percent),
            float(Jitter_Abs),
            float(RAP),
            float(PPQ),
            float(DDP),
            float(Shimmer),
            float(Shimmer_dB),
            float(APQ3),
            float(APQ5),
            float(APQ),
            float(DDA),
            float(NHR),
            float(HNR),
            float(RPDE),
            float(DFA),
            float(spread1),
            float(spread2),
            float(D2),
            float(PPE)
        ]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = 'Person has Parkinsons Disease'
        else:
            parkinsons_diagnosis = 'Person does not have Parkinsons Disease'

    st.success(parkinsons_diagnosis)