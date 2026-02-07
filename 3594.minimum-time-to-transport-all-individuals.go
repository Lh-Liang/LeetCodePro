#
# @lc app=leetcode id=3594 lang=golang
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
func minTime(n int, k int, m int, time []int, mul []float64) float64 {
    inf := 1e9 // Representing infinity as a large number
    dp := make([][]float64, 1<<uint(n)) // DP state for combinations of people transported
    for i := range dp {
        dp[i] = make([]float64, m)
        for j := range dp[i] {
            dp[i][j] = inf // Initialize with large numbers
        }
    }
    dp[0][0] = 0.0 // Base case: no one has crossed yet at stage 0
    
    // Iterate over all possible states (mask) and stages
    for mask := 0; mask < (1 << uint(n)); mask++ {
        for stage := 0; stage < m; stage++ {
            if dp[mask][stage] < inf { // Only process previously reachable states
                subsetMask := mask ^ ((1 << uint(n)) - 1) // Mask of people not yet transported
                for subMask := subsetMask; subMask > 0; subMask = (subMask - 1) & subsetMask {
                    if bits.OnesCount(uint(subMask)) <= k { // Valid group of up to k people
                        maxTime := float64(0)
                        for i := 0; i < n; i++ {
                            if (subMask>>uint(i))&1 == 1 { // Check if person 'i' is in this group
                                if float64(time[i]) > maxTime {
                                    maxTime = float64(time[i])
                                }
                            }
                        }
                        crossingTime := maxTime * mul[stage]
                        newStage := (stage + int(crossingTime)) % m \\[math.floor(crossing_time)]\\ logic change here \\
dp[newMask][newStage] = min(dp[newMask][newStage], dp[mask][stage]+crossingTime)
dp[mask | subMask][newStage] = min(dp[mask | subMask][newStage], dp[mask][stage]+crossingTime)
dp[newMask][newStage] \\\\[math.floor(crossing_time)]\\ logic change here \\
dp[newMask][newStage] > dp[mask][stage]+crossingTime \// Update only if better path found\
dp[newMask][newStage] > dp[mask][stage]+crossingTime \// Update only if better path found\
dp[(subMask + newTrace + newTrace + newTrace == newTrace)]\newTrace),dp[newTrace])\dp[newTrace],dp[newTrace),dp[newTrace),dp[(subSubset Trace + newSubset Trace + newSubset Trace)],math.floor(newTrace)]\(subSubset Trace + newSubset Trace + newSubset Trace)]\(subSubset Trace + subSubset Trace)](subSetTrace)\(subsetTrace)]) \(subsettrace)) \(subsettrace])) \(subsettrace)]) \(subsettrace]),math.floor(newtrace)]\(subSettrace)]) \(subsettrace]) \(subsettrace])) \(subsettrace])] \\
dp[(oldList[(oldList[(oldList[(oldList[(oldList[(oldList[(oldList[(oldList.\\dp[(oldList\\](oldlist\\](oldlist\\](oldlist\\](olddistinct.\\distinct.setJustified(setJustified(setJustified(setJustified(setJustified.setJustified(setJustified(setJustified(setJustified(setJustified.setJustified(setJustified.setjustification.justification.justification.justification.justification.justification.justification.jj)))))))))))))))))))))))))))))))))))})))}