# import necessary libraries
import streamlit as st
import requests

# URL of FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict"

def get_prediction(input_data):
    """
    Sends input data to a specified FastAPI endpoint and retrieves the model's prediction.

    Parameters:
    - input_data (dict): A dictionary containing the input data in JSON format as expected by the model.

    Returns:
    - dict: A dictionary containing the model's prediction response.

    The function performs an HTTP POST request to the FastAPI endpoint. The JSON response from the API, is parsed and returned as a Python dictionary.
    """
    response = requests.post(FASTAPI_URL, json=input_data)
    return response.json()


def get_prediction_description(prediction):
    """
    Provides a descriptive interpretation of the credit risk prediction.

    Parameters:
    - prediction (int): The prediction result from the model

    Returns:
    - str: A string describing the implications of the credit risk prediction.
    
    This function translates numerical prediction values into a short interpretation of the prediction outcomes.
    """
    if prediction == 1:  # denotes 'Good' Credit Risk
        description = ("Low Risk - The loan or credit application is likely to be safe.")
    elif prediction == 2:  # denotes 'Bad' Credit Risk
        description = ("High Risk - The loan or credit application is likely to be risky.")
    else:
        description = "Unknown Credit Risk: Unable to determine the risk level from the provided information."
    return description

# Mappings from descriptive names to codes for categorical variables

account_status_options = {
    "< 0 DM": "A11",
    "0 - 200 DM (0 inclusive)": "A12",
    ">= 200 DM / salary assignments for at least 1 year": "A13",
    "no checking account": "A14"
}

credit_history_options = {
    "no credits taken/all credits paid back duly": "A30",
    "all credits at this bank paid back duly": "A31",
    "existing credits paid back duly till now": "A32",
    "delay in paying off in the past": "A33",
    "critical account/other credits existing (not at this bank)": "A34"
}

purpose_options = {
    "car (new)": "A40",
    "car (used)": "A41",
    "furniture/equipment": "A42",
    "radio/television": "A43",
    "domestic appliances": "A44",
    "repairs": "A45",
    "education": "A46",
    "retraining": "A48",
    "business": "A49",
    "others": "A410"
}

savings_account_options = {
    "< 100 DM": "A61",
    "100 - 500 DM (100 inclusive)": "A62",
    "500 - 1000 DM (500 inclusive)": "A63",
    ">= 1000 DM": "A64",
    "unknown/no savings account": "A65"
}

employment_duration_options = {
    "unemployed": "A71",
    "< 1 year": "A72",
    "1-4 years (1 inclusive)": "A73",
    "4-7 years (4 inclusive)": "A74",
    ">= 7 years": "A75"
}

personal_status_sex_options = {
    "male: divorced/separated": "A91",
    "female: divorced/separated/married": "A92",
    "male: single": "A93",
    "male: married/widowed": "A94",
    "female: single": "A95"
}

other_debtors_options = {
    "none": "A101",
    "guarantor": "A102",
    "co-applicant": "A103"
}

property_options = {
    "real estate": "A121",
    "building society savings agreement/life insurance": "A122",
    "car or other": "A123",
    "unknown/no property": "A124"
}

other_installment_plans_options = {
    "bank": "A141",
    "stores": "A142",
    "none": "A143"
}

housing_options = {
    "rent": "A151",
    "own": "A152",
    "for free": "A153"
}

job_options = {
    "unemployed/unskilled - non-resident": "A171",
    "unskilled - resident": "A172",
    "skilled employee/official": "A173",
    "management/self-employed/highly qualified employee/officer": "A174"
}

telephone_options = {
    "none": "A191",
    "yes, registered under the customer's name": "A192"
}

foreign_worker_options = {
    "yes": "A201",
    "no": "A202"
}

# Define the Streamlit layout
st.title('German Credit Risk Prediction')
with st.form("prediction_form"):
    # Creating input fields for each feature
    status_of_existing_checking_account = st.selectbox("Status of Existing Checking Account", options=list(account_status_options.keys()))
    duration_in_months = st.number_input("Duration in Months", min_value=1, max_value=120, value=12)
    credit_history = st.selectbox("Credit History", options=list(credit_history_options.keys()))
    purpose = st.selectbox("Purpose", options=list(purpose_options.keys()))
    credit_amount = st.number_input("Credit Amount", min_value=0, value=5000, format='%d')
    savings_account = st.selectbox("Savings Account/Bonds", options=list(savings_account_options.keys()))
    employment_duration = st.selectbox("Present Employment Since", options=list(employment_duration_options.keys()))
    installment_rate = st.slider("Installment Rate in Percentage of Disposable Income", 1, 100, 25)
    personal_status_sex = st.selectbox("Personal Status and Sex", options=list(personal_status_sex_options.keys()))
    other_debtors = st.selectbox("Other Debtors/Guarantors", options=list(other_debtors_options.keys()))
    present_residence_since = st.slider("Present Residence Since", 1, 10, 4)
    property = st.selectbox("Property", options=list(property_options.keys()))
    age_years = st.slider("Age in Years", 18, 100, 35)
    other_installment_plans = st.selectbox("Other Installment Plans", options=list(other_installment_plans_options.keys()))
    housing = st.selectbox("Housing", options=list(housing_options.keys()))
    num_existing_credits = st.slider("Number of Existing Credits at This Bank", 1, 10, 2)
    job = st.selectbox("Job", options=list(job_options.keys()))
    num_people_liable = st.slider("Number of People Being Liable to Provide Maintenance For", 0, 5, 1)
    telephone = st.selectbox("Telephone", options=list(telephone_options.keys()))
    foreign_worker = st.selectbox("Foreign Worker", options=list(foreign_worker_options.keys()))

    # When the user clicks the 'Predict' button
    submitted = st.form_submit_button("Predict")
    if submitted:
        # Prepare the data in the format expected by our model
        model_input = {
            "ExistingAccount_Status": account_status_options[status_of_existing_checking_account],
            "Duration_Months": duration_in_months,
            "Credit_History": credit_history_options[credit_history],
            "Purpose": purpose_options[purpose],
            "Credit_Amount": credit_amount,
            "SavingsAccount_Bonds": savings_account_options[savings_account],
            "Present_Employment_Since": employment_duration_options[employment_duration],
            "Installment_Rate": installment_rate,
            "PersonalStatus_Sex": personal_status_sex_options[personal_status_sex],
            "OtherDebtors_Guarantors": other_debtors_options[other_debtors],
            "Present_Residence_Since": present_residence_since,
            "Property": property_options[property],
            "Age_Years": age_years,
            "Other_Installment_Plans": other_installment_plans_options[other_installment_plans],
            "Housing": housing_options[housing],
            "Num_Existing_Credits": num_existing_credits,
            "Job": job_options[job],
            "Num_People_Liable": num_people_liable,
            "Telephone": telephone_options[telephone],
            "Foreign_Worker": foreign_worker_options[foreign_worker]
        }
 
        prediction_response = get_prediction(model_input)
        # store the received prediction result
        prediction = prediction_response['prediction'][0]

        result = ""

        if prediction == 1:
            result = "Good"
        elif prediction == 2:
            result = "Bad"
        else:
            result = "Unknown"
        
        # Get descriptive text for the prediction
        description = get_prediction_description(prediction)

        # Display the predicted class 
        st.write(f"Prediction: {result}")
        
        # Display the predicted class description
        st.write(description)