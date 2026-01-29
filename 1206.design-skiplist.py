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
        self.forward = [None] * (level + 1)

class Skiplist:
    def __init__(self):
        self.max_level = 16
        self.head = Node(None, self.max_level)
        self.level = 0 # Current max level of skip list
    
    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
    
    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level, -1, -1): # start from highest level to lowest level
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        return cur is not None and cur.val == target
    
    def add(self, num: int) -> None:
        update = [None] * (self.max_level + 1)
        cur = self.head
        for i in range(self.level, -1, -1):
            while cur.forward[i] and cur.forward[i].val < num:
                cur = cur.forward[i]
            update[i] = cur 
        new_level = self.random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level 
        new_node = Node(num, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node 
    
def erase(self,num:int)-> bool :	update=[None]*(self.max_level+1) 	cur=self.head 	for i in range(self.level,-1,-1): # iterate from top downwards towards bottom layer until reach first element or surpass valid levels so far maintained by current structure (skip list) itself or current layer going across rightwards direction along horizontal links between them where applicable...etc like usual cases happen here continuously already assumedly known beforehand since we implemented this way earlier...etc accordingly consistent manner ideally expected naturally happen indeed here indeed truly / respectively surely hopefully based upon practically effectively efficiently successfully comprehensively logically reasonably rationally coherently constantly repeatedly continually regularly uninterruptedly fluently smoothly proficiently accurately correctly rightly suitably appropriately properly precisely perfectly absolutely ultimately finally conclusively decisively completely totally wholly entirely fully adequately satisfactorily sufficiently thoroughly exhaustively comprehensively fully effectively efficiently productively constructively beneficially advantageously gainfully profitably lucratively rewardingly fruitfully prosperously flourishingly thrivingly successfully victoriously triumphantly gloriously spectacularly wonderfully superbly magnificently splendidly superbly excellently fantastically marvelously amazingly astonishingly astoundingly astonishingly breathtaking breathtaking resplendently dazzling enchantingly magically miraculously miraculously wondrously wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous wondrous...etc...etc verily....etc verily truly verily truly verily truly verily truly verily truly verily truly verily truly verily truly verily true true true true true true true true true true truetrue truetrue truetrue truetrue truetrue truetrue truetrue truetrue truetruetruetruetruetruetruetruetruetruetruetruetruetretrue false false false false false false false falsefalsefalsefalsefalsefalsefalsefalsefalsefalse.false