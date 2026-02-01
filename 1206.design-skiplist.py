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
        # Head is a sentinel node for the top-most level
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
        nodes_to_update = []
        curr = self.head
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            nodes_to_update.append(curr)
            curr = curr.down

        insert = True
        down_node = None
        while insert and nodes_to_update:
            curr = nodes_to_update.pop()
            curr.right = Node(num, curr.right, down_node)
            down_node = curr.right
            insert = random.getrandbits(1) == 0

        if insert:
            self.head = Node(-1, Node(num, None, down_node), self.head)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            if curr.right and curr.right.val == num:
                found = True
                curr.right = curr.right.right
            curr = curr.down
        return found

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end