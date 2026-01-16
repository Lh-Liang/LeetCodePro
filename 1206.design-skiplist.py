#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
import random

# @lc code=start
class Node:
    def __init__(self, val, levels):
        self.val = val
        # Array to hold forward pointers for each level
        self.forward = [None] * levels

class Skiplist:
    def __init__(self):
        self.max_levels = 16
        self.probability = 0.5
        # Create head node with value -1 (smaller than any possible input)
        self.head = Node(-1, self.max_levels)
    
    def _random_level(self):
        """Generate random level for a new node"""
        level = 1
        while random.random() < self.probability and level < self.max_levels:
            level += 1
        return level
    
    def search(self, target: int) -> bool:
        current = self.head
        
        # Start from highest level and work down
        for level in range(self.max_levels - 1, -1, -1):
            # Move forward while next node is smaller than target
            while current.forward[level] and current.forward[level].val < target:
                current = current.forward[level]
        
        # Move to the next node at base level
        current = current.forward[0]
        
        # Check if we found the target
        return current and current.val == target
    
    def add(self, num: int) -> None:
        # Array to store predecessors at each level
        update = [None] * self.max_levels
        current = self.head
        
        # Find the position to insert at each level
        for level in range(self.max_levels - 1, -1, -1):
            while current.forward[level] and current.forward[level].val < num:
                current = current.forward[level]
            update[level] = current
        
        # Create new node with random level
        new_level = self._random_level()
        new_node = Node(num, new_level)
        
        # Insert the new node at each of its levels
        for level in range(new_level):
            new_node.forward[level] = update[level].forward[level]
            update[level].forward[level] = new_node
    
    def erase(self, num: int) -> bool:
        # Array to store predecessors at each level
        update = [None] * self.max_levels
        current = self.head
        
        # Find the node to delete at each level
        for level in range(self.max_levels - 1, -1, -1):
            while current.forward[level] and current.forward[level].val < num:
                current = current.forward[level]
            update[level] = current
        
        # Move to the node to delete (if it exists)
        current = current.forward[0]
        
        # If node doesn't exist or value doesn't match, return False
        if not current or current.val != num:
            return False
        
        # Remove the node from all levels where it appears
        for level in range(len(current.forward)):
            update[level].forward[level] = current.forward[level]
        
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end