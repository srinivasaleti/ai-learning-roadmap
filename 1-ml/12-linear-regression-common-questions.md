# 📚 Linear Regression - Common Questions

---

## 🔰 Basic Level

### 1. What is Linear Regression?

- It is a way to find a straight line that best fits the data.
- Used to predict a value (like price, marks) using another value (like size, experience).

---

### 2. What are independent and dependent variables?

- **Independent variable** = input (like `Experience`)
- **Dependent variable** = output (like `Salary`)

---

### 3. What is the formula for linear regression?

- For one input:  
  `y = mx + c`  
  (m = slope, c = intercept)

---

### 4. What is the line of best fit?

- A line that goes through most of the points with the least error.

---

### 5. What is intercept and slope?

- **Intercept** = where the line crosses y-axis (when x = 0)
- **Slope** = how steep the line is

---

### 6. What is the use of `train_test_split()`?

- It splits the data:
  - Some for training
  - Some for testing

---

### 7. What is overfitting and underfitting?

- **Overfitting** = model learns too much, performs bad on new data
- **Underfitting** = model learns too little, bad on both training and test data

---

### 8. What are MAE, MAPE, MSE?

- **MAE**: average of all absolute errors
- **MAPE**: error in percentage
- **MSE**: square of errors, gives more weight to big errors

---

### 9. Can Linear Regression work with multiple inputs?

- ✅ Yes. This is called **Multiple Linear Regression**

---

### 10. Can Linear Regression work with multiple outputs?

- ✅ Yes. This is called **Multi-output Regression**

---

## 🧠 Intermediate Level

### 11. How do we measure how good the model is?

- Using `R² Score` (closer to 1 is better)

---

### 12. What if the data is not in a straight line?

- Linear regression won't work well
- We can try **Polynomial Regression** instead

---

### 13. Can Linear Regression work with text data?

- ❌ No, only with numbers
- But we can convert text to numbers using encoding

---

### 14. What are assumptions in linear regression?

1. Linearity
2. No multicollinearity (inputs should not be strongly related)
3. Homoscedasticity (equal spread of errors)
4. No auto-correlation
5. Normal distribution of errors

---

### 15. Can we use it for classification problems?

- ❌ No, it's used only for prediction (continuous output)
- For classification, use **Logistic Regression**

---

## 💡 Advanced Level

### 16. What happens if input variables are related to each other?

- This is called **multicollinearity**
- It can confuse the model

---

### 17. What is the difference between Simple and Multiple Linear Regression?

| Type                       | Input       | Output   |
| -------------------------- | ----------- | -------- |
| Simple Linear Regression   | 1 input     | 1 output |
| Multiple Linear Regression | Many inputs | 1 output |

---

### 18. Can we regularize linear regression?

- ✅ Yes. Use:
  - **Ridge Regression** (L2)
  - **Lasso Regression** (L1)

---

### 19. How does scikit-learn train the model?

- It uses math to find the best values for slope and intercept using **least squares method**

---

### 20. What are some real-life use cases?

- Predicting house prices
- Estimating salary based on experience
- Forecasting sales
- Predicting marks from study hours

---
