class MinStack:

    def __init__(self):
        self.st = []
        self.sm = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.sm or val <= self.sm[-1]:
            self.sm.append(val)

    def pop(self) -> None:
        if self.st.pop() == self.sm[-1]:
            self.sm.pop()

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.sm[-1]
