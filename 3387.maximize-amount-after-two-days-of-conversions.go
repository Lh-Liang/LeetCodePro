#
# @lc app=leetcode id=3387 lang=golang
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
func maxAmount(initialCurrency string, pairs1 [][]string, rates1 []float64, pairs2 [][]string, rates2 []float64) float64 {
    // Construct graph for Day 1 conversions using adjacency lists
    day1Graph := make(map[string]map[string]float64)
    for i, pair := range pairs1 {
        if day1Graph[pair[0]] == nil {
            day1Graph[pair[0]] = make(map[string]float64)
        }
        day1Graph[pair[0]][pair[1]] = rates1[i]
        day1Graph[pair[1]] = make(map[string]float64) // Reverse conversion not needed here but initialized for completeness
    }
    
    // Calculate all possible amounts after Day 1 using BFS/DFS
    amountsDay1 := make(map[string]float64)
    amountsDay1[initialCurrency] = 1.0 // Start with initial currency value of 1.0
    queue := []struct{currency string; amount float64}{{initialCurrency, 1.0}}
    
    for len(queue) > 0 {
        current := queue[0]
        queue = queue[1:]
        for nextCurrency, rate := range day1Graph[current.currency] {
            newAmount := current.amount * rate
            if newAmount > amountsDay1[nextCurrency] {
                amountsDay1[nextCurrency] = newAmount
                queue = append(queue, struct{currency string; amount float64}{nextCurrency, newAmount})
            }
        }
    }
    
    // Construct graph for Day 2 conversions using adjacency lists and calculate maximum after Day 2 conversions based on Day 1 results. Similar process with Day 2 graph. 
    day2Graph := make(map[string]map[string]float64) 
    for i, pair := range pairs2 { 
        if day2Graph[pair[0]] == nil { 
            day2Graph[pair[0]] = make(map[string]float64) 
        } 
        day2Graph[pair[0]][pair[1]] = rates2[i] 
        day2Graph[pair[1]] = make(map[string]float64) // Reverse conversion not needed here but initialized for completeness 
    } 
n maxAmountAfterTwoDays := 0.0 
n for currencyAfterDayOne, amountAfterDayOne := range amountsDay1 { 
n queueAfterDayOne := []struct{currency string; amount float64}{{currencyAfterDayOne, amountAfterDayOne}} 
n amountsDayTwo := make(map[string]float64) 
n amountsDayTwo[currencyAfterDayOne] = amountAfterDayOne 
n while len(queueAfterDayOne) > 0 { 
n currentConversion := queueAfterDayOne[0] 
n queueAfterDayOne = queueAfterDayOne[1:] 
n for nextCurrency, rate := range day2Graph[currentConversion.currency] { 
n newAmountTwoDays := currentConversion.amount * rate 
n if newAmountTwoDays > amountsDayTwo[nextCurrency] { 
n amountsDayTwo[nextCurrency] = newAmountTwoDays 
n queueAfterDayOne = append(queueAfterDayOne, struct{currency string; amount float64}{nextCurrency, newAmountTwoDays}) } } } nn maxAmountForThisPath := amountsDayTwo[initialCurrency] nn if maxAmountForThisPath > maxAmountAfterTwoDays { nn maxAmountAfterTwoDays = maxAmountForThisPath n} n} return maxAmountAfterTwoDays n} # @lc code=end