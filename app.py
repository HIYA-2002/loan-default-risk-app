import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("loan_default_model.pkl")
sc = joblib.load("sc.pkl")
model_columns =joblib.load("model_columns.pkl")



st.markdown("""
<h1 style='text-align: center;'>🏦 Loan Default Risk Analyzer</h1>
<p style='text-align: center;'>Smart prediction using Machine Learning</p>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Loan Risk Predictor", layout="wide")


st.write("Enter applicant details:")

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)


with col1:
    loan_amount = st.number_input("Loan Amount", min_value=0.0)
    property_value = st.number_input("Property Value", min_value=0.0)
    income = st.number_input("Income", min_value=0.0)
    credit_score = st.number_input("Credit Score", min_value=300, max_value=900)


with col2:
    rate_of_interest = st.number_input("Interest Rate", min_value=0.0)
    ltv = st.number_input("Loan-to-Value (LTV)", min_value=0.0)
    dtir1 = st.number_input("Debt-to-Income Ratio", min_value=0.0)

# ---------- CATEGORICAL ----------
st.subheader("Loan Characteristics")

col3, col4, col5 = st.columns(3)

with col3:
    credit_type = st.selectbox("Credit Type", ["CRIF", "EQUI", "EXP"])

with col4:
    neg_amortization = st.selectbox("Negative Amortization", ["Yes", "No"])

with col5:
    lump_sum_payment = st.selectbox("Lump Sum Payment", ["Yes", "No"])

# Button
if st.button("Predict Risk"):
    # Step 1: Create input dictionary
    input_dict = {
        'loan_amount': loan_amount,
        'rate_of_interest': rate_of_interest,
        'property_value': property_value,
        'income': income,
        'Credit_Score': credit_score,
        'LTV': ltv,
        'dtir1': dtir1,

        # Default all dummy variables to 0
        'credit_type_EQUI': 0,
        'Neg_ammortization_not_neg': 0,
        'lump_sum_payment_not_lpsm': 0
    }
        
    
    # Handle categorical → dummy mapping

    if credit_type == "EQUI":
        input_dict['credit_type_EQUI'] = 1

    if neg_amortization == "No":
        input_dict['Neg_ammortization_not_neg'] = 1

    if lump_sum_payment == "No":
        input_dict['lump_sum_payment_not_lpsm'] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure correct column order
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Predict probability
    prob = model.predict_proba(input_df)[0][1]

    # Apply threshold
    prediction = 1 if prob > 0.6 else 0


    st.subheader("📊 Prediction Result")

    # ---------- RISK LEVEL ----------
    if prob < 0.3:
        st.markdown(f"<p class='risk-low'>🟢 Low Risk</p>", unsafe_allow_html=True)
    elif prob < 0.6:
        st.markdown(f"<p class='risk-medium'>🟡 Medium Risk</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p class='risk-high'>🔴 High Risk</p>", unsafe_allow_html=True)

    # ---------- PROBABILITY ----------
    st.write(f"**Default Probability:** {prob:.2f}")

    # ---------- PROGRESS BAR ----------
    st.progress(float(prob))

    # ---------- INTERPRETATION ----------
    st.subheader("💡 Interpretation")
    # Output
    if prediction == 1:
        st.write("The applicant shows a higher likelihood of default. "
            "Consider reviewing credit profile, income stability, and loan structure.")
    else:
        st.write(
            "The applicant appears to be at low risk of default based on current inputs."
        )
    st.subheader("📌 Key Risk Indicators")

if credit_score < 500:
    st.write("⚠️ Low credit score detected")

if dtir1 > 50:
    st.write("⚠️ High debt-to-income ratio")

if ltv > 80:
    st.write("⚠️ High loan-to-value ratio")
