#
# @lc app=leetcode id=3563 lang=golang
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
func lexicographicallySmallestString(s string) string {
    var stack []rune
    for _, c := range s {
        if len(stack) > 0 && (c == stack[len(stack)-1]+1 || c == stack[len(stack)-1]-1 || (c == 'a' && stack[len(stack)-1] == 'z') || (c == 'z' && stack[len(stack)-1] == 'a')) {
            stack = stack[:len(stack)-1]
        } else {
            stack = append(stack, c)
        }
    }
    return string(stack)
}
# @lc code=end