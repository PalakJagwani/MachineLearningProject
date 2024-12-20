## END TO END MACHINE LEARNING PROJECT : STUDENT PERFORMANCE PREDICTION

## Overview
The goal of this project is to predict a student's performance in mathematics based on multiple features such as their study habits, family background, test preparation, and more. The application uses supervised machine learning models and implements hyperparameter tuning to select the best performing model.

## Features
- Predict Student Math Score: Input various factors like study hours, parental education, lunch, test preparation, etc., to predict the student's math score.
- Hyperparameter Tuning: Models are fine-tuned using techniques like GridSearchCV or RandomizedSearchCV to achieve the best prediction performance.
- Model Comparison: Multiple models (e.g., Linear Regression, Random Forest, Support Vector Machine) are trained and evaluated to choose the best one.

## Requirements
- Python 3.x

## Libraries:
- numpy
- pandas
- matplotlib
- scikit-learn
- streamlit (for deployment)

##You can install the required dependencies using:
```
pip install -r requirements.txt
```

## Installation
Clone this repository:

git clone https://github.com/PalakJagwani/MachineLearningProject.git

## Streamlit to launch the web app where users can input student data and get predictions. To run the Streamlit app, use the following command:

```
streamlit run app.py
```

## Input Data:
The app will ask you to provide features like:

- Gender
- Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score
After entering the values, it will predict the student's math score.

## Live Link
```
https://student-performance-prediction-v4kznyvnecgiofbf3ywkpl.streamlit.app/
```