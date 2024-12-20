import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Title of the app
st.title("Prediction App")

# Create input fields for user data
st.header("Enter your details")

gender = st.selectbox('Gender', ['male', 'female'])
ethnicity = st.selectbox('Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])  # Customize options
parental_level_of_education = st.selectbox('Parental Level of Education', ['some college', "associate's degree", 'some high school', 'high school', "bachelor's degree", "master's degree"])
lunch = st.selectbox('Lunch', ['standard', 'free/reduced'])
test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])
reading_score = st.number_input('Reading Score', min_value=0, max_value=100, step=1)
writing_score = st.number_input('Writing Score', min_value=0, max_value=100, step=1)

# Button to trigger prediction
if st.button('Predict'):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()
    st.write("Data before prediction:")
    st.write(pred_df)

    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    st.header("Prediction Results")
    st.write(f"Predicted Maths Score: {results[0]}")

# Run the Streamlit app using the command below:
# streamlit run app.py
