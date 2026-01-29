#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = 'val', 'forward'
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * level

class Skiplist:

    def __init__(self):
        self.MAX_LEVEL = 16
        self.P = 0.5
        self.head = Node(-1, self.MAX_LEVEL)

    def _random_level(self) -> int:
        lvl = 1
        while lvl < self.MAX_LEVEL and random.random() < self.P:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [None] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        
        lvl = self._random_level()
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.MAX_LEVEL - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        
        curr = curr.forward[0]
        if not curr or curr.val != num:
            return False
        
        for i in range(len(curr.forward)):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end