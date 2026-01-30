#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

from collections import deque

# @lc code=start
class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _balance(self):
        # Balance the two deques so that back is never bigger than front by more than one element
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if not self.front:
            return self.back.popleft()
        val = self.front.popleft()
        self._balance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        self._balance()
        return val

    def popBack(self) -> int:
        if not self.back and not self.front:
            return -1
        if not self.back:
            return self.front.pop()
        val = self.back.pop()
        self._balance()
        return val
# @lc code=end