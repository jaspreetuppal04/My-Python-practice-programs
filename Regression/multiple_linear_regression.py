import numpy as np

# Two input variables: X1 and X2
X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

# Output variable
Y = np.array([5, 8, 11, 14, 17])

# Initially set all weights and intercept to 0
w1 = 0
w2 = 0
b = 0

# Learning rate
lr = 0.01

# Number of iterations
epochs = 1000

# Number of data points
n = len(X)

# Gradient Descent
for i in range(epochs):

    # Prediction formula:
    # Y = w1*X1 + w2*X2 + b
    Y_pred = w1 * X[:, 0] + w2 * X[:, 1] + b

    # Gradient for w1
    dw1 = (-2/n) * np.sum(X[:, 0] * (Y - Y_pred))

    # Gradient for w2
    dw2 = (-2/n) * np.sum(X[:, 1] * (Y - Y_pred))

    # Gradient for intercept
    db = (-2/n) * np.sum(Y - Y_pred)

    # Update w1
    w1 = w1 - lr * dw1

    # Update w2
    w2 = w2 - lr * dw2

    # Update intercept
    b = b - lr * db

# Final trained values
print("w1:", w1)
print("w2:", w2)
print("Intercept:", b)

# New input values
x1 = 6
x2 = 7

# Make prediction using trained values
prediction = w1*x1 + w2*x2 + b

print("Prediction:", prediction)