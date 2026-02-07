#
# @lc app=leetcode id=3327 lang=golang
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
func findAnswer(parent []int, s string) []bool {
    n := len(parent)
    children := make([][]int, n)
    for i := 1; i < n; i++ {
        p := parent[i]
        children[p] = append(children[p], i)
    }
    
    var dfs func(int) string
    dfs = func(node int) string {
        dfsStr := ""
        for _, child := range children[node] {
            dfsStr += dfs(child)
        }
        return dfsStr + string(s[node])
    }
    
    answer := make([]bool, n)
    for i := 0; i < n; i++ {
        dfsStr := dfs(i)
        answer[i] = isPalindrome(dfsStr)
    }
    return answer
}

func isPalindrome(s string) bool { &lt;- helper function to check palindrome condition &gt; &gt;