class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        days = 1
        if not self.stack:
            self.stack.append((price,days))
            return 1
        else:
            while self.stack and self.stack[-1][0] <= price:    
                top_stack = self.stack.pop()
                pre_price, pre_days = top_stack
                days+=pre_days
            self.stack.append((price,days))
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)