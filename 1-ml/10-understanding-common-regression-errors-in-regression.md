### Understanding Common Evaluation Metrics in Regression Models

#### 1. **Mean Absolute Error (MAE)**

- **What it is:**  
  MAE measures the average of the absolute differences between the predicted values and the actual values. It tells us how far off the predictions are from the actual values, without considering whether the errors are positive or negative.
  
- **Interpretation:**  
  - Lower MAE means the model’s predictions are closer to the actual values.
  - Higher MAE means the model's predictions are off by a larger amount.

---

#### 2. **Mean Absolute Percentage Error (MAPE)**

- **What it is:**  
  MAPE calculates the average absolute percentage difference between the predicted values and actual values. It tells us how much error there is in the predictions compared to the actual values, expressed as a percentage.
  
- **Interpretation:**  
  - MAPE is useful when we want to see how much error we have in percentage terms.
  - If the MAPE is lower, it means the model is making good predictions.
  - If MAPE is high, the model's predictions are far from the actual values.

---

#### 3. **Mean Squared Error (MSE)**

- **What it is:**  
  MSE calculates the average of the squared differences between the predicted values and actual values. This error measurement gives more weight to large errors (because errors are squared), meaning it heavily penalizes predictions that are far from the actual values.
  
- **Interpretation:**  
  - Lower MSE means the model is doing well in predicting the values.
  - Higher MSE indicates that the model’s predictions are not close to the actual values.
  - Since MSE squares the errors, it can be more sensitive to outliers compared to MAE.

---

### **Summary of Differences:**

- **MAE** gives the **average error** in the same units as the data.
- **MAPE** expresses error as a **percentage**, useful when comparing models on different scales.
- **MSE** penalizes **larger errors** more than smaller ones and is sensitive to outliers.
