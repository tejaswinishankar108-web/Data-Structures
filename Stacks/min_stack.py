"""MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack."""

##O(1) time complexity for all operations and O(n) space complexity for the stack.
class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.min_s or val <= self.min_s[-1]:
            self.min_s.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.min_s[-1]:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]