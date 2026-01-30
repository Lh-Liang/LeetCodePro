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
        self.next = [None] * level

class Skiplist:

    def __init__(self):
        self.max_level = 16
        self.prob = 0.5
        self.head = Node(-1, self.max_level)
        self.level = 1

    def random_level(self):
        lvl = 1
        while random.random() < self.prob and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        node = self.head
        for i in reversed(range(self.level)):
            while node.next[i] and node.next[i].val < target:
                node = node.next[i]
        node = node.next[0]
        return node is not None and node.val == target

    def add(self, num: int) -> None:
        update = [None] * self.max_level
        node = self.head
        for i in reversed(range(self.level)):
            while node.next[i] and node.next[i].val < num:
                node = node.next[i]
            update[i] = node
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        node = self.head
        found = False
        for i in reversed(range(self.level)):
            while node.next[i] and node.next[i].val < num:
                node = node.next[i]
            update[i] = node
        node = node.next[0]
        if node and node.val == num:
            found = True
            for i in range(self.level):
                if update[i].next[i] != node:
                    continue
                update[i].next[i] = node.next[i]
            # Decrease level if needed
            while self.level > 1 and self.head.next[self.level - 1] is None:
                self.level -= 1
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end