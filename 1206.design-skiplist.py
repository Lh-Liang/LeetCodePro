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
        self.max_level = 16
        self.head = Node(-1, self.max_level)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * self.max_level
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        
        lvl = self._random_level()
        if lvl > self.level:
            self.level = lvl
        
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [self.head] * self.max_level
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        
        curr = curr.forward[0]
        if not curr or curr.val != num:
            return False
        
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]
        
        while self.level > 0 and not self.head.forward[self.level - 1]:
            self.level -= 1
        return True

    def _random_level(self):
        lvl = 1
        while lvl < self.max_level and random.random() < 0.5:
            lvl += 1
        return lvl

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end