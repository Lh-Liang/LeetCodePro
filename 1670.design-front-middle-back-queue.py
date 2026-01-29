#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # Invariant: len(left) == len(right) OR len(right) == len(left) + 1
        self.left = deque()
        self.right = deque()

    def _rebalance(self):
        # Case 1: Left is too long
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        # Case 2: Right is too long (more than 1 greater than left)
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            # Adding to right keeps it at len(left) + 1
            self.right.appendleft(val)
        else:
            # Right was len(left) + 1, adding to left makes them equal
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.right:
            return -1
        if not self.left:
            res = self.right.popleft()
        else:
            res = self.left.popleft()
        self._rebalance()
        return res

    def popMiddle(self) -> int:
        if not self.right:
            return -1
        if len(self.left) == len(self.right):
            # Even size: [1, 2 | 3, 4] -> middle is 2 (frontmost)
            res = self.left.pop()
        else:
            # Odd size: [1, 2 | 3, 4, 5] -> middle is 3
            res = self.right.popleft()
        self._rebalance()
        return res

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