#
# @lc app=leetcode id=3779 lang=java
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
import java.util.*;
class Solution {
    public int minOperations(int[] nums) {
        Set<Integer> distinctSet = new HashSet<>();
        int operations = 0;
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }
        
        while (true) {
            distinctSet.clear();
            distinctSet.addAll(numList);
            if (distinctSet.size() == numList.size()) {
                break; // All elements are distinct
            }
            
            // Remove first three elements or all remaining if less than three
            int removeCount = Math.min(3, numList.size());
            for (int i = 0; i < removeCount; i++) {
                numList.remove(0);
            }
            operations++;

            if (numList.isEmpty()) {
                break; // Array is empty
            }
        }
        
        return operations;
    }
}
# @lc code=end