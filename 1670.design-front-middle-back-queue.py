#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # Invariant: len(left) == len(right) or len(left) + 1 == len(right)
        self.left = deque()
        self.right = deque()

    def _balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        # Balance not strictly needed here if logic is precise, 
        # but calling it ensures invariant safety.
        self._balance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.right:
            return -1
        if not self.left:
            res = self.right.popleft()
        else:
            res = self.left.popleft()
        self._balance()
        return res

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            res = self.left.pop()
        else:
            res = self.right.popleft()
        self._balance()
        return res

    def popBack(self) -> int:
        if not self.right:
            return -1
        res = self.right.pop()
        self._balance()
        return res

# @lc code=end