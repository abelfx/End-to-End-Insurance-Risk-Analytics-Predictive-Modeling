# Insurance Risk Analytics & Predictive Modeling

This project focuses on analyzing historical insurance claim data to optimize marketing strategies and identify low-risk customer segments for AlphaCare Insurance Solutions (ACIS). By leveraging data engineering, predictive analytics, and machine learning, we aim to build models that can predict optimal premium values and inform business decisions.

## Business Objective

The primary goal is to help ACIS develop cutting-edge risk and predictive analytics for car insurance planning and marketing in South Africa. By analyzing historical data, we will identify "low-risk" targets for whom premiums could be reduced, creating opportunities to attract new clients.

### Key Areas of Analysis:

- **Insurance Terminologies:** Understanding key insurance concepts.
- **A/B Hypothesis Testing:** Testing hypotheses about risk differences across various segments.
- **Machine Learning & Statistical Modeling:** Building predictive models for claims and optimal premiums.

## Motivation

This challenge is designed to enhance skills in:

- **Data Engineering (DE):** Managing and processing complex datasets.
- **Predictive Analytics (PA):** Uncovering patterns and making predictions.
- **Machine Learning Engineering (MLE):** Building and deploying machine learning models.

## Data

The dataset contains historical insurance data from February 2014 to August 2015. The data is located in the `data/` directory.

### Data Structure:

The data includes columns related to:

- Insurance Policy
- Client Information
- Client Location
- Insured Car
- Insurance Plan
- Payments & Claims

## Learning Outcomes

- **Data Exploration and Insight Extraction:** Using various techniques to understand the data.
- **EDA and ML Pipelines:** Understanding data structures and algorithms.
- **Python Programming:** Writing modular and object-oriented code.
- **Statistical Modeling:** Applying statistical models for prediction and analysis.
- **A/B Testing:** Designing and implementing robust A/B tests.
- **Data Versioning:** Using DVC to manage datasets.
- **Predictive Modeling:** Build regression and classification models to predict claim severity, claim probability, and risk-adjusted premiums.
- **Feature Engineering:** Create derived features such as loss ratio, vehicle age, and interaction terms for better model performance.
- **Model Interpretability:** Use SHAP to identify top drivers of risk and provide actionable insights for premium optimization.

## Tasks

### Task 1: EDA & Stats

- **1.1 Git and GitHub:**
  - Set up a Git repository with a proper `README.md`.
  - Use Git for version control.
  - Implement CI/CD with GitHub Actions.
- **1.2 Project Planning - EDA & Stats:**
  - Perform Exploratory Data Analysis (EDA) to understand the data, assess its quality, and find initial patterns.
  - Conduct statistical analysis to guide modeling.

### Task 2: Data Version Control

- Establish a reproducible data pipeline using Data Version Control (DVC).
- Version datasets and track changes.

### Task 3: A/B Hypothesis Testing

- Tested key business hypotheses about risk across provinces, gender, and postal codes.
- Measured Claim Frequency, Claim Severity, and Margin as KPIs.
- Rejected or failed to reject hypotheses based on statistical significance (p-values).
- Provided business recommendations, e.g., adjusting premiums for high-risk provinces like Gauteng.

### Task 4: Predictive Modeling & Risk-Based Premiums

- Prepared numeric and categorical features with imputation and encoding.
- Trained models to predict claim severity (Linear Regression, Random Forest, XGBoost).
- Built claim probability model (classification) to estimate the likelihood of a claim.
- Developed a dynamic, risk-based premium framework:

- Premium=(Predicted Probability of Claim×Predicted Claim Severity)+Expenses+Profit Margin
- Evaluated models using RMSE, R², and feature importance via SHAP for actionable insights.
- Recommended premium adjustments based on province, vehicle type, and policyholder characteristics.

## Deliverables

- Final Report: Detailed methodologies, results, and business recommendations.
- Notebooks & Code: Well-structured, modular, and version-controlled.
- Visualizations: Clear and interpretable charts for EDA, statistical testing, and model interpretation.
- Predictive Models: Fully prepared pipeline for claim severity, claim probability, and risk-based premium estimation.

## Installation

To run this project locally, follow these steps:
Clone the repository:
```
git clone https://github.com/<your-username>/insurance-risk-analytics.git
cd insurance-risk-analytics
```

Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

Set up data:

- Place the dataset in the data/ folder.
- Ensure the filename matches MachineLearningRating_v3.txt or update paths in notebooks.

Run Jupyter notebooks or scripts:
```
jupyter notebook
```
