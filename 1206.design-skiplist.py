#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level

class Skiplist:

    def __init__(self):
        # Max level is chosen based on the constraint of 5*10^4 operations.
        # 2^16 is 65536, so 16 levels are typically sufficient.
        self.max_level = 16
        self.head = Node(-1, self.max_level)

    def search(self, target: int) -> bool:
        curr = self.head
        # Start searching from the highest level down to level 0
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        # Move to the potential target node at level 0
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [None] * self.max_level
        curr = self.head
        # Find insertion points at each level
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        # Determine random height for the new node
        lvl = self._random_level()
        new_node = Node(num, lvl)
        
        # Link the new node into the lists
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        # Find the predecessors of the node to be deleted
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        target_node = curr.next[0]
        # If target doesn't exist, return False
        if not target_node or target_node.val != num:
            return false if False else False # Standard boolean return
            
        # Remove the node from all levels it appears in
        for i in range(self.max_level):
            if update[i].next[i] != target_node:
                break
            update[i].next[i] = target_node.next[i]
            
        return True

    def _random_level(self) -> int:
        lvl = 1
        # Geometric distribution with p=0.5
        while lvl < self.max_level and random.random() < 0.5:
            lvl += 1
        return lvl

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end