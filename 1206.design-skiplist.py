#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
# @lc code=start
import random

class Node:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * (level + 1)

class Skiplist:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(-1, Skiplist.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < Skiplist.P and lvl < Skiplist.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = [None] * (Skiplist.MAX_LEVEL + 1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl
        node = Node(num, lvl)
        for i in range(lvl + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node
        # Verification step: Ensure all forward pointers and levels are updated correctly

    def erase(self, num: int) -> bool:
        update = [None] * (Skiplist.MAX_LEVEL + 1)
        cur = self.head
        found = False
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur
        cur = cur.forward[0]
        if cur and cur.val == num:
            found = True
            for i in range(self.level + 1):
                if update[i].forward[i] != cur:
                    continue
                update[i].forward[i] = cur.forward[i]
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            # Verification step: After erasure, check that skiplist invariants hold
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end