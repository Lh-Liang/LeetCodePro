#
# @lc app=leetcode id=3462 lang=golang
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
import (
    "sort"
)

func maxSum(grid [][]int, limits []int, k int) int64 {
    // Define a type for storing matrix elements along with their original row index.
    type Element struct {
        value int
        row   int
    }
    
    // Initialize a slice to store potential elements.
    var elements []Element
    
    // Step 1: Collect elements within their respective row limits.
    for i, row := range grid {
        // Sort each row in descending order to facilitate selecting maximum values.
        sort.Sort(sort.Reverse(sort.IntSlice(row)))
        count := 0
        for _, val := range row {
            if count < limits[i] { // Respect the limit for this specific row.
                elements = append(elements, Element{value: val, row: i})
                count++
            } else {
                break // Stop adding when limit is reached.
            }
        }
    }
    
    // Step 2: Sort all collected elements in descending order based on their value.
    sort.Slice(elements, func(i, j int) bool { return elements[i].value > elements[j].value })
    
    // Step 3: Select up to k top elements to maximize the sum.
    var sum int64 = 0
    for i := 0; i < min(k, len(elements)); i++ {
        sum += int64(elements[i].value)
    }
    
    return sum
}

// Helper function for minimum of two integers.
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
# @lc code=end