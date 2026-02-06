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
        return self.queue.pop(0) if self.queue else -1
    
    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        mid = (len(self.queue) - 1) // 2
        return self.queue.pop(mid)
    
    def popBack(self) -> int:
        return self.queue.pop() if self.queue else -1