"""
# Problem Statement:
# -------------------
# This script demonstrates how to classify animals as either a **Cat** or a **Dog** based on their physical attributes:
# - Weight (in kilograms)
# - Height (in centimeters)
#
# We are using **Logistic Regression** to classify animals. The script:
# 1. Loads animal data (Weight, Height) from a CSV file.
# 2. Splits the data into training and testing datasets.
# 3. Trains a Logistic Regression model on the training data.
# 4. Predicts the label (Cat = 0, Dog = 1) using the trained model on test data.
# 5. Evaluates model performance using accuracy.
# 6. Visualizes the decision boundary between Cats and Dogs.
# 7. Predicts the label for a new animal based on its weight and height.
#
# This example shows how a binary classification problem can be solved using **Logistic Regression** with two independent variables (Weight and Height) to predict a dependent variable (Cat or Dog).
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import os
import numpy as np

# Step 1: Load data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data.csv')
    df = pd.read_csv(file_path)
    X = df[['Weight', 'Height']] 
    y = df['Label']
    return X, y

# Step 2: Train model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Step 3: Predict for a new input
def predict_new_input(model, weight, height):
    new_data = pd.DataFrame([[weight, height]], columns=['Weight', 'Height'])
    prediction = model.predict(new_data)
    if prediction == 0:
        return "Cat"
    else:
        return "Dog"
    
# Run the full flow
X, y = load_data()
model, X_test, y_test = train_model(X, y)
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

new_weight = 15.0  # Example: 5.0 kg
new_height = 30.0  # Example: 30.0 cm

predicted_label = predict_new_input(model, new_weight, new_height)
print(f"Predicted label for a new animal with weight {new_weight} kg and height {new_height} cm is: {predicted_label}")