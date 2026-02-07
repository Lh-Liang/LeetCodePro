#
# @lc app=leetcode id=3387 lang=golang
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
    // Helper function to perform Bellman-Ford style relaxation.
    relax := func(pairs [][]string, rates []float64) map[string]float64 {
        maxAmounts := make(map[string]float64)
        maxAmounts[initialCurrency] = 1.0
        for i := 0; i < len(pairs); i++ {
            for j := range pairs {
                start, target := pairs[j][0], pairs[j][1]
                rate := rates[j]
                if amount, exists := maxAmounts[start]; exists {
                    if maxAmounts[target] < amount * rate {
                        maxAmounts[target] = amount * rate
                    }
                }
            }
        }
        return maxAmounts
    }

    // Calculate Day 1 results.
    maxAfterDay1 := relax(pairs1, rates1)

    // Use results from Day 1 as basis for Day 2 calculations.
    finalMaxAmounts := make(map[string]float64)
    for curr, amount := range maxAfterDay1 {
        tempMax := relax(pairs2, rates2)
        for newCurr, newAmount := range tempMax {
            if finalMaxAmounts[newCurr] < newAmount * amount {
                finalMaxAmounts[newCurr] = newAmount * amount
            }
        }
    }

    // Return maximum amount of initial currency after Day 2.
    return finalMaxAmounts[initialCurrency]
}
# @lc code=end