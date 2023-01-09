# Design a stack that supports push, pop, top, and retrieving the 
# minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack2:
            self.stack2.append(val)
        
        elif self.stack2[-1] < val:
            self.stack2.insert(0, val)

        else:
            self.stack2.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack2[-1]