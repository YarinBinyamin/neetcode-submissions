class MyStack:

    def __init__(self):
        self.the_stack = []
        self.helper_queue = []
        

    def push(self, x: int) -> None:
        while self.the_stack:
            self.helper_queue.append(self.the_stack.pop(0))
        self.the_stack.append(x)
        while self.helper_queue:
            self.the_stack.append(self.helper_queue.pop(0))
        

    def pop(self) -> int:
        return self.the_stack.pop(0)
        

    def top(self) -> int:
        return self.the_stack[0]

    def empty(self) -> bool:
        if self.the_stack:
            return False
        return True
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()