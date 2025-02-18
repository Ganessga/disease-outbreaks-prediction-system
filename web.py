import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

st.set_page_config(page_title='Prediction of Disease Outbreaks', 
                   layout='wide', 
                   page_icon="🩺")

diabetes_model = pickle.load(open(r"C:\Users\Shalini\OneDrive\Documents\Disease Prediction\saved models\diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\Shalini\OneDrive\Documents\Disease Prediction\saved models\heart_model.sav",'rb'))
parkinsons_model = pickle.load(open(r"C:\Users\Shalini\OneDrive\Documents\Disease Prediction\saved models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

with st.sidebar:
    st.title("Disease Prediction System")
    st.markdown("""
        This system predicts disease outbreaks using machine learning models for:
        - Diabetes
        - Heart Disease
        - Parkinson's
    """)

def display_card(result):
    st.markdown(
        f"""
        <style>
        .card {{
            background-color: #e0f7fa;  
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}
            .card h2 {{
            color: #000000;  
        }}
            .card p {{
            color: #000000;  
            font-size: 18px;
        }}
        </style>
        <div class="card">
            <h2>Prediction Result</h2>
            <p>{result}</p>
        </div>
        <br> <!-- Adds space between card and chart -->
        """, unsafe_allow_html=True
    )

def display_prediction_and_chart(prediction, labels, model_name):
    if prediction[0] == 1:
        diagnosis = f"✅ The Person has {model_name}"
    else:
        diagnosis = f"❌ The Person does not have {model_name}"

    display_card(diagnosis)

    colors = ['#ff4c4c', '#66c466'] 
    fig, ax = plt.subplots()
    ax.pie([prediction[0], 1 - prediction[0]], labels=labels, autopct='%1.1f%%',colors=colors)
    st.pyplot(fig)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure Value')
    with col1:
        Skinthickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the person')


    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.error("Please fill all the fields.")
        else:
            user_input = [Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]
            diab_prediction = diabetes_model.predict([user_input])
            
            display_prediction_and_chart(diab_prediction, ['Diabetic', 'Not Diabetic'], "Diabetes")

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Gender of the person')
    with col3:
        cp = st.text_input('CP Value')
    with col1:
        trestbps = st.text_input('Trestbps Value')
    with col2:
        chol = st.text_input('Chol Value')
    with col3:
        fbs = st.text_input('Fbs Value')
    with col1:
        restecg = st.text_input('Restecg Value')
    with col2:
        thalach = st.text_input('Thalach Value')
    with col3:
        exang = st.text_input('Exang Value')
    with col1:
        oldpeak = st.text_input('Oldpeak Value')
    with col2:
        slope = st.text_input('Slope Value')
    with col3:
        ca = st.text_input('Ca Value')
    with col1:
        thal = st.text_input('Thal Value')


    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.error("Please fill all the fields.")
        else:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_model.predict([user_input])
            
            display_prediction_and_chart(heart_prediction, ['Heart Disease', 'No Heart Disease'], "Heart Disease")

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction Using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        name = st.text_input('Name of the person')
    with col2:
        MDVP_fo = st.text_input('MDVP:Fo(Hz) Value')
    with col3:
        MDVP_fhi = st.text_input('MDVP:Fhi(Hz) Value')
    with col1:
        MDVP_flo = st.text_input('MDVP:Flo(Hz) Value')
    with col2:
        MDVP_jit = st.text_input('MDVP:Jitter(%) Value')
    with col3:
        MDVP_jitter = st.text_input('MDVP:Jitter(Abs) Value')
    with col1:
        MDVP_rap = st.text_input('MDVP:RAP Value')
    with col2:
        MDVP_ppq = st.text_input('MDVP:PPQ Value')
    with col3:
        Jitter_ddp = st.text_input('Jitter:DDP Value')
    with col1:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer Value')
    with col2:
        MDVP_Shimmerdb = st.text_input('MDVP:Shimmer(dB) Value')
    with col3:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3 Value')
    with col1:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5 Value')
    with col2:
        MDVP_APQ = st.text_input('MDVP:APQ Value')
    with col3:
        Shimmer_DDA = st.text_input('Shimmer:DDA Value')
    with col1:
        NHR = st.text_input('NHR Value')
    with col2:
        HNR = st.text_input('HNR Value')
    with col3:
        RPDE = st.text_input('RPDE Value')
    with col1:
        DFA = st.text_input('DFA Value')
    with col2:
        spread1 = st.text_input('spread1 Value')
    with col3:
        spread2 = st.text_input('spread2 Value')
    with col1:
        D2 = st.text_input('D2 Value')
    with col2:
        PPE = st.text_input('PPE Value')

    if st.button('Parkinsons Test Result'):
        if not all([name, MDVP_fo, MDVP_fhi, MDVP_flo, MDVP_jit, MDVP_jitter, MDVP_rap, MDVP_ppq, Jitter_ddp, 
                    MDVP_Shimmer, MDVP_Shimmerdb, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, 
                    RPDE, DFA, spread1, spread2, D2, PPE]):
            st.error("Please fill all the fields.")
        else:
            user_input = [MDVP_fo, MDVP_fhi, MDVP_flo, MDVP_jit, MDVP_jitter, MDVP_rap, MDVP_ppq, Jitter_ddp, 
                          MDVP_Shimmer, MDVP_Shimmerdb, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, 
                          HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])

            display_prediction_and_chart(parkinsons_prediction, ['Parkinsons Disease', 'No Parkinsons Disease'], "Parkinson's")
