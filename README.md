# Predictive Maintenance Analytics System

## Overview

<img width="645" height="358" alt="Screenshot 2026-05-10 145948" src="https://github.com/user-attachments/assets/04d76eeb-f26e-4986-8dc1-2a7b1f53e482" />



This project is an AI-powered predictive maintenance analytics system built using Python, Pandas, Matplotlib, Scikit-learn, and Power BI concepts. The project analyzes industrial machine telemetry data to identify machine failure patterns, engineer meaningful operational features, and train a machine learning model capable of predicting machine failures.

The dataset contains 10,000 machine operation records with sensor-based telemetry data such as:

* Air temperature
* Process temperature
* Rotational speed
* Torque
* Tool wear
* Failure modes

The system simulates a real-world industrial monitoring workflow commonly used in:

* Smart manufacturing
* Industrial IoT systems
* Automotive telemetry
* Predictive maintenance platforms
* AI-based monitoring systems

---

# Project Goals

The main objectives of this project were:

* Analyze industrial sensor telemetry data
* Understand machine failure patterns
* Engineer meaningful operational features
* Build machine learning classification models
* Visualize operational insights and failures
* Simulate real predictive maintenance workflows
* Prepare data for dashboard and reporting systems

---

# Technologies Used

## Programming & Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

## Machine Learning

* Random Forest Classifier

## Visualization

* Matplotlib
* Power BI (planned dashboard integration)

## Development Tools

* VS Code
* Git
* GitHub

---

# Dataset Information

Dataset used:

AI4I 2020 Predictive Maintenance Dataset

The dataset contains 10,000 rows of industrial machine telemetry data and multiple machine failure modes.

## Important Features

| Feature                 | Description                   |
| ----------------------- | ----------------------------- |
| Air temperature [K]     | Ambient operating temperature |
| Process temperature [K] | Machine process temperature   |
| Rotational speed [rpm]  | Rotational speed of machine   |
| Torque [Nm]             | Rotational force applied      |
| Tool wear [min]         | Tool usage duration           |
| Machine failure         | Target variable (0 or 1)      |

## Failure Modes

* Tool Wear Failure (TWF)
* Heat Dissipation Failure (HDF)
* Power Failure (PWF)
* Overstrain Failure (OSF)
* Random Failure (RNF)

---

# Project Workflow

## 1. Data Exploration

Performed exploratory data analysis (EDA) to:

* Inspect dataset structure
* Analyze failure distributions
* Check missing values
* Understand telemetry relationships

## 2. Data Visualization

Created multiple visualizations including:

* Failure mode distributions
* Torque vs rotational speed
* Process temperature analysis
* Tool wear distribution
* Failure highlighted scatter plots
* Confusion matrix visualization
* Feature importance charts

## 3. Feature Engineering

Created engineered features such as:

* Temperature Difference
* Power
* Wear Stress
* High Temperature Flag
* High Torque Flag
* Low RPM Flag

Example power equation used:

[
P = \frac{Torque \times RPM}{9550}
]

These engineered features helped simulate realistic operational analytics and predictive maintenance indicators.

## 4. Machine Learning Model

A Random Forest Classifier was trained to predict machine failures.

### Why Random Forest?

Random Forest was selected because it:

* Performs well on tabular telemetry data
* Handles nonlinear relationships
* Reduces overfitting using multiple decision trees
* Provides feature importance analysis
* Is commonly used in industrial predictive maintenance systems

---

# Key Visualizations & Findings

## Failure Mode Analysis

### Failure Mode Counts
<img width="1000" height="600" alt="failure_mode_counts_bar" src="https://github.com/user-attachments/assets/397c0989-0a19-46b9-83e4-e5cfb3129d28" />

### Findings

* Heat Dissipation Failure was the most common failure mode in the dataset.
* Overstrain and Power failures also occurred frequently.
* Random failures were extremely rare.
* This indicates that thermal conditions and operational stress are major contributors to machine failure.

---

## Failure Mode Distribution

<img width="800" height="800" alt="failure_mode_distribution_pie" src="https://github.com/user-attachments/assets/3cdf641b-35d6-4b47-831b-f2084ce93d51" />


### Findings

* Heat Dissipation Failures accounted for the largest percentage of failures.
* Tool Wear failures represented a smaller portion of total failures.
* The distribution demonstrates how different operational conditions contribute differently to machine reliability.

---

## Temperature Distribution Analysis

<img width="1000" height="600" alt="temperature_distribution_failure" src="https://github.com/user-attachments/assets/32ed6e0e-8b98-4e36-96a3-1f5809407739" />


### Findings

* Failed machines generally operated at slightly higher process temperatures.
* Temperature alone was not enough to cause failure, but higher temperatures increased operational risk.
* This supports the importance of monitoring thermal conditions in predictive maintenance systems.

---

## Process Temperature vs Rotational Speed

<img width="1000" height="600" alt="temperature_vs_rotor_speed" src="https://github.com/user-attachments/assets/58a30069-f6a4-4955-8772-b8bd07fdd94d" />


### Findings

* Machine failures were concentrated around lower rotational speeds combined with elevated process temperatures.
* The visualization highlights abnormal operational regions associated with failures.
* This demonstrates how telemetry relationships can reveal failure patterns.

---

## Heat Dissipation Failure Visualization

<img width="1000" height="600" alt="temperature_vs_rotor_speed_heat_dissipation" src="https://github.com/user-attachments/assets/7292371a-ab42-483b-9c49-bde1fa63227b" />

### Findings

* Heat dissipation failures occurred primarily at lower rotational speeds.
* This aligns with the dataset definition where insufficient cooling combined with low RPM contributes to overheating-related failures.
* The clustered failure region validates the engineering logic behind the dataset.

---

## Torque vs Rotational Speed

<img width="1000" height="600" alt="torque_vs_rotor_speed" src="https://github.com/user-attachments/assets/4021fb3a-7a0b-4ae6-a87e-bc554e7445ba" />


### Findings

* Higher torque values combined with lower rotational speeds were associated with machine failures.
* The inverse relationship between torque and rotational speed became visually apparent.
* Operational stress conditions significantly influenced machine reliability.

---

## Overstrain Failure Analysis

<img width="1000" height="600" alt="torque_vs_rotor_speed_overstrain" src="https://github.com/user-attachments/assets/314adb7f-5bca-419b-9d51-92edb22779a4" />


### Findings

* Overstrain failures occurred primarily in high torque operating regions.
* These failures were strongly connected to increased mechanical stress and tool wear.
* The visualization demonstrates how excessive load conditions can damage industrial systems.

---

## Confusion Matrix

<img width="800" height="600" alt="model_confusion_matrix" src="https://github.com/user-attachments/assets/775fcd66-8d3f-498b-bb2a-eabf5ce8bba7" />


### Findings

* The model correctly classified most normal operating conditions.
* Only a small number of false positives occurred.
* The model successfully identified most machine failures while maintaining strong overall accuracy.
* A limited number of failures were missed, which is important in predictive maintenance applications where false negatives can be costly.

---

## Feature Importance

<img width="1000" height="600" alt="failure_mode_counts_bar" src="https://github.com/user-attachments/assets/7b0fcd40-b252-439e-9694-2fdd1fcdafae" />


### Findings

* Wear Stress was the most influential feature in predicting failures.
* Power and Temperature Difference also contributed strongly to model predictions.
* Engineered features significantly improved model performance.
* Operational stress metrics played a more important role than raw temperature values alone.

---

# Model Performance

## Classification Report

```text
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      1939
           1       0.94      0.80      0.87        61

    accuracy                           0.99      2000
   macro avg       0.97      0.90      0.93      2000
weighted avg       0.99      0.99      0.99      2000
```

## Confusion Matrix

```text
[[1936    3]
 [  12   49]]
```

## Model Insights

* The model achieved 99% overall accuracy
* Successfully identified most machine failures
* Maintained a very low false-positive rate
* Performed well despite dataset imbalance
* Feature engineering improved predictive capability

---

# Key Learning Outcomes

Through this project, I learned:

* Exploratory data analysis workflows
* Data cleaning and preprocessing
* Engineering-based feature creation
* Machine learning classification concepts
* Model evaluation techniques
* Confusion matrix interpretation
* Predictive maintenance analytics
* Data visualization and reporting
* Git and GitHub project management

---

# Project Structure

```text
predictive-maintenance-project/
│
├── data/
│   ├── ai4i2020.csv
│   ├── cleaned_predictive_maintenance.csv
│   └── feature_engineered_data.csv
│
├── scripts/
│   ├── 01_explore_data.py
│   ├── 02_clean_data.py
│   ├── 03_visualize_data.py
│   ├── 04_feature_engineering.py
│   ├── 05_train_model.py
│   └── 06_model_visualization.py
│
├── charts/
│
├── outputs/
├── dashboard/
│   ├── predictive-maintenance-dashboard.pbix
│   └── dashboard_overview.pdf
├── requirements.txt
├── .gitignore
└── README.md
```
# Power BI Dashboard

This project also includes an interactive Power BI dashboard used to visualize:

- Operational KPIs
- Failure analysis
- Telemetry analytics
- Machine learning model insights

## Dashboard Features

- Interactive slicers
- Failure mode analysis
- Telemetry scatter plots
- Feature importance visualization
- Confusion matrix analysis
---

# Author

Avipreet Singh

Computer Science Student at Simon Fraser University

