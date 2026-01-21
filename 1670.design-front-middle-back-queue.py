#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        # We split the queue into two halves to handle middle operations efficiently.
        # Invariant: len(right) == len(left) or len(right) == len(left) + 1
        self.left = deque()
        self.right = deque()

    def _balance(self):
        # Ensure the invariant: len(right) is either equal to len(left) or len(left) + 1.
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None: 
        self.left.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) == len(self.right):
            # [1, 2] [3, 4] -> middle index is 4 // 2 = 2. 
            # Adding to right's front puts it at index 2.
            self.right.appendleft(val)
        else:
            # [1, 2] [3, 4, 5] -> middle index is 5 // 2 = 2.
            # Adding to left's back puts it at index 2.
            self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.left and not self.right:
            return -1
        if not self.left:
            res = self.right.popleft()
        else:
            res = self.left.popleft()
        self._balance()
        return res

    def popMiddle(self) -> int:
        if not self.left and not self.right:
            return -1
        if len(self.left) == len(self.right):
            # [1, 2] [3, 4] -> removal index is (4-1)//2 = 1. 
            # Index 1 is the back of left.
            res = self.left.pop()
        else:
            # [1, 2] [3, 4, 5] -> removal index is (5-1)//2 = 2.
            # Index 2 is the front of right.
            res = self.right.popleft()
        self._balance()
        return res

    def popBack(self) -> int:
        if not self.left and not self.right:
            return -1
        res = self.right.pop()
        self._balance()
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