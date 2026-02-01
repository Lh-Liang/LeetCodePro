#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = 'val', 'right', 'down'
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:

    def __init__(self):
        # Initialize with a single dummy head representing the top level.
        self.head = Node()

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            # Move right as long as the next value is smaller than target
            while curr.right and curr.right.val < target:
                curr = curr.right
            # If found, return True
            if curr.right and curr.right.val == target:
                return True
            # Move down to search in the next level
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        # Track the nodes before the insertion point at each level
        stack = []
        curr = self.head
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            stack.append(curr)
            curr = curr.down
        
        insert = True
        down_node = None
        # Insert levels from bottom up based on random choice
        while insert and stack:
            prev = stack.pop()
            prev.right = Node(num, prev.right, down_node)
            down_node = prev.right
            insert = (random.random() < 0.5)
        
        # If we still need to insert after reaching the top, add a new level
        if insert:
            self.head = Node(-1, Node(num, None, down_node), self.head)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            # Move right as long as the next value is smaller than num
            while curr.right and curr.right.val < num:
                curr = curr.right
            # If num is found at this level, remove the first occurrence
            if curr.right and curr.right.val == num:
                found = True
                curr.right = curr.right.right
                # Note: Continue moving down to remove the rest of the tower
            curr = curr.down
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end