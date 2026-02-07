#
# @lc app=leetcode id=1206 lang=golang
#
# [1206] Design Skiplist
#

# @lc code=start
type Node struct {
    val int
    forward []*Node // pointers to next nodes in different levels
}

type Skiplist struct {
    head *Node // starting point of the skip list
    maxLevel int
}

func Constructor() Skiplist {
    return Skiplist{
        head: &Node{forward: make([]*Node, 16)}, // assume max level is 16 for simplicity
        maxLevel: 16,
    }
}

func (this *Skiplist) Search(target int) bool {
    curr := this.head
    for i := this.maxLevel - 1; i >= 0; i-- {
        // Move forward while next node value is less than target
        for curr.forward[i] != nil && curr.forward[i].val < target {
            curr = curr.forward[i]
        }
    }
    curr = curr.forward[0]
    return curr != nil && curr.val == target
}

func (this *Skiplist) Add(num int) {
    update := make([]*Node, this.maxLevel)
    curr := this.head
    for i := this.maxLevel - 1; i >= 0; i-- {
        for curr.forward[i] != nil && curr.forward[i].val < num {
            curr = curr.forward[i]
        }
        update[i] = curr // track nodes that need to be updated at each level
    }
    level := randomLevel(this.maxLevel)
    newNode := &Node{val: num, forward: make([]*Node, level)}
    for i := 0; i < level; i++ {
        newNode.forward[i] = update[i].forward[i]
        update[i].forward[i] = newNode
    }
}

func (this *Skiplist) Erase(num int) bool {
    update := make([]*Node, this.maxLevel)
    found := false
    curr := this.head
    for i := this.maxLevel - 1; i >= 0; i-- {
        for curr.forward[i] != nil && curr.forward[i].val < num {
            curr = curr.forward[i]
        }
        update[i] = curr
    }
    curr = curr.forward[0]
    if curr != nil && curr.val == num {
        found = true
        for i := 0; i < len(curr.forward); i++ {if update[i].forward[i] == curr {update[i].forward[i] =curr.forward[\u001b}returnfound}returnfalse}	funcrandomLevel(maxLevellintint{	level:=1	forlevel<maxLevellrand.Float32()<0.5{level++}returnlevel}