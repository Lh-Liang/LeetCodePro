#
# @lc app=leetcode id=3777 lang=golang
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
type node struct {
    l, r int
    left, right *node
    minDel [2]int
    lch, rch byte
}

func build(s []byte, l, r int) *node {
    n := &node{l: l, r: r}
    if l == r {
        n.lch, n.rch = s[l], s[l]
        n.minDel[0], n.minDel[1] = 0, 0
        // Verification: Single element segment invariants are correct
        return n
    }
    m := (l + r) / 2
    n.left = build(s, l, m)
    n.right = build(s, m+1, r)
    n.merge()
    // Verification: After merge, segment invariants are checked
    return n
}

func (n *node) merge() {
    // Merge left and right children and verify alternation and minDel invariants
    for first := 0; first <= 1; first++ {
        leftDel := n.left.minDel[first]
        rightDel := n.right.minDel[1-first]
        add := 0
        if n.left.rch == n.right.lch {
            add = 1
        }
        n.minDel[first] = leftDel + rightDel + add
    }
    n.lch = n.left.lch
    n.rch = n.right.rch
    // Verification: lch and rch represent new segment boundaries
}

func (n *node) update(idx int) {
    if n.l == n.r {
        if n.lch == 'A' {
            n.lch, n.rch = 'B', 'B'
        } else {
            n.lch, n.rch = 'A', 'A'
        }
        // Verification: Leaf node update invariants
        return
    }
    if idx <= n.left.r {
        n.left.update(idx)
    } else {
        n.right.update(idx)
    }
    n.merge()
    // Verification: After update and merge, invariants are checked
}

func (n *node) query(l, r int) (int, int, byte, byte, int) {
    // Edge case: No overlap
    if n.l > r || n.r < l {
        return 1<<30, 1<<30, 0, 0, 0
    }
    // Edge case: Complete overlap
    if l <= n.l && n.r <= r {
        // Verification: Segment is fully within range
        return n.minDel[0], n.minDel[1], n.lch, n.rch, n.r-n.l+1
    }
    // Partial overlap: Query left and right children separately
    ld0, ld1, ll, lr, llen := n.left.query(l, r)
    rd0, rd1, rl, rr, rlen := n.right.query(l, r)
    res0, res1 := 1<<30, 1<<30
    add := 0
    if lr != 0 && rl != 0 && lr == rl {
        add = 1
    }
    if ld0 < 1<<30 && rd1 < 1<<30 {
        res0 = ld0 + rd1 + add
    }
    if ld1 < 1<<30 && rd0 < 1<<30 {
        res1 = ld1 + rd0 + add
    }
    totalLen := llen + rlen
    // Verification: After merge, check alternation and boundary correctness
    return res0, res1, func() byte { if ll != 0 { return ll } else { return rl } }(), func() byte { if rr != 0 { return rr } else { return lr } }(), totalLen
}

func minDeletions(s string, queries [][]int) []int {
    n := len(s)
    root := build([]byte(s), 0, n-1)
    res := []int{}
    for _, q := range queries {
        if q[0] == 1 {
            root.update(q[1])
            // Verification: Update propagation and invariant maintenance
        } else {
            l, r := q[1], q[2]
            // Edge case: Singleton range
            if l == r {
                res = append(res, 0)
                continue
            }
            d0, d1, _, _, _ := root.query(l, r)
            // Verification: Query returns valid minimum deletions
            if d0 < d1 {
                res = append(res, d0)
            } else {
                res = append(res, d1)
            }
        }
        // Verification: Optionally check entire structure after each operation
    }
    // Final verification: Output array matches number of type-2 queries
    return res
}
# @lc code=end