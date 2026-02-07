#
# @lc app=leetcode id=3331 lang=golang
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
func findSubtreeSizes(parent []int, s string) []int {
    n := len(parent)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        children[parent[i]] = append(children[parent[i]], i)
    }
    newParent := make([]int, n)
    copy(newParent, parent)
    // Step 1: DFS to assign new parents based on closest same-char ancestor
    var dfs func(node int, path map[byte]int)
    dfs = func(node int, path map[byte]int) {
        if node != 0 {
            c := s[node]
            if y, ok := path[c]; ok {
                newParent[node] = y
            }
        }
        c := s[node]
        orig, had := path[c]
        path[c] = node
        for _, ch := range children[node] {
            dfs(ch, path)
        }
        if had {
            path[c] = orig
        } else {
            delete(path, c)
        }
    }
    dfs(0, map[byte]int{ s[0]: 0 })
    // Step 2: Build new children list from newParent
    newChildren := make([][]int, n)
    for i := 1; i < n; i++ {
        newChildren[newParent[i]] = append(newChildren[newParent[i]], i)
    }
    // Step 3: DFS to compute subtree sizes
    ans := make([]int, n)
    var dfs2 func(int) int
    dfs2 = func(u int) int {
        sz := 1
        for _, v := range newChildren[u] {
            sz += dfs2(v)
        }
        ans[u] = sz
        return sz
    }
    dfs2(0)
    return ans
}
# @lc code=end