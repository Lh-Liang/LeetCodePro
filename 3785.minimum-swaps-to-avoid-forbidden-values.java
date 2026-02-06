#
# @lc app=leetcode id=3785 lang=java
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#
# @lc code=start
class Solution {
public int minSwaps(int[] nums, int[] forbidden) {
    int n = nums.length;
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < n; i++) {
        if (nums[i] != forbidden[i]) {
            map.put(nums[i], i);
        } else {
            boolean swapped = false;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] != forbidden[i] && nums[j] != forbidden[j]) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                    swapped = true;
                    break;
                }
            }
            if (!swapped) return -1; // No valid swap found to separate from forbidden value. 
        }
    }
    return map.size(); // Count of successful swaps made. 
}
}
# @lc code=end