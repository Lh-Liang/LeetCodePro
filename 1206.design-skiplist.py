#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = ['val', 'next']
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level

class Skiplist:
    def __init__(self):
        self.max_level = 16
        self.head = Node(-1, self.max_level)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * self.max_level
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        lvl = self._random_level()
        if lvl > self.level:
            self.level = lvl
            
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        target_node = curr.next[0]
        if not target_node or target_node.val != num:
            return False
        
        for i in range(len(target_node.next)):
            if update[i].next[i] == target_node:
                update[i].next[i] = target_node.next[i]
        
        while self.level > 0 and self.head.next[self.level - 1] is None:
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