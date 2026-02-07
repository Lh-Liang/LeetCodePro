#
# @lc app=leetcode id=3373 lang=golang
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
    n := len(edges1) + 1
    m := len(edges2) + 1
    // Build adjacency lists
    adj1 := make([][]int, n)
    for _, e := range edges1 {
        a, b := e[0], e[1]
        adj1[a] = append(adj1[a], b)
        adj1[b] = append(adj1[b], a)
    }
    adj2 := make([][]int, m)
    for _, e := range edges2 {
        a, b := e[0], e[1]
        adj2[a] = append(adj2[a], b)
        adj2[b] = append(adj2[b], a)
    }
    // BFS to get depth parity for all nodes in both trees
    depth1 := make([]int, n)
    var bfs1 = func() {
        vis := make([]bool, n)
        queue := []int{0}
        vis[0] = true
        for len(queue) > 0 {
            cur := queue[0]
            queue = queue[1:]
            for _, nei := range adj1[cur] {
                if !vis[nei] {
                    depth1[nei] = depth1[cur] + 1
                    vis[nei] = true
                    queue = append(queue, nei)
                }
            }
        }
    }
    bfs1()
    depth2 := make([]int, m)
    var bfs2 = func() {
        vis := make([]bool, m)
        queue := []int{0}
        vis[0] = true
        for len(queue) > 0 {
            cur := queue[0]
            queue = queue[1:]
            for _, nei := range adj2[cur] {
                if !vis[nei] {
                    depth2[nei] = depth2[cur] + 1
                    vis[nei] = true
                    queue = append(queue, nei)
                }
            }
        }
    }
    bfs2()
    // Count even and odd depths
    even1, odd1 := 0, 0
    for _, d := range depth1 {
        if d%2 == 0 {
            even1++
        } else {
            odd1++
        }
    }
    even2, odd2 := 0, 0
    for _, d := range depth2 {
        if d%2 == 0 {
            even2++
        } else {
            odd2++
        }
    }
    // Sanity check: even + odd should sum to number of nodes for each tree
    if even1+odd1 != n || even2+odd2 != m {
        // handle error or return empty
        return []int{}
    }
    // For each node in tree1, maximize target nodes
    res := make([]int, n)
    for i := 0; i < n; i++ {
        parity := depth1[i] % 2
        // Option 1: connect to a node of same parity in tree2
        cnt1 := 0
        if parity == 0 {
            cnt1 = even1 + even2
        } else {
            cnt1 = odd1 + odd2
        }
        // Option 2: connect to node of opposite parity
        cnt2 := 0
        if parity == 0 {
            cnt2 = even1 + odd2
        } else {
            cnt2 = odd1 + even2
        }
        if cnt1 > cnt2 {
            res[i] = cnt1
        } else {
            res[i] = cnt2
        }
    }
    // Optional: verify results for a small example here (omitted for brevity)
    return res
}
# @lc code=end