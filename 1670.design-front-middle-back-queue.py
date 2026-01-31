#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # Invariant: len(self.right) - len(self.left) is 0 or 1
        self.left = deque()
        self.right = deque()

    def _rebalance(self):
        # Ensure len(self.right) - len(self.left) is 0 or 1
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)
        # pushMiddle logic naturally maintains the invariant

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.right:
            return -1
        if not self.left:
            return self.right.popleft()
        res = self.left.popleft()
        self._rebalance()
        return res

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            return self.left.pop()
        else:
            return self.right.popleft()
        # popMiddle logic naturally maintains the invariant

    def popBack(self) -> int:
        if not self.right:
            return -1
        res = self.right.pop()
        self._rebalance()
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