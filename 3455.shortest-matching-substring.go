# @lc app=leetcode id=3455 lang=golang
#
# [3455] Shortest Matching Substring
#
# @lc code=start
func shortestMatchingSubstring(s string, p string) int {
    prefixEnd := strings.Index(p, "*")
    suffixStart := strings.LastIndex(p, "*") + 1
    prefix := p[:prefixEnd]
    suffix := p[suffixStart:]
    middle := p[prefixEnd+1:suffixStart-1]
    
    n := len(s)
    minLength := n + 1 // Initialize with a value larger than any possible substring
    
    i := 0
    for i <= n-len(prefix) {
        if strings.HasPrefix(s[i:], prefix) {
            j := i + len(prefix)
            for j <= n-len(suffix) {
                if strings.Contains(s[j:], middle) {
                    k := j + strings.Index(s[j:], middle) + len(middle)
                    if k <= n && strings.HasPrefix(s[k:], suffix) {
                        minLength = min(minLength, k+len(suffix)-i)
                        break // Found a valid match, try to improve
                    }
                }
                j++
            }
        }
        i++
    }
    
    if minLength == n+1 {
        return -1 // No valid substring found
    }
    return minLength
}

func min(a, b int) int {
	if a < b { return a } return b } # @lc code=end