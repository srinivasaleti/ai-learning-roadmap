## Types of Logistic Regression

Logistic Regression can be classified into three main types based on the nature of the target variable. These types are:

### 1. **Binary Logistic Regression**

- **Definition**: In **Binary Logistic Regression**, the target variable has only two possible categories. This is the most common form of logistic regression.
- **Target Variable**: Two categories (binary outcome).
- **Examples**:
  - **Spam vs. Non-Spam**: Predicting whether an email is spam or not (Yes/No).
  - **Pass or Fail**: Predicting whether a student passes or fails an exam (Pass/Fail).
  - **True or False**: Predicting whether a statement is true or false (True/False).
---

### 2. **Multinomial Logistic Regression**

- **Definition**: **Multinomial Logistic Regression** is used when the target variable has three or more categories that are not ordered. These categories are **nominal**, meaning they don't have any specific rank or order.
- **Target Variable**: Three or more categories with no inherent order.
- **Examples**:

  - **Fruit Types**: Predicting the type of fruit (Apple, Mango, Orange, Banana) based on features like color and size.
  - **Car Brands**: Predicting the brand of a car (Ford, Honda, BMW) based on car specifications.
  - **Political Parties**: Predicting which political party a person would vote for (Democrat, Republican, Independent).

- **Formula**: Multinomial Logistic Regression uses the **softmax** function to predict the probabilities for each class.

---

### 3. **Ordinal Logistic Regression**

- **Definition**: **Ordinal Logistic Regression** is used when the target variable has three or more categories with a natural order. These categories are **ordinal**, meaning they have a specific ranking or order, but the distances between the categories may not be equal.
- **Target Variable**: Three or more categories with an inherent order (ranked).
- **Examples**:
  - **Student Performance**: Categorizing students' performance as **Poor**, **Average**, **Good**, and **Excellent**.
  - **Survey Ratings**: Customer satisfaction ratings like **Very Unsatisfied**, **Unsatisfied**, **Neutral**, **Satisfied**, **Very Satisfied**.
  - **Health Status**: Classifying a person’s health as **Very Poor**, **Poor**, **Fair**, **Good**, and **Excellent**.
- **Formula**: Ordinal logistic regression uses a **cumulative logit model** to predict the odds of being in a higher category versus a lower one.

---

### Summary Table

| Type                                | Target Variable         | Number of Categories | Order of Categories | Example                             |
| ----------------------------------- | ----------------------- | -------------------- | ------------------- | ----------------------------------- |
| **Binary Logistic Regression**      | 2 categories (binary)   | 2                    | No                  | Spam/Non-Spam, Pass/Fail            |
| **Multinomial Logistic Regression** | 3+ categories (nominal) | 3 or more            | No                  | Fruit type (Apple, Mango, Orange)   |
| **Ordinal Logistic Regression**     | 3+ categories (ordinal) | 3 or more            | Yes (ordered)       | Student performance (Poor, Average) |

---
