class StockSpanner:

    def __init__(self):
        # Each entry is (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # Collapse previous days with price <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        # Push current day
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)