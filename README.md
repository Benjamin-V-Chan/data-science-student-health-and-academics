# data-science-student-health-and-academics

# Project Overview
This project analyzes the impact of mobile phone usage on students' health and academic performance. The analysis involves data preprocessing, exploratory data analysis (EDA), visualization, and predictive modeling.

# Folder Structure
```
project-root/
├── data/          # Contains the dataset
├── scripts/       # Python scripts for data processing, analysis, and modeling
├── outputs/       # Stores results, cleaned data, and visualizations
├── requirements.txt  # List of required Python dependencies
└── README.md      # Project documentation
```

# Usage
### 1. Setup the Project:
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 2. Run Data Preprocessing:
This script cleans the dataset and saves a cleaned version.
```bash
python scripts/01_preprocess.py
```

### 3. Perform Exploratory Data Analysis:
This script generates summary statistics of the dataset.
```bash
python scripts/02_exploratory_analysis.py
```

### 4. Generate Data Visualizations:
This script creates visualizations for key categorical variables.
```bash
python scripts/03_visualization.py
```

### 5. Train and Evaluate a Predictive Model:
This script trains a decision tree model to predict students' health ratings.
```bash
python scripts/04_modeling.py
```

# Requirements
- Python 3.x
- pandas
- matplotlib
- scikit-learn

# Acknowledgments
- **Dataset Name:** Students Health & Academic Performance
- **Dataset Author:** Mursaleen Ameer
- **Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/innocentmfa/students-health-and-academic-performance)