#
# @lc app=leetcode id=3563 lang=golang
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
func lexicographicallySmallestString(s string) string {
    stack := []rune{}
    for _, c := range s {
        for len(stack) > 0 && (stack[len(stack)-1] == c+1 || stack[len(stack)-1] == c-1 || (stack[len(stack)-1] == 'a' && c == 'z') || (stack[len(stack)-1] == 'z' && c == 'a')) {
            // Remove adjacent consecutive pairs considering circular adjacency
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, c)
    }
    return string(stack)
}
# @lc code=end