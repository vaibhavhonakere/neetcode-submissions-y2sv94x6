import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)
        weights = initial_weights
        for n in range(num_iterations):
            pred = self.get_model_prediction(X, weights)
            # square = np.square(pred - Y)
            # error = np.mean(square)
            d1 = self.get_derivative(pred, Y, len(X), X, 0)
            d2 = self.get_derivative(pred, Y, len(X), X, 1)
            d3 = self.get_derivative(pred, Y, len(X), X, 2)
            weights[0] -= self.learning_rate * d1
            weights[1] -= self.learning_rate * d2
            weights[2] -= self.learning_rate * d3
        return np.round(weights,5)
        
        