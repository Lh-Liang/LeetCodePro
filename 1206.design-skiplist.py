#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    def __init__(self, val=None, level=0):
        self.val = val
        self.next = [None] * (level + 1)

class Skiplist:
    def __init__(self):
        self.head = Node(-1, 16) # Using 16 levels as an arbitrary choice for max levels.
        self.levels = 0 # Current maximum level in skip list.
    
    def random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < len(self.head.next) - 1:
            lvl += 1
        return lvl
    
    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.levels, -1, -1): # Start from top level down to base level.
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr is not None and curr.val == target
    
    def add(self, num: int) -> None:
        update = [None] * (len(self.head.next)) # To store nodes that need to update their forward pointers.
        curr = self.head
        for i in range(self.levels, -1, -1): # Traverse from top to bottom level.
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr # Remember this position to update pointers later.
        level = self.random_level() # Determine random level for new node insertion.
        if level > self.levels: # If new node has higher level than current list level.
            for i in range(self.levels + 1, level + 1): # Update levels beyond current list levels.
                update[i] = self.head # New highest nodes should point back to head node initially.
            self.levels = level # Update skiplist's known maximum levels count. 
        new_node = Node(num, level) # Create a new node with determined random height/levels.
        for i in range(level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
    
    def erase(self, num: int) -> bool:
        update = [None] * (len(self.head.next))
        curr = self.head
        found = False
        for i in range(self.levels, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        if curr.next[0] and curr.next[0].val == num:
            found = True
            for i in range(len(curr.next)):												   			   	     	   	   	     	   	       	   	       	   	   	       	     	   	         	     	                if update[i].next[i] and update[i].next[i].val == num:                 update[i].next[i] = update[i].next[i].next[i]         while self.levels > 0 and not self.head.next[self.levels]:             self.levels -= 1         return found# @lc code=end