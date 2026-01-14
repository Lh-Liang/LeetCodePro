#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
import random

# @lc code=start
class Skiplist:
    class Node:
        def __init__(self, val, levels):
            self.val = val
            self.next = [None] * levels
    
    def __init__(self):
        self.max_level = 16  # reasonable max level
        self.p = 0.5  # probability for promoting a node to next level
        self.head = self.Node(-1, self.max_level)
        self.levels = 1  # current number of levels
    
    def _random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level
    
    def search(self, target: int) -> bool:
        current = self.head
        # Start from the top level and move down
        for i in range(self.levels - 1, -1, -1):
            # Move right while the next node exists and its value is less than target
            while current.next[i] and current.next[i].val < target:
                current = current.next[i]
        # Check if the next node at level 0 has the target value
        return current.next[0] and current.next[0].val == target
    
    def add(self, num: int) -> None:
        # Array to keep track of the nodes at each level where we need to insert
        update = [self.head] * self.max_level
        current = self.head
        
        # Find the insertion point at each level
        for i in range(self.levels - 1, -1, -1):
            while current.next[i] and current.next[i].val < num:
                current = current.next[i]
            update[i] = current
        
        # Generate a random level for the new node
        new_level = self._random_level()
        
        # Update the current number of levels if needed
        if new_level > self.levels:
            for i in range(self.levels, new_level):
                update[i] = self.head
            self.levels = new_level
        
        # Create the new node
        new_node = self.Node(num, new_level)
        
        # Insert the new node at each level
        for i in range(new_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
    
    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        current = self.head
        
        # Find the node to delete at each level
        for i in range(self.levels - 1, -1, -1):
            while current.next[i] and current.next[i].val < num:
                current = current.next[i]
            update[i] = current
        
        # The node to be deleted is at level 0
        target_node = current.next[0]
        
        # If the target node doesn't exist or doesn't match the value, return False
        if not target_node or target_node.val != num:
            return False
        
        # Remove the node from each level
        for i in range(self.levels):
            if update[i].next[i] != target_node:
                break
            update[i].next[i] = target_node.next[i]
        
        # Remove empty top levels
        while self.levels > 1 and self.head.next[self.levels - 1] is None:
            self.levels -= 1
        
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end