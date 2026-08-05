import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict value
x_new = np.array([[6]])
prediction = model.predict(x_new)

# Print results
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for x = 6:", prediction[0])