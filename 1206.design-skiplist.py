#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    def __init__(self, val, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:

    def __init__(self):
        # Initialize with a sentinel head node. 
        # Since values are >= 0, -1 is a safe sentinel value.
        self.head = Node(-1)

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.right and curr.right.val < target:
                curr = curr.right
            if curr.right and curr.right.val == target:
                return True
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        # Keep track of the 'path' where we transitioned down levels
        path = []
        curr = self.head
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            path.append(curr)
            curr = curr.down
        
        insert_up = True
        down_node = None
        
        while insert_up:
            if path:
                prev = path.pop()
                prev.right = Node(num, prev.right, down_node)
                down_node = prev.right
            else:
                # If path is empty but we still need to insert up, create a new level
                new_node = Node(num, None, down_node)
                self.head = Node(-1, new_node, self.head)
                down_node = new_node
            
            # Probabilistically decide to add another level (50% chance)
            insert_up = (random.random() < 0.5)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            if curr.right and curr.right.val == num:
                found = True
                # Remove the node at this level and continue to the level below
                curr.right = curr.right.right
            curr = curr.down
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end