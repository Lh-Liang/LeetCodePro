#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

import random

# @lc code=start
class Node:
    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)

class Skiplist:
    def __init__(self):
        self.head = Node(-1) # Sentinel node with negative infinity value
        self.max_level = 16 # Maximum number of levels in this skip list
        self.level = 0 # Current highest level initialized to 0
    
    def random_level(self):
        lvl = 1
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl
    
    def search(self, target: int) -> bool:
        current = self.head
        for i in range(self.level, -1, -1): # Traverse from highest level to base level
            while current.forward[i] and current.forward[i].value < target:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == target
    
    def add(self, num: int) -> None:
        updates = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1): # Find position to insert new node
            while current.forward[i] and current.forward[i].value < num:
                current = current.forward[i]
            updates[i] = current # Keep track of paths where we drop down a level
        
        level_for_new_node = self.random_level()
        if level_for_new_node > self.level: # New node has more levels than currently exist in list
            for i in range(self.level + 1, level_for_new_node):
                updates[i] = self.head
            self.level = level_for_new_node # Update the list's max level if needed
        
        new_node = Node(num, level_for_new_node)
        for i in range(level_for_new_node): # Insert new node into its positions on all levels up to its height.
            new_node.forward[i] = updates[i].forward[i]
            updates[i].forward[i] = new_node   
    
    def erase(self, num: int) -> bool:
        updates = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1): # Find nodes that need their forward pointers updated or reset at each relevant layer.
            while current.forward[i] and current.forward[i].value < num:
                current = current.forward[i]
            updates[i] = current 
       
       target_found_flag=False
       possible_target=current.forward[0] # Check first layer only after descending through all layers available ensuring no higher layer contains matching target already found.
       if possible_target and possible_target.value==num:
           target_found_flag=True
           for i in range(len(possible_target.forward)):# Remove links from update chain effectively removing specified node completely from structure.
               updates[i].forward[i]=possible_target.forward[i]
           del possible_target
       return target_found_flag
# @lc code=end