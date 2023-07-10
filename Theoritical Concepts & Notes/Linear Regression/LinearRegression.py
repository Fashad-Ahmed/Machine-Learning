import numpy as np
from sklearn.metrics import mean_squared_error

class LinearRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.coefficients = None

    def fit(self, X, y):
        m, n = X.shape
        self.coefficients = np.zeros(n)

        for _ in range(self.num_iterations):
            predictions = np.dot(X, self.coefficients)
            error = predictions - y
            gradient = (1 / m) * np.dot(X.T, error)
            self.coefficients -= self.learning_rate * gradient

    def predict(self, X):
        return np.dot(X, self.coefficients)

# Example usage
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
