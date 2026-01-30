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
        # Maintain the invariant: len(self.left) == len(self.right) or len(self.left) == len(self.right)+1
        while len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        while len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
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
            res = self.left.popleft()
        else:
            res = self.right.popleft()
        self.rebalance()
        return res

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        res = self.left.pop()
        self.rebalance()
        return res

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        if self.right:
            res = self.right.pop()
        else:
            res = self.left.pop()
        self.rebalance()
        return res
# @lc code=end