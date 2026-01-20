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
        # Array of pointers to next nodes at different levels
        self.forward = [None] * level

class Skiplist:

    def __init__(self):
        self.MAX_LEVEL = 16
        self.P = 0.5
        # Head is a dummy node with a value less than any valid input
        # or we just handle it logically. 
        # Using -1 as dummy value since constraints say 0 <= num.
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        self.level = 0  # Current highest level in the skiplist

    def random_level(self):
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        current = self.head
        # Start from the highest level and move down
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]
        
        # Move to the next node at level 0, which should be the target
        current = current.forward[0]
        
        return current is not None and current.val == target

    def add(self, num: int) -> None:
        update = [None] * self.MAX_LEVEL
        current = self.head
        
        # Find the place to insert
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
            
        lvl = self.random_level()
        
        # If the new level is higher than current skiplist level,
        # initialize update array for the new levels to head
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
            
        # Create new node
        new_node = SkiplistNode(num, lvl)
        
        # Insert the node by updating pointers
        for i in range(lvl):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        current = self.head
        
        # Find the node and its predecessors
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current
            
        target_node = current.forward[0]
        
        # If target not found
        if target_node is None or target_node.val != num:
            return False
        
        # Update pointers to skip the target node
        for i in range(self.level):
            if update[i].forward[i] != target_node:
                break
            update[i].forward[i] = target_node.forward[i]
            
        # Update current level of the skiplist if top layers are empty
        while self.level > 0 and self.head.forward[self.level - 1] is None:
            self.level -= 1
            
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end