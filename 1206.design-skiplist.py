#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
# @lc code=start
import random

class SkiplistNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)

class Skiplist:
    def __init__(self):
        self.MAX_LEVEL = 16
        self.P = 0.5
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        self.level = 0

    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [None] * (self.MAX_LEVEL + 1)
        curr = self.head
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lvl = self.randomLevel()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl
        node = SkiplistNode(num, lvl)
        for i in range(lvl + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def erase(self, num: int) -> bool:
        update = [None] * (self.MAX_LEVEL + 1)
        curr = self.head
        found = False
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr and curr.val == num:
            found = True
            for i in range(self.level + 1):
                if update[i].forward[i] != curr:
                    continue
                update[i].forward[i] = curr.forward[i]
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end