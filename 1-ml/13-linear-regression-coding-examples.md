## Pre-requisites

1. Install Python 3.x
   Make sure you have Python 3.x installed on your system. If you don't have it, download and install it from the official Python website.

2. Install Required Libraries.
   - scikit-learn: For implementing the Linear Regression model.
   - matplotlib: For plotting the graph to visualize the data and the regression line.

To install these libraries, run the following commands in your terminal:

```
pip3 install scikit-learn
pip3 install matplotlib
```

---

## Example1: Simple House Prediction

📁 **File location**: `./practice/1-linear-regression/test-1`  
▶️ **To Run**: `python3 ./practice/1-linear-regression/test-1/main.py`

Predicts house prices based on the house size. Visualizes the data and the regression line.

---

## Example2: Salary Prediction Using Experience

📁 **File location**: `./practice/1-linear-regression/test-2`  
▶️ **To Run**: `python3 ./practice/1-linear-regression/test-2/main.py`

Predicts salary using experience years as input. Splits data into training and test sets, evaluates with MAE, MAPE, and MSE, and includes a function to predict salary.

---

## Example3: Salary Prediction Using Multiple Inputs

📁 **File location**: `./practice/1-linear-regression/test-3`  
▶️ **To Run**: `python3 ./practice/1-linear-regression/test-3/main.py`

Predicts salary using multiple inputs: Experience, Age, and Education level. Evaluates with MAE, MAPE, and MSE, and includes a prediction function for multiple input values.

### **Problem Statement**:

Predict a person’s salary based on:

- Experience (years)
- Age
- Education Level (integer coded)

Trains a Multiple Linear Regression model and evaluates its performance.

---

### **CSV Data Structure**:

- **Experience**: Years of work experience
- **Age**: Age of the individual
- **Education**: Education level (coded as an integer)
- **Salary**: The salary (target value)
