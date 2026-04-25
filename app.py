import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
@st.cache_data

def load_data():
    df = pd.read_csv("HR_job_prediction_cleaned.csv")
    return df


df = load_data()

# --------------------------------------------------
# Dashboard Title
# --------------------------------------------------
st.title("📊 HR Job Acceptance Prediction Dashboard")
st.markdown("### Key Performance Indicators (KPIs)")

# --------------------------------------------------
# KPI Calculations
# --------------------------------------------------

# Total Candidates
total_candidates = len(df)

# Placement Rate
placement_rate = (df['status'] == 1).mean() * 100

# Job Acceptance Rate
job_acceptance_rate = (df['status'] == 1).mean() * 100

# Average Interview Score
avg_interview_score = df['interview_score'].mean()

# Average Skills Match %
avg_skills_match = df['skills_match_percentage'].mean()

# Offer Dropout Rate
# Example logic:
# Candidate selected but low relocation willingness
offer_dropout_rate = (
    (df['status'] == 1) &
    (df['relocation_willingness'] == 0)
).mean() * 100

# High-Risk Candidate Percentage
# Example logic:
# Low interview score OR employment gap
high_risk_candidates = (
    (df['interview_score'] < 60) |
    (df['employment_gap_months'] > 12)
).mean() * 100

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👨‍💼 Total Candidates", total_candidates)

with col2:
    st.metric("✅ Placement Rate", f"{placement_rate:.2f}%")

with col3:
    st.metric("📌 Job Acceptance Rate", f"{job_acceptance_rate:.2f}%")


col4, col5, col6 = st.columns(3)

with col4:
    st.metric("🎤 Avg Interview Score", f"{avg_interview_score:.2f}")

with col5:
    st.metric("🧠 Avg Skills Match", f"{avg_skills_match:.2f}%")

with col6:
    st.metric("⚠️ Offer Dropout Rate", f"{offer_dropout_rate:.2f}%")


col7, col8 = st.columns(2)

with col7:
    st.metric("🚨 High-Risk Candidates", f"{high_risk_candidates:.2f}%")

