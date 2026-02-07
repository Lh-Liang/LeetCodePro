#
# @lc app=leetcode id=3771 lang=golang
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
func totalScore(hp int, damage []int, requirement []int) int64 {
    n := len(damage)
    totalScore := int64(0)
    cumulativeDamage := make([]int, n+1)
    
    // Calculate cumulative damage from the start to each room
    for i := 0; i < n; i++ {
        cumulativeDamage[i+1] = cumulativeDamage[i] + damage[i]
    }
    
    // Calculate scores starting from each room using prefix sums
    for start := 0; start < n; start++ {
        currentHp := hp - cumulativeDamage[start]
        currentScore := 0
        for i := start; i < n; i++ {
            if currentHp >= requirement[i] {
                currentScore++
            }
            currentHp -= damage[i]
        }
        totalScore += int64(currentScore)
    }
    return totalScore
}
# @lc code=end