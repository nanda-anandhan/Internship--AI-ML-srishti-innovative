import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Title
st.title("🌸 Iris Flower Prediction")

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# User Input
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

# Prediction
prediction = model.predict([
    [sepal_length, sepal_width, petal_length, petal_width]
])

# Display Result
st.success(f"Prediction: {iris.target_names[prediction][0]}")

