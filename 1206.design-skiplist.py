#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    def __init__(self, val=None, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))  # Top-level head sentinel node.
        self.levels = 0  # Initial number of levels is zero.
    
    def search(self, target: int) -> bool:
        current = self.head
        while current:
            while current.right and current.right.val < target:
                current = current.right
            if current.right and current.right.val == target:
                return True  # Found target.
            current = current.down  # Move to next lower level.
        return False  # Target not found.
    
    def add(self, num: int) -> None:
        nodes_to_update = []  # Nodes that need links updated at each level.
        current = self.head
        while current:
            while current.right and current.right.val < num:
                current = current.right
            nodes_to_update.append(current)  # Potential insert points.
            current = current.down  # Move downwards.
        # Insert new nodes at appropriate levels based on random decision.
        insert_level = 0  # Start from base level (0).
        new_node_below = None  # New nodes below this one.
        while insert_level == 0 or (insert_level < len(nodes_to_update) and random.random() < 0.5):
            if insert_level >= len(nodes_to_update):
                new_head_top = Node(float('-inf'), down=self.head)
                self.head = new_head_top
                nodes_to_update.append(new_head_top)
                self.levels += 1
            prev_node = nodes_to_update[-(insert_level+1)]
            new_node = Node(num, prev_node.right, new_node_below)
            prev_node.right = new_node
            new_node_below = new_node  # Link vertically downward.
            insert_level += 1
    
    def erase(self, num: int) -> bool:
        success = False
        current = self.head
        while current:
            while current.right and current.right.val < num:
                current = current.right
            if current.right and current.right.val == num:
                success = True  # Found target for removal.
                current.right = current.right.right  # Remove node horizontally.
            current = current.down  # Move downward in list.
        return success  # Return whether any removal occurred.