#
# @lc app=leetcode id=3605 lang=golang
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
func minStable(nums []int, maxC int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    // Helper function to calculate GCD of two numbers
    gcd := func(a, b int) int {
        for b != 0 {
            a, b = b, a % b
        }
        return a
    }
    
    // Function to determine HCF for any given range efficiently using sliding window or other method
    calculateHCF := func(l int, r int) int {
        hcf := nums[l]
        for i := l + 1; i <= r; i++ {
            hcf = gcd(hcf, nums[i])
            if hcf < 2 { // If at any point HCF < 2, break early
                break
            }
        }
        return hcf
    }
    
    minStabilityFactor := n // Start with worst case where each element is separate (stability factor = n)
   
    // Strategic modifications planning based on identified key elements impacting stability.
   	// Iterate over possible lengths of subarrays from longest to shortest until changes are exhausted or minimal factor is achieved.	for length := n; length > 1 && maxC >= 0; length-- {		foundStable := false // Track if we found a stable subarray of this length	   	for start := 0; start <= n - length; start++ {		end := start + length - 1		if calculateHCF(start, end) >= 2 { // If this subarray is stable...			foundStable = true // Mark it as found at this length level			break // No need to check further at this size if we confirmed one exists		}	}	   	if !foundStable { // If no stable array found at this length level...		minStabilityFactor = length - 1 // Reduce possible minimal stability factor by one since none exist here anymore.	// Implement strategic changes here based on calculated optimal points of modification from prior analysis.	// Aim is reducing minStabilityFactor as much as possible within limits allowed (maxC).	   	}	}	return minStabilityFactor	}//# @lc code=end