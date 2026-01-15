#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
class FrontMiddleBackQueue:
    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.queue) // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(0)

    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        # For odd length, middle index is len//2; for even length, it's len//2 - 1 (frontmost middle)
        mid = (len(self.queue) - 1) // 2
        return self.queue.pop(mid)

    def popBack(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop()
# @lc code=end