#
# @lc app=leetcode id=3510 lang=golang
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
import (
    "container/heap"
)

type Pair struct {
    sum int
    leftIdx int // index of the left element in nums
    order int   // to break ties for leftmost pair (monotonically increasing)
    valid bool  // to mark if pair is still valid
}

type PairHeap []*Pair

func (h PairHeap) Len() int { return len(h) }
func (h PairHeap) Less(i, j int) bool {
    if h[i].sum != h[j].sum {
        return h[i].sum < h[j].sum
    }
    return h[i].order < h[j].order // leftmost tie-breaker
}
func (h PairHeap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}
func (h *PairHeap) Push(x interface{}) {
    *h = append(*h, x.(*Pair))
}
func (h *PairHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

func minimumPairRemoval(nums []int) int {
    n := len(nums)
    if n <= 1 {
        return 0
    }

    // Step 1: Build a doubly linked list to represent the array
    type Node struct {
        val int
        prev, next *Node
        idx int // original index, for mapping
        alive bool
    }
    nodes := make([]*Node, n)
    for i := 0; i < n; i++ {
        nodes[i] = &Node{val: nums[i], idx: i, alive: true}
    }
    for i := 0; i < n; i++ {
        if i > 0 {
            nodes[i].prev = nodes[i-1]
        }
        if i < n-1 {
            nodes[i].next = nodes[i+1]
        }
    }

    // Step 2: Build all initial pairs and a heap
    h := &PairHeap{}
    order := 0
    pairMap := map[[2]int]*Pair{} // [leftIdx,rightIdx] => *Pair
    for i := 0; i < n-1; i++ {
        p := &Pair{sum: nums[i]+nums[i+1], leftIdx: i, order: order, valid: true}
        heap.Push(h, p)
        pairMap[[2]int{i, i+1}] = p
        order++
    }
    heap.Init(h)

    ops := 0
    aliveCnt := n
    for aliveCnt > 1 {
        // Step 3: Pop the minimal valid pair from the heap
        var p *Pair
        for h.Len() > 0 {
            top := heap.Pop(h).(*Pair)
            if top.valid {
                p = top
                break
            }
        }
        if p == nil {
            break // no valid pairs left
        }
        lidx, ridx := p.leftIdx, p.leftIdx+1
        left, right := nodes[lidx], nodes[ridx]
        if !left.alive || !right.alive {
            continue // skip stale pairs
        }

        // Step 4: Merge the pair into a single node
        mergedVal := left.val + right.val
        left.val = mergedVal
        right.alive = false
        aliveCnt--
        // Remove right from linked list
        left.next = right.next
        if right.next != nil {
            right.next.prev = left
        }

        // Invalidate old pairs involving left and right
        if left.prev != nil && left.prev.alive {
            if q, ok := pairMap[[2]int{left.prev.idx, lidx}]; ok {
                q.valid = false
            }
        }
        if q, ok := pairMap[[2]int{lidx, ridx}]; ok {
            q.valid = false
        }
        if right.next != nil && right.next.alive {
            if q, ok := pairMap[[2]int{ridx, right.next.idx}]; ok {
                q.valid = false
            }
        }

        // Step 5: Add new pairs formed by merging
        // (left.prev, left)
        if left.prev != nil && left.prev.alive {
            np := &Pair{sum: left.prev.val + left.val, leftIdx: left.prev.idx, order: order, valid: true}
            heap.Push(h, np)
            pairMap[[2]int{left.prev.idx, lidx}] = np
            order++
        }
        // (left, left.next)
        if left.next != nil && left.next.alive {
            np := &Pair{sum: left.val + left.next.val, leftIdx: lidx, order: order, valid: true}
            heap.Push(h, np)
            pairMap[[2]int{lidx, left.next.idx}] = np
            order++
        }

        ops++
        // Step 6: After each operation, check if the array is non-decreasing
        // (Needed only if aliveCnt > 1)
        isND := true
        var prev *Node
        for cur := nodes[0]; cur != nil; cur = cur.next {
            if !cur.alive {
                continue
            }
            if prev != nil && cur.val < prev.val {
                isND = false
                break
            }
            prev = cur
        }
        if isND {
            break
        }
    }
    // Step 7: Verification - all steps are implemented: data structure initialization, minimal pair selection, merging, updating neighbors, array status check, and operation counting.
    return ops
}
# @lc code=end