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

    def rebalance(self):
        # Maintain the invariant: len(self.left) >= len(self.right) and at most 1 more
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        # Place in left so that 'frontmost' middle is at end of left
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self.rebalance()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.left:
            val = self.left.popleft()
        else:
            val = self.right.popleft()
        self.rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        val = self.left.pop()
        self.rebalance()
        return val

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.right:
            val = self.right.pop()
        else:
            val = self.left.pop()
        self.rebalance()
        return val

# @lc code=end