import streamlit as st
import numpy as np
import pandas as pd
import datetime
from sklearn.ensemble import GradientBoostingRegressor

import joblib

# Load the pre-trained model using joblib
model = joblib.load('model_joblib_gr.json')

def main():
    html_temp = """
     <div style = "background-color:lightblue;padding:0px">
     <h2 style="color:black;text-align:center;"> Health Insurance Prediction Using ML</h2>
     </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.write('')
    st.write('')

    p1 = st.number_input('Enter Your Age:', 1.0, 120.0, step=1.0)

    s1 = st.selectbox('Enter Your Gender:', ('Male', 'Female'))
    if s1 == "Male":
        p4 = 0
    elif s1 == "Female":
        p4 = 1

    p5 = st.number_input('Enter Your BMI Value:', 1.0, 200.0, step=1.0)

    p6 = st.number_input('How Many Children You Have:', 0.0, 20.0, step=1.0)

    s2 = st.selectbox('Enter Your Region:', ('southwest', 'southeast', 'northwest', 'northeast'))
    if s2 == "southwest":
        p7 = 1
    elif s2 == "southeast":
        p7 = 2
    elif s2 == "northwest":
        p7 = 3
    elif s2 == "northeast":
        p7 = 4

    s3 = st.selectbox('Are You Smoker:', ('Yes', 'No'))
    if s3 == "Yes":
        p8 = 1
    elif s3 == "No":
        p8 = 0

    customer = pd.DataFrame({'age': [p1],
                             'sex': [p4],
                             'bmi': [p5],
                             'children': [p6],
                             'smoker': [p8],
                             'region': [p7]
                             })

    try:
        if st.button('Predict'):
            prediction = model.predict(customer)
            if prediction > 0:
                st.success('Your Predicted Health Insurance Cost Is: '.format(prediction[0]))
            else:
                st.warning("You Will Not Be Able To Get This Health Insurance!!")
    except Exception as e:
        st.warning("Oops!! Something went wrong\nTry again")
        st.write(e)

if __name__ == '__main__':
    main()
