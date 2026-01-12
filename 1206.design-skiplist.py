#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = 'val', 'right', 'down'
    def __init__(self, val, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:

    def __init__(self):
        # Initialize with a sentinel head node
        self.head = Node(-1)

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            # Move right as much as possible at the current level
            while curr.right and curr.right.val < target:
                curr = curr.right
            # If target found in current level express lane
            if curr.right and curr.right.val == target:
                return True
            # Move down to search in the next level
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        stack = []
        curr = self.head
        # Find insertion points at each level
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            stack.append(curr)
            curr = curr.down
        
        down_node = None
        should_add = True
        # Insert the node and decide levels via coin flip
        while should_add:
            if stack:
                prev = stack.pop()
                prev.right = Node(num, prev.right, down_node)
                down_node = prev.right
            else:
                # If we need a new level above current maximum
                self.head = Node(-1, Node(num, None, down_node), self.head)
                down_node = self.head.right
            # 50% chance to go up one more level
            should_add = (random.random() < 0.5)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            # Find the node just before the target value
            while curr.right and curr.right.val < num:
                curr = curr.right
            if curr.right and curr.right.val == num:
                # Found the value, remove the node at this level
                found = True
                curr.right = curr.right.right
                # Move down to remove the same tower at lower levels
            curr = curr.down
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end