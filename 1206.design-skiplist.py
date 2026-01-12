import random

#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level

class Skiplist:

    def __init__(self):
        self.max_level = 16
        self.head = Node(-1, self.max_level)

    def _random_level(self) -> int:
        lvl = 1
        while lvl < self.max_level and random.random() < 0.5:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
            if curr.next[i] and curr.next[i].val == target:
                return True
        return False

    def add(self, num: int) -> None:
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        lvl = self._random_level()
        node = Node(num, lvl)
        for i in range(lvl):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        node = update[0].next[0]
        if not node or node.val != num:
            return False
        
        for i in range(len(node.next)):
            update[i].next[i] = node.next[i]
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end