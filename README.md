# MLOPS Project: German Credit Risk Prediction

This project implements an end-to-end MLOps pipeline for predicting whether an applicant poses a good or bad credit risk. It covers data preparation, model training and experiment tracking, model deployment, user interface development, and model monitoring.

---

## Project Overview

- **Data Preparation:**  
  Loaded the dataset and defined the schema, generated data profile report using ydata-profiling, and splitted it into training, test, and production sets.

- **Experiment Tracking & Model Training:**  
  Built an ML pipeline with scikit-learn and conducted multiple experiments which were tracked with MLflow. The best model (SVC) was selected based on test accuracies.

- **Model Deployment:**  
  Deployed the chosen model using FastAPI, and the deployment was integrated with a Streamlit UI for user interaction.

- **Model Monitoring:**  
  Data drift (numeric as well as categorical) is monitored using alibi-detect to ensure consistency among the production and training data.

---

## Running the Notebooks and Components

### Notebook1: Data Preparation and Experiment Tracking
- **Content:**  
  Contains code for data ingestion, data profiling, train-test-production split, building the ML pipeline, and MLflow experiment tracking.
- **Usage:**  
  Open and run `Gr-05_Notebook-1.ipynb` in your Jupyter environment to reproduce the experiments.

### Notebook2: Model Deployment using FastAPI
- **Content:**  
  Contains FastAPI code to deploy the best model.
- **Converted to Python File:**  
  The code has been converted to `app.py` for command-line execution.
- **Run the FastAPI App:**
  ```bash
  uvicorn app:app --reload

### Notebook3: Streamlit UI
**Content:**  
  Contains the Streamlit UI code for collecting user inputs and displaying predictions.  
  
**Converted to Python File:**  
  The code has been converted to `Streamlit.py`.  
  
**Run the Streamlit UI:**
  ```bash
  streamlit run Streamlit.py



