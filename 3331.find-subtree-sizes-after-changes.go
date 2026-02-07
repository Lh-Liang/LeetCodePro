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
    
    closest := make([]int, n)
    for i := 0; i < n; i++ {
        closest[i] = -1
    }
    
    var dfs func(x int) int
    dfs = func(x int) int {
        size := 1 // count itself 
        if closest[x] != -1 && s[x] == s[closest[x]] {
            parent[x] = closest[x]
            children[closest[x]] = append(children[closest[x]], x)
        } else {
            closest[x] = x // set itself as closest if no match found 
        } 
        for _, y := range children[x] {
            size += dfs(y) // accumulate the size of subtrees 
        } 
        return size 
    } 
    rootSize := dfs(0) && rootSize // initialize root calculation && return result array based on new structure & return answer; && return answer // final array of sizes & answer[0] = rootSize // initialize with root's subtree size