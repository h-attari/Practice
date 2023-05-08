class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        temp_stack = [self.stack.pop(-1) for _ in range(len(self.stack))]
        element = temp_stack.pop(-1)
        self.stack = [temp_stack.pop(-1) for _ in range(len(temp_stack))]
        return element
        

    def peek(self) -> int:
        temp_stack = [self.stack.pop(-1) for _ in range(len(self.stack))]
        element = temp_stack[-1]
        self.stack = [temp_stack.pop(-1) for _ in range(len(temp_stack))]
        return element
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()