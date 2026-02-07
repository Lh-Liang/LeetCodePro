#
# @lc app=leetcode id=3771 lang=golang
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
func totalScore(hp int, damage []int, requirement []int) int64 {
    n := len(damage)
    totalScore := int64(0)
    
    for start := 0; start < n; start++ {
        currentHp := hp
        currentScore := 0
        
        for i := start; i < n; i++ {
            currentHp -= damage[i]
            if currentHp >= requirement[i] {
                currentScore++
            } else { // Health is not enough to earn a point from room i+1 onwards. 
                break // Optimization: stop early as subsequent rooms will not earn any points. 
            }
        }
        
        totalScore += int64(currentScore)
    }
    
    return totalScore
}
# @lc code=end