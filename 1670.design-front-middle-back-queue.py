#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
class FrontMiddleBackQueue:
    def __init__(self):
        self.front = []
        self.back = []

    def pushFront(self, val: int) -> None:
        self.front.append(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.insert(0, self.front.pop())
        self.front.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if not self.front:
            return self.back.pop(0)
        return self.front.pop()
    
def popMiddle(self) -> int:
def popBack(self) -> int:
def _balance(self): # Internal method to balance front and back lists 
def _balance(self):