# @lc app=leetcode id=1206 lang=python3
class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

import random
class Skiplist:
    def __init__(self):
        self.max_level = 16
        self.head = Node(-1, self.max_level)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl
    
    def search(self, target: int) -> bool:
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < target:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == target

    def add(self, num: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < num:
                current = current.forward[i]
            update[i] = current
        
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl
        
        new_node = Node(num, lvl)
        for i in range(lvl + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def erase(self, num: int) -> bool:
        update = [None] * (self.max_level + 1)
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < num:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]
        if not (current is not None and current.value == num):
            return False
        
        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]
            
        while self.level > 0 and not self.head.forward[self.level]:
            self.level -= 1
            
        return True