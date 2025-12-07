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

## Project Structure
```
project-root/
│
├── data/
│   └── insurance_data.csv.dvc  # DVC metadata file
│
├── notebooks/
│   ├── 01_data_quality.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_stats_testing.ipynb
│   └── 04_modeling.ipynb
│
├── models/
│   ├── baseline/               # Early baseline models
│   ├── final/                  # Final models (DVC tracked)
│   └── shap_analysis/          # Model interpretability artifacts
│
├── plots/
│   ├── loss_ratio_province.png
│   ├── claims_postalcode.png
│   └── top_makes_claims.png
│
├── reports/
│   ├── interim/
│   │   └── ACIS_Interim_Report.pdf
│   └── stats_tests/
│       └── statistical_outputs.md
│
├── .github/
│   └── workflows/
│       └── ci.yml              # CI/CD pipeline for linting + DVC checks
│
├── src/
│   ├── data/                   # Scripts for data cleaning, loading
│   ├── features/               # Feature engineering pipeline
│   ├── models/                 # Training / evaluation scripts
│   └── utils/                  # Helper functions
│
├── .dvc/                       # DVC tracking and metadata
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

## ⚙️ Installation & Setup
1. Clone the repository

2. 
```
git clone the repo
cd to the repo
```

3. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

5. Install dependencies
```
pip install -r requirements.txt
```

## 🗂️ Data Version Control (DVC) Setup

This project uses DVC to track data versions and ensure full reproducibility.

Pull the dataset
```
dvc pull
```


This will download the tracked dataset from the configured remote storage.

To add new data versions

```
dvc add data/raw/new_dataset.csv
git add data/raw/new_dataset.csv.dvc
git commit -m "Added new dataset version"
dvc push
```

### ▶️ Running the Project
1. Run EDA

Open notebooks:
```
jupyter notebook notebooks/01_data_quality.ipynb
jupyter notebook notebooks/02_eda.ipynb
```

2. Run Statistical Tests
```
jupyter notebook notebooks/03_stats_testing.ipynb
```

4. Run Machine Learning Pipelines

```
python src/models/train_model.py
```

6. Generate SHAP Interpretability Plots

```
python src/models/shap_analysis.py
```
## 🧪 Tasks Completed

**Task 1: EDA & Stats**

- Git repository set up
- Branch strategy implemented
- EDA completed
- Statistical insights documented

**Task 2: Data Version Control**
- DVC initialized
- Local remote configured
- Dataset versioned
- Reproducible pipeline created

## Deliverables

- A final report detailing methodologies, findings, and recommendations.
- Well-structured and version-controlled code and notebooks.
- Creative and insightful visualizations.

