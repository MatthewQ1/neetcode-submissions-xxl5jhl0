class MinStack:

    def __init__(self):
        self.stack = [] # tuples of (val, min at the moment)

        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            tup = (val, min(val, self.stack[-1][1]))
            self.stack.append(tup)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
