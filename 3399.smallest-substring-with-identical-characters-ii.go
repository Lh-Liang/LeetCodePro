#
# @lc app=leetcode id=3399 lang=golang
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
func minLength(s string, numOps int) int {
    n := len(s)
    left, right := 0, 0
    maxLen := 0
    flipCount := 0
    currentChar := ' ' // not a valid char initially
    
    for right < n {
        if s[right] != currentChar {
            flipCount++
            if flipCount > numOps {
                currentChar = s[left]
                flipCount--
                for left < n && s[left] == currentChar {
                    left++
                }
                left++ // move past last different char causing excess flips
            } else {
                currentChar = s[right]
            }
        }
        maxLen = max(maxLen, right-left+1)
        right++
    }
    return maxLen// - 1 because we want minimum longest-length after flips (as asked in problem) 
}
def max(a, b int) int { if a > b { return a } else { return b } } 
def min(a, b int) int { if a < b { return a } else { return b } } 
def abs(a int) int { if a < 0 { return -a } else { return a } } 
def zeroIfNegative(a int) int { if a < 0 { return 0 } else { return a }} 
def minLengthAfterFlips(s string, k int) int{ cnt:= make(map[byte]int); cnt['0'], cnt['1'] = 0 , 0; res:= len(s); j := 0; for i:= range s{cnt[s[i]]++; for min(cnt['0'], cnt['1']) > k{cnt[s[j]]--; j++;} res=min(res,max(cnt['0'],cnt['1']))} return res;} # @lc code=end