#
# @lc app=leetcode id=3771 lang=golang
#
# [3771] Total Score of Dungeon Runs
#
# @lc code=start
func totalScore(hp int, damage []int, requirement []int) int64 {
    // Use prefix sums to efficiently compute remaining health after entering rooms
    n := len(damage)
    prefix := make([]int, n+1)
    for i := 0; i < n; i++ {
        prefix[i+1] = prefix[i] + damage[i]
    }
    var total int64 = 0
    // For each starting room
    for start := 0; start < n; start++ {
        curr_hp := hp
        score := 0
        for i := start; i < n; i++ {
            curr_hp -= damage[i]
            if curr_hp >= requirement[i] {
                score++
            }
        }
        total += int64(score)
    }
    return total
}
# @lc code=end