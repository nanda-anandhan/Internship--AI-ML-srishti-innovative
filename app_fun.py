import streamlit as st
import pandas as pd
import numpy as np

# =========================
# Title
# =========================
st.title("🌟 My First Streamlit App")

st.header("Welcome")
st.write("This app demonstrates basic Streamlit features.")

st.markdown("### Enter Your Details")

# =========================
# Text Input
# =========================
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}! Welcome to Streamlit.")

# =========================
# Button
# =========================
if st.button("Click Me"):
    st.write("🎉 Button Clicked!")

# =========================
# Checkbox
# =========================
agree = st.checkbox("I agree")

if agree:
    st.write("✅ Thank you for agreeing.")

# =========================
# Radio Button
# =========================
gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

st.write("Selected:", gender)

# =========================
# Select Box
# =========================
course = st.selectbox(
    "Choose Your Course",
    ["BSc", "MSc", "BTech", "MTech"]
)

st.write("Course:", course)

# =========================
# Slider
# =========================
age = st.slider("Select your age", 18, 60, 22)

st.write("Age:", age)

# =========================
# DataFrame
# =========================
st.header("Random Data")

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)

st.dataframe(df)

# =========================
# Charts
# =========================
st.header("Charts")

st.line_chart(df)

st.bar_chart(df)

# =========================
# File Upload
# =========================
st.header("Upload CSV File")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# =========================
# Sidebar
# =========================
st.sidebar.title("Sidebar")

username = st.sidebar.text_input("Username")

if username:
    st.sidebar.success(f"Hello {username}")

# =========================
# Columns
# =========================
st.header("Columns")

col1, col2 = st.columns(2)

with col1:
    st.info("This is Column 1")

with col2:
    st.warning("This is Column 2")