#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # We maintain two deques: left and right.
        # Invariant: len(right) is always equal to or one greater than len(left).
        self.left = deque()
        self.right = deque()

    def rebalance(self):
        # Maintain the invariant: 0 <= len(right) - len(left) <= 1
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            self.right.appendleft(val)
        else:
            self.left.append(val)
        # pushMiddle logic naturally maintains balance, but rebalance() is safe.

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.rebalance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if not self.left:
            res = self.right.popleft()
        else:
            res = self.left.popleft()
        self.rebalance()
        return res

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            res = self.left.pop()
        else:
            res = self.right.popleft()
        self.rebalance()
        return res

    def popBack(self) -> int:
        if not self.right:
            return -1
        res = self.right.pop()
        self.rebalance()
        return res


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end