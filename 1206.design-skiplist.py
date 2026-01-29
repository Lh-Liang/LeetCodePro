#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    __slots__ = 'val', 'next'
    def __init__(self, val, levels):
        self.val = val
        # next[i] stores the pointer to the next node at level i
        self.next = [None] * levels

class Skiplist:

    def __init__(self):
        self.max_level = 16
        # Dummy head node with value -1 (less than any possible input)
        self.head = Node(-1, self.max_level)

    def search(self, target: int) -> bool:
        curr = self.head
        # Traverse from top level down to level 0
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        # Check if the node at level 0 is the target
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        # update[i] will store the rightmost node at level i with value < num
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        # Randomly determine the height of the new node
        lvl = 1
        while lvl < self.max_level and random.random() < 0.5:
            lvl += 1
            
        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        # Find the predecessors of the node to be removed
        update = [None] * self.max_level
        curr = self.head
        for i in range(self.max_level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        
        # target_node is the first node with value >= num at level 0
        target_node = curr.next[0]
        if not target_node or target_node.val != num:
            return False
        
        # Remove the node from all levels it belongs to
        for i in range(len(target_node.next)):
            if update[i].next[i] == target_node:
                update[i].next[i] = target_node.next[i]
        
        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end