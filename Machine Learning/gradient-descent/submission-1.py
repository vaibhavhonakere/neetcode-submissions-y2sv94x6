class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        first = init
        for i in range(iterations):
            d = 2 * first
            first -= learning_rate * d
        return round(first,5)
    