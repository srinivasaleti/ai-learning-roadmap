import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

# Step 1: Load the data
def load_data():
    url = 'https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv'
    data = pd.read_csv(url)
    X = data[['Experience Years']]  # input
    y = data['Salary']              # output
    return X, y

# Step 2: Train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=2529)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_train, X_test, y_train, y_test

# Step 3: Predict and show results
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print(f"\nModel Formula: Salary = {model.intercept_:.2f} + ({model.coef_[0]:.2f} × Experience)")
    
    print("\n--- Error Metrics ---")
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("Mean Absolute Percentage Error:", mean_absolute_percentage_error(y_test, y_pred))
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

    return y_pred

# Step 4: Plot the result
def plot_results(X_train, y_train, X_test, y_test, y_pred, model):
    plt.figure(figsize=(8, 6))

    # Plot actual data
    plt.scatter(X_train, y_train, color='blue', label='Train Data')
    plt.scatter(X_test, y_test, color='green', label='Test Data')

    # Plot best fit line
    x_line = pd.concat([X_train, X_test])
    y_line = model.predict(x_line)
    plt.plot(x_line, y_line, color='red', label='Best Fit Line')

    plt.xlabel('Experience (Years)')
    plt.ylabel('Salary')
    plt.title('Experience vs Salary - Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 5: Predict salary for new experience
def predict_salary(model, experience):
    predicted_salary = model.predict([[experience]])
    print(f"\nPredicted salary for {experience} years of experience: ₹{predicted_salary[0]:.2f}")

# Step 6: Run all steps
def main():
    X, y = load_data()
    model, X_train, X_test, y_train, y_test = train_model(X, y)
    y_pred = evaluate_model(model, X_test, y_test)
        
    # Predict for a given experience (change this as needed)
    predict_salary(model, 5)
    plot_results(X_train, y_train, X_test, y_test, y_pred, model)


if __name__ == "__main__":
    main()
