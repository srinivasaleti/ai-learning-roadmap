import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Function to train the model
def train(X, y):
    # Initialize the model
    model = LinearRegression()
    model.fit(X, y)  # Train the model on X and y
    return model

# Function to predict price for a given size
def predict(model, size):
    predicted_price = model.predict([[size]])  # Predict price for the given size
    return predicted_price[0]

# Function to plot the data and best fit line
def plot(x_line, y, model):
    # Generate values for the line (to make a smooth curve)
    y_line = model.predict(x_line)

    # Plot actual data points
    plt.scatter([x[0] for x in x_line], y, color='blue', label='Actual Data')

    # Plot the best fit line
    plt.plot([x[0] for x in x_line], y_line, color='red', label='Best Fit Line')

    # Labels and title
    plt.xlabel('Size of House (sq ft)')
    plt.ylabel('Price (lakhs)')
    plt.title('Linear Regression: House Price Prediction')
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

# Hardcoded training data
X = [[600], [800], [1000], [1200], [1400], [1600]]  # Size of the house in sq ft
y = [30, 40, 50, 60, 70, 100]  # Price of the house in lakhs

# Step 1: Train the model
model = train(X, y)

# Step 2: Predict price for a given size (e.g., 1100 sq ft)
size_to_predict = 1100
predicted_price = predict(model, size_to_predict)
print(f"Predicted price for {size_to_predict} sq ft house is ₹{predicted_price:.2f} lakhs")

# Step 3: Plot the graph with the trained model
plot(X, y, model)
