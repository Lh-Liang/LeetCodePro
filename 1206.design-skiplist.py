#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    def __init__(self, val: int):
        self.val = val
        self.forward = None

class Skiplist:

    def __init__(self):
        self.MAXLVL = 16
        self.head = Node(-1)
        self.head.forward = [None] * self.MAXLVL

    def randomLevel(self):
        level = 1
        while random.random() < 0.5 and level < self.MAXLVL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        curr = self.head
        for lvl in range(self.MAXLVL - 1, -1, -1):
            while curr.forward[lvl] is not None and curr.forward[lvl].val < target:
                curr = curr.forward[lvl]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        level = self.randomLevel()
        new_node = Node(num)
        new_node.forward = [None] * self.MAXLVL
        pred = [None] * self.MAXLVL
        curr = self.head
        for i in range(self.MAXLVL - 1, -1, -1):
            while curr.forward[i] is not None and curr.forward[i].val < num:
                curr = curr.forward[i]
            pred[i] = curr
        for i in range(level):
            new_node.forward[i] = pred[i].forward[i]
            pred[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        pred = [None] * self.MAXLVL
        curr = self.head
        for i in range(self.MAXLVL - 1, -1, -1):
            while curr.forward[i] is not None and curr.forward[i].val < num:
                curr = curr.forward[i]
            pred[i] = curr
        node = pred[0].forward[0]
        if node is None or node.val != num:
            return False
        for i in range(self.MAXLVL):
            if pred[i].forward[i] == node:
                pred[i].forward[i] = node.forward[i]
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end