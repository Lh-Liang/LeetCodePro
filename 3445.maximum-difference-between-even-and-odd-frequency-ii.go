#
# @lc app=leetcode id=3445 lang=golang
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
func maxDifference(s string, k int) int {
    maxDiff := -1
    n := len(s)
    for i := 0; i <= n-k; i++ {
        freq := make(map[byte]int)
        for j := i; j < n; j++ {
            freq[s[j]]++
            if j-i+1 >= k {
                maxOdd, minEven := 0, 0x3f3f3f3f // large value for min comparison
                for _, count := range freq {
                    if count%2 == 1 { // odd frequency
                        if count > maxOdd {
                            maxOdd = count
                        }
                    } else if count > 0 { // even frequency and non-zero
                        if minEven == 0x3f3f3f3f || count < minEven {
                            minEven = count
                        }
                    }
                }
                if maxOdd != 0 && minEven != 0x3f3f3f3f && (maxOdd-minEven) > maxDiff {
                    maxDiff = maxOdd - minEven
                } 
            } 
        } 
    } 
    return maxDiff 
}
# @lc code=end