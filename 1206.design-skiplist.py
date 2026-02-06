#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
import random

class Node:
    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)

class Skiplist:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.header = Node(-1, self.MAX_LEVEL)
        self.level = 0

def random_level(self):
    lvl = 0
    while random.random() < self.P and lvl < self.MAX_LEVEL:
        lvl += 1
    return lvl
def search(self, target: int) -> bool:
    current = self.header
    for i in range(self.level, -1, -1): # Start from highest level of skip list
        while current.forward[i] and current.forward[i].value < target:
            current = current.forward[i]
    current = current.forward[0]
def add(self, num: int) -> None:
def erase(self, num: int) -> bool:
def skip_list = Skiplist()