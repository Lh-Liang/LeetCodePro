# @lc app=leetcode id=3441 lang=golang
# [3441] Minimum Cost Good Caption
# @lc code=start
func minCostGoodCaption(caption string) string {
    n := len(caption)
    if n < 3 {
        return ""
    }

    runes := []rune(caption)
    i := 0

    for i < n {
        count := 1
        for i+count < n && runes[i+count] == runes[i] {
            count++
        }
        
        if count < 3 {
            if i + count < n && (runes[i+count-1] + 1 == runes[i+count] || runes[i+count-1] - 1 == runes[i+count]) {
                for j := i; j < i + count; j++ {
                    if runes[j] != 'z' {
                        runes[j] = runes[j] + 1
                    } else if runes[j] != 'a' {
                        runes[j] = runes[j] - 1
                    }
                }
            } else {
                return "" // Cannot adjust to form a good caption
            }
            continue // Restart evaluation after adjustment
        }
i += count // Move past this valid group of identical characters
}
i = 0 // Re-evaluate all groups are valid now (all have at least 3 same consecutive chars)
i += count `}
i += count \""
i += count } \"
i += count `}
i += count "}
i += count __`}`}
i += count __}```}}
}
# @lc code=end