# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack_in = []  
        self.stack_out = []  

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._move_elements()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _move_elements(self) -> None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Usage example:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# print(obj.peek())  # Returns 1
# print(obj.pop())   # Returns 1
# print(obj.empty()) # Returns False
