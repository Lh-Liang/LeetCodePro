#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # Ensures the invariant: len(right) == len(left) or len(right) == len(left) + 1
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        # If left is empty, the only element must be in right
        val = self.left.popleft() if self.left else self.right.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        # For even total length (L==R), the frontmost middle is the last element of the left half
        # For odd total length (R==L+1), the middle is the first element of the right half
        if len(self.left) == len(self.right):
            val = self.left.pop()
        else:
            val = self.right.popleft()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.right.pop()
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