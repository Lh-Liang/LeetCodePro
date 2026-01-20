#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # Two deques to manage the front and back halves of the queue.
        # Invariant: len(left) == len(right) or len(left) == len(right) + 1
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # Maintain the invariant len(left) >= len(right)
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        # Maintain the invariant len(left) <= len(right) + 1
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        # If left has more elements, move the last of left to right 
        # to make space for the new middle in left.
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        # No explicit balance needed here as we manually adjusted, 
        # but _balance() wouldn't hurt.

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        
        # Usually pop from left, but if left is empty (implies right is empty due to invariant),
        # handled by check above. 
        val = self.left.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        
        # The middle element is always at the back of self.left 
        # because len(left) >= len(right).
        val = self.left.pop()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        
        if self.right:
            val = self.right.pop()
        else:
            # If right is empty, left must have exactly 1 element (invariant)
            val = self.left.pop()
        
        self._balance()
        return val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end