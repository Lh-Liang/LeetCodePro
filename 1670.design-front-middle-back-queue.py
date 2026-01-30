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
        self.queue.insert(len(self.queue) // 2, val) 
    def pushBack(self, val: int) -> None: 
        self.queue.append(val) 
    def popFront(self) -> int: 
        return self.queue.pop(0) if self.queue else -1 
    def popMiddle(self) -> int: 
        return self.queue.pop((len(self.queue) - 1) // 2) if self.queue else -1 
    def popBack(self) -> int: 
        return self.queue.pop() if self.queue else -1 
# Your FrontMiddleBackQueue object will be instantiated and called as such:
o = FrontMiddleBackQueue() o.pushFront(val)o.pushMiddle(val)o.pushBack(val)param_4 = o.popFront()param_5 = o.popMiddle()param_6 = o.popBack() # @lc code=end 