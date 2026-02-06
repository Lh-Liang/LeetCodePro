#
# @lc app=leetcode id=3488 lang=java
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        Map<Integer, List<Integer>> indexMap = new HashMap<>();
        int n = nums.length;
        
        // Preprocess: map each number to its list of indices
        for (int i = 0; i < n; i++) {
            indexMap.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        
        List<Integer> result = new ArrayList<>();
        // Process each query
        for (int query : queries) {
            int target = nums[query];
            List<Integer> indices = indexMap.get(target);
            if (indices == null || indices.size() == 1) { // No other occurrence or only one occurrence at query itself
                result.add(-1);
            } else {
                int minDist = Integer.MAX_VALUE;
                // Find minimum distance considering circularity
                for (int idx : indices) {
                    if (idx != query) {
                        int dist = Math.min(Math.abs(idx - query), n - Math.abs(idx - query)); // Circular distance calculation 
                        minDist = Math.min(minDist, dist); 
                    }
                }   
                result.add(minDist); 
            }    
        }   
        return result;  
    }   
}
# @lc code=end