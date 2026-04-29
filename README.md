# 🏦 Loan Default Risk Predictor

An end-to-end Machine Learning project that predicts the likelihood of loan default using financial and behavioral features, deployed as an interactive web application.

---

## 🌍 Live Demo

🔗 https://loan-default-risk-app-fvjtxw3m7mh49r3y4b8z8j.streamlit.app/

---

## 🚀 Project Overview

This project aims to help assess loan risk by predicting whether a loan applicant is likely to default. It covers the complete machine learning lifecycle—from data preprocessing and model building to deployment using Streamlit.

---

## 🎯 Objectives

* Predict loan default probability using ML models
* Identify key risk-driving features
* Build a full ML pipeline
* Deploy an interactive web application for real-time predictions

---

## 🧠 Machine Learning Workflow

### 1. Data Preprocessing

* Handled missing values using median (numerical) and mode (categorical)
* Removed irrelevant features (ID, low-variance columns)
* Treated outliers

---

### 2. Exploratory Data Analysis (EDA)

* Target variable distribution
* Feature distributions and relationships
* Outlier detection
* Correlation heatmap
* Numerical vs target analysis
* Categorical vs target analysis

---

### 3. Model Building

Trained and evaluated:

* Logistic Regression
* Random Forest Classifier ✅ (Selected Model)
* XGBoost

---

### 4. Model Optimization

* Feature importance analysis
* Selected top contributing features
* Retrained model on reduced feature set
* Improved model performance and interpretability

---

### 5. Threshold Tuning

* Final threshold: **0.6**
* Achieved higher recall for default class
* Balanced precision-recall trade-off

---

## 📊 Final Model Performance

| Metric              | Value |
| ------------------- | ----- |
| Accuracy            | ~0.91 |
| Precision (Default) | ~0.72 |
| Recall (Default)    | ~0.99 |
| F1 Score            | ~0.84 |

👉 The model prioritizes **high recall** to minimize missed default cases.

---

## 🖥️ Web Application Features

* Real-time loan default prediction
* Risk categorization:

  * 🟢 Low Risk
  * 🟡 Medium Risk
  * 🔴 High Risk
* Probability score display
* Interactive and user-friendly interface

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## 📁 Project Structure

```
loan-default-risk-app/
│
├── app.py
├── loan_default_model.pkl
├── model_columns.pkl
├── sc.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/loan-default-risk-app.git
cd loan-default-risk-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Key Insights

* Interest rate and Loan-to-Value (LTV) are strong predictors
* High recall ensures minimal missed defaulters
* Model predictions are well-distributed after feature refinement

---

## ⚠️ Limitations

* Predictions depend on dataset patterns
* Some high-risk cases may show moderate probabilities
* Limited feature scope

---

## 🚀 Future Improvements

* Add model explainability (SHAP)
* Improve probability calibration
* Enhance UI with dashboards and visualizations
* Integrate more features for better accuracy

---

## 👤 Author

**Hiya Maiti**

---

## ⭐ If you found this useful

Give this repo a ⭐ and feel free to share feedback!
