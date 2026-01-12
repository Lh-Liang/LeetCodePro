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
        # Initialize with a dummy head node for the top-most level
        self.head = Node(-1)

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            # Move right as long as the next node's value is less than target
            while curr.right and curr.right.val < target:
                curr = curr.right
            # If target found at current level, return True
            if curr.right and curr.right.val == target:
                return True
            # Move down to search in the lower level
            curr = curr.down
        return False

    def add(self, num: int) -> None:
        path = []
        curr = self.head
        # Traverse and record the path of nodes where we move down
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            path.append(curr)
            curr = curr.down
        
        insert = True
        down_ptr = None
        # Insert at the current level and potentially promote to higher levels
        while insert and path:
            prev = path.pop()
            prev.right = Node(num, prev.right, down_ptr)
            down_ptr = prev.right
            # Probability 0.5 to promote to the next level
            insert = (random.random() < 0.5)
        
        # If promotion continues beyond existing levels, create a new top level
        if insert:
            self.head = Node(-1, Node(num, None, down_ptr), self.head)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            # Move right as long as the next node's value is less than num
            while curr.right and curr.right.val < num:
                curr = curr.right
            # If num found at current level, remove it and mark as found
            if curr.right and curr.right.val == num:
                found = True
                curr.right = curr.right.right
            # Move down to continue removal in lower levels
            curr = curr.down
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end