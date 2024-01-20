class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # Push the value to the stack and the min_stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stack[-1] if self.stack else val)
        self.min_stack.append(val)
    
    # Pop the value from the stack and the min_stack
    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)
    
    # Return the top value of the stack    
    def top(self) -> int:
        return self.stack[-1]
    
    # Return the top value of the min_stack
    def getMin(self) -> int:
        return self.min_stack[-1]