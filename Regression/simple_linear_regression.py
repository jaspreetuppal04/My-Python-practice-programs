import numpy as np

# Input data (independent variable)
X = np.array([1, 2, 3, 4, 5])

# Output data (dependent variable)
Y = np.array([2, 4, 6, 8, 10])

m = 0 #slope
c = 0 #intercept

# Learning rate controls how big each update is
alpha = 0.01

# Number of times we update m and c
epochs = 1000

# Number of data points
n = len(X)

# Gradient Descent
for i in range(epochs):

    # Calculate predicted Y using: Y = mX + c
    Y_pred = m * X + c

    # Calculate gradient of m (slope)
    dm = (-2/n) * np.sum(X * (Y - Y_pred))

    # Calculate gradient of c (intercept)
    dc = (-2/n) * np.sum(Y - Y_pred)

    # Update slope
    m = m - alpha * dm

    # Update intercept
    c = c - alpha * dc

# Final values after training
print("Slope:", m)
print("Intercept:", c)

# Predict Y when X = 6
x = 6
prediction = m * x + c

print("Prediction:", prediction)