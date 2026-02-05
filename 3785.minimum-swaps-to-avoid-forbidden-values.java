#
# @lc app=leetcode id=3785 lang=java
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution {
    public int minSwaps(int[] nums, int[] forbidden) {
        int n = nums.length;
        // Step 1: Identify indices where nums[i] == forbidden[i]
        List<Integer> conflictIndices = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                conflictIndices.add(i);
            }
        }
        // Step 2: Attempt to resolve conflicts by swapping with non-conflicting indices
        int swaps = 0;
        for (int i : conflictIndices) {
            boolean resolved = false;
            for (int j = 0; j < n; j++) {
                if (nums[j] != forbidden[j] && nums[j] != forbidden[i]) {
                    // Swap indices i and j to resolve conflict at i
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                    swaps++;
                    resolved = true;
                    break; 
                } 
            } 
            if (!resolved) return -1; // If no resolution possible for this conflict 
        } 
        // Final validation
        for (int i = 0; i < n; i++) {
            if (nums[i] == forbidden[i]) {
                return -1; // Return -1 if any conflict remains
            }
        }
        return swaps; 
    } 
}
# @lc code=end