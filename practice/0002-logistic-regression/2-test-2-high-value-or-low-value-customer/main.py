"""
Problem Statement:
-------------------

This script demonstrates how to classify customers as either **High Value** or **Low Value** based on their historical data. The dataset contains features related to customer behavior and demographics.

We are using **Logistic Regression** to predict the customer value classification. The script will:

1. Load the customer data from a CSV file.
2. Split the data into training and testing datasets.
3. Train a Logistic Regression model on the training data.
4. Predict the customer classification (High Value = 1, Low Value = 0) using the trained model on test data.
5. Evaluate the model performance using accuracy, precision, recall, and F1-score.
6. Visualize the distribution of the predicted values.
7. Predict the classification for a new customer based on their features.

Features used in the dataset:
- **Age**: Age of the customer (years).
- **Annual Income**: The income of the customer (in dollars).
- **Spending Score**: A score assigned based on the customer's spending habits (0-100).
- **Gender**: Whether the customer is Male or Female (encoded as 0 for Male and 1 for Female).
- **Number of Purchases**: Total number of purchases made by the customer in the past year.
  
### Dataset:
The dataset is available in the CSV file `customer_data.csv` and contains the following columns:
- **Age**: The age of the customer (numeric value).
- **Annual_Income**: The customer's income in dollars (numeric value).
- **Spending_Score**: A score representing customer spending habits (numeric value from 0 to 100).
- **Gender**: Coded as 0 for Male and 1 for Female (categorical).
- **Number_of_Purchases**: Total number of purchases made (numeric value).
- **Customer_Value**: The classification target variable. 0 for **Low Value** and 1 for **High Value** customer.

### Example:
Sample dataset (customer_data.csv):

| Age | Annual_Income | Spending_Score | Gender | Number_of_Purchases | Customer_Value |
|-----|---------------|----------------|--------|----------------------|----------------|
| 22  | 30000         | 50             | 1      | 10                   | 0              |
| 35  | 45000         | 60             | 0      | 20                   | 1              |
| 45  | 60000         | 30             | 0      | 15                   | 0              |
| 50  | 70000         | 80             | 1      | 25                   | 1              |
| 28  | 35000         | 55             | 1      | 12                   | 0              |

### Your Task:
1. Preprocess the data by handling any missing values and encoding categorical variables.
2. Split the dataset into training and testing sets.
3. Train a **Logistic Regression** model to classify customers into **High Value** or **Low Value**.
4. Evaluate the model's performance using accuracy, precision, recall, and F1-score.
5. Predict the classification for a new customer based on the following features:
   - Age = 30, Annual_Income = 45000, Spending_Score = 70, Gender = 0 (Male), Number_of_Purchases = 18
"""

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
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import os
import numpy as np
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

# Step 1: Load data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'data.csv')
    df = pd.read_csv(file_path)
    X = df[['Age', 'Annual_Income', 'Spending_Score', 'Gender', 'Number_of_Purchases']] 
    y = df['Label']
    return X, y

# Step 2: Train model

def train_model(X, y):
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, train_size=0.7, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model, scaler, X_test, y_test

def predict_new_input(model, scaler, age, annual_income, spending_score, gender, number_of_purchages):
    new_data = pd.DataFrame([[age, annual_income, spending_score, gender, number_of_purchages]],
                            columns=['Age', 'Annual_Income', 'Spending_Score', 'Gender', 'Number_of_Purchases'])
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)
    return "Valued" if prediction[0] == 1 else "Not Valued"
    
# Run the full flow
X, y = load_data()
model, scaler, X_test, y_test = train_model(X, y)
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


# Input values
age = 40
annual_income = 146538
spending_score = 10
gender = 1  # 1 for Male, 0 for Female
number_of_purchases = 22
predicted_label = predict_new_input(model, scaler, age, annual_income, spending_score, gender, number_of_purchases)

# Convert gender to text
gender_text = "Male" if gender == 1 else "Female"

print(f"The customer with Age {age}, Income ₹{annual_income}, Spending Score {spending_score}, Gender {gender_text}, and {number_of_purchases} purchases is predicted to be a **{predicted_label}** customer.")
