#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#

# @lc code=start
class SkiplistNode:
    def __init__(self, val=0, level=1):
        self.val = val
        self.forward = [None] * level
        self.level = level

class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(-1) # Head node with dummy value -1
        self.max_level = 16 # Maximum possible level in skiplist
        self.p_factor = 0.5 # Probability factor for level generation
    
    def random_level(self):
        lvl = 1
        while random.random() < self.p_factor and lvl < self.max_level:
            lvl += 1
        return lvl
    
    def search(self, target: int) -> bool:
        current = self.head
        for i in range(self.max_level-1, -1, -1): # Start from topmost level
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.val == target
    
    def add(self, num: int) -> None:
        update = [None] * self.max_level
        current = self.head
        for i in range(self.max_level-1, -1, -1): # Start from topmost level for addition path traversal
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current # Keep track of nodes where update is needed upon insertion
        lvl = self.random_level() # Determine the level of new node randomly using p_factor probability distribution function. 
nnew_node = SkiplistNode(num,lvl) # Create new node based on generated levels 
nfor i in range(lvl): # Insert new node into skip list at each determined levels 
nnew_node.forward[i] = update[i].forward[i] 
nupdate[i].forward[i] = new_node 
n  
n def erase(self,num:int)->bool: # This function removes element from skip list if it exists otherwise returns false without any change made by traversing through all levels until reaching desired element position along with updating its references appropriately 
nupdate=[None]*self.max_level;current=self.head;found=False;for i in range(self.max_level-1,-1,-1):while(current.forward[i]!=None and current.forward[i].val<num):current=current.forward[i];update[i]=current;if(current.forward[0]!=None and current.forward[0].val==num):found=True;for j in range(len(current.forward[0].forward)):if(update[j].forward[j]==current.forward[0]):update[j].forward[j]=current.forward[0].forward[j];return found;return False;