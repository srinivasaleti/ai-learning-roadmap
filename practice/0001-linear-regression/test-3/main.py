# Problem Statement:
# -------------------
# This script demonstrates how to predict a person's salary based on multiple factors:
# - Years of Experience
# - Age
# - Education Level (coded as a number)
#
# We are using Multiple Linear Regression to predict the salary. The script:
# 1. Loads salary data from a CSV file.
# 2. Splits the data into training and testing datasets.
# 3. Trains a Linear Regression model on the training data.
# 4. Predicts salary using the trained model for test data.
# 5. Evaluates model performance using common metrics (MAE, MSE).
# 6. Visualizes the relationship between actual vs predicted salary.
# 7. Predicts salary for new inputs (Experience, Age, Education).
#
# This example shows how multiple independent variables (features) can be used to
# predict a dependent variable (salary) using linear regression.

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import os

# Step 1: Load data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'salary_data.csv')
    df = pd.read_csv(file_path)
    X = df[['Experience', 'Age', 'Education']]  # multiple input features
    y = df['Salary']  # output
    return X, y

# Step 2: Train model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Step 3: Predict salary
def predict_salary(model, experience, age, education):
    salary = model.predict([[experience, age, education]])
    return salary[0]

# Step 4: Plot actual vs predicted
def plot_results(y_test, y_pred):
    plt.scatter(y_test, y_pred, color='purple')
    plt.xlabel('Actual Salary')
    plt.ylabel('Predicted Salary')
    plt.title('Actual vs Predicted Salary (Multi-Input Linear Regression)')
    plt.grid(True)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # diagonal
    plt.show()

# Run the full flow
X, y = load_data()
model, X_test, y_test = train_model(X, y)
y_pred = model.predict(X_test)

print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Plot
plot_results(y_test, y_pred)

# Predict new salary
exp = 5
age = 28
edu = 3
predicted_salary = predict_salary(model, exp, age, edu)
print(f"\nPredicted salary for {exp} yrs exp, age {age}, edu level {edu}: ₹{predicted_salary:.2f}")
