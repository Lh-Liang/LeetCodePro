#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _rebalance(self):
        # Ensure the size invariant: len(front) == len(back) or len(front) == len(back) + 1
        while len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        while len(self.front) < len(self.back):
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._rebalance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        val = self.front.pop()
        self._rebalance()
        return val

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self._rebalance()
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