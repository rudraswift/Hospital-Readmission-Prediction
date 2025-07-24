Project: Hospital Readmission Prediction

Team Name: Team(SC1)3_5

Team Members:
1)Rudra Abhishek Badatia
2)U.Gopal Krishna
3)Vinayak Tripathy

Project Description

Problem Statement:
Hospital readmissions are a major issue in healthcare, resulting in increased medical costs and patient stress. Identifying patients at high risk of being readmitted within a short period (e.g., 30 days) can help improve patient care and reduce unnecessary readmissions.

Objective:
To develop a machine learning-based predictive model that can identify patients who are likely to be readmitted to the hospital. The model can assist healthcare providers in making early interventions and improving treatment plans.

Dataset:
The dataset is taken from a hospital record system (or UCI Machine Learning Repository). It includes:
--> Patient demographics (age, gender)
--> Medical conditions (diagnosis codes)
--> Number of previous admissions
--> Length of stay
--> Medications and lab results
--> Readmission status

Approach:
We performed the following steps:
--> Data cleaning and preprocessing
--> Exploratory data analysis (EDA)
--> Feature selection
--> Built models using:
   -> Logistic Regression
   -> Random Forest
   -> Decision Tree
--> Evaluated models using accuracy, precision, recall, and F1-score
--> Visualized key trends and risk factors using graphs

Key Features:
--> Predict readmission within 30 days
--> Identify top 5 medical conditions contributing to readmission
--> Streamlit app for live prediction

Outcome:
Our model achieved ~85% accuracy in predicting readmission. Hospitals can use this to take proactive action with at-risk patients and reduce operational costs.

Presentation:
[Click to view our presentation and Demo video](https://drive.google.com/drive/folders/1Si-xYpG_fR4b_E0jC81ZGqfVLhVdYSLL?usp=sharing)

How to Run:
1. Clone the repository
2. Open the Jupyter Notebook 'analysis.ipynb'
3. Follow instructions in the notebook to run the analysis

Tools Used:
1) Python
2) Pandas, Matplotlib, Scikit-learn
3) Streamlit
