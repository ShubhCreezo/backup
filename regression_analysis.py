import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data for regression analysis
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (input)
y = np.array([2, 4, 5, 4, 5])  # Dependent variable (target)

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Make predictions
y_pred = model.predict(x)

# Print the coefficients (slope and intercept)
print("Coefficient (slope):", model.coef_)
print("Intercept:", model.intercept_)

# Print the predicted values
print("Predicted values:", y_pred)
