#
# @lc app=leetcode id=1206 lang=golang
#
# [1206] Design Skiplist
#

# @lc code=start
import (
    "math/rand"
    "time"
)

const (
    maxLevel = 16
    p = 0.25
)

type Node struct {
    val int
    forward []*Node
}

type Skiplist struct {
    head *Node
    level int
}

func Constructor() Skiplist {
    rand.Seed(time.Now().UnixNano())
    head := &Node{val: -1, forward: make([]*Node, maxLevel)}
    return Skiplist{head: head, level: 1}
}

func randomLevel() int {
    lvl := 1
    for lvl < maxLevel && rand.Float64() < p {
        lvl++
    }
    return lvl
}

func (this *Skiplist) Search(target int) bool {
    curr := this.head
    for i := this.level - 1; i >= 0; i-- {
        for curr.forward[i] != nil && curr.forward[i].val < target {
            curr = curr.forward[i]
        }
    }
    curr = curr.forward[0]
    return curr != nil && curr.val == target
}

func (this *Skiplist) Add(num int) {
    update := make([]*Node, maxLevel)
    curr := this.head
    for i := this.level - 1; i >= 0; i-- {
        for curr.forward[i] != nil && curr.forward[i].val < num {
            curr = curr.forward[i]
        }
        update[i] = curr
    }
    lvl := randomLevel()
    if lvl > this.level {
        for i := this.level; i < lvl; i++ {
            update[i] = this.head
        }
        this.level = lvl
    }
    node := &Node{val: num, forward: make([]*Node, lvl)}
    for i := 0; i < lvl; i++ {
        node.forward[i] = update[i].forward[i]
        update[i].forward[i] = node
    }
}

func (this *Skiplist) Erase(num int) bool {
    update := make([]*Node, maxLevel)
    curr := this.head
    found := false
    for i := this.level - 1; i >= 0; i-- {
        for curr.forward[i] != nil && curr.forward[i].val < num {
            curr = curr.forward[i]
        }
        update[i] = curr
    }
    curr = curr.forward[0]
    if curr != nil && curr.val == num {
        found = true
        for i := 0; i < this.level; i++ {
            if update[i].forward[i] != curr {
                break
            }
            update[i].forward[i] = curr.forward[i]
        }
        for this.level > 1 && this.head.forward[this.level-1] == nil {
            this.level--
        }
    }
    return found
}

# @lc code=end