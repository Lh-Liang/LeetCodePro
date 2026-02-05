# @lc app=leetcode id=3488 lang=java
#
# [3488] Closest Equal Element Queries
#
# @lc code=start
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        Map<Integer, List<Integer>> valueIndicesMap = new HashMap<>();
        int n = nums.length;
        List<Integer> results = new ArrayList<>();

        // Building a map of values to their indices for quick access
        for (int i = 0; i < n; i++) {
            if (!valueIndicesMap.containsKey(nums[i])) {
                valueIndicesMap.put(nums[i], new ArrayList<>());
            }
            valueIndicesMap.get(nums[i]).add(i);
        }

        // Process each query
        for (int query : queries) {
            int targetValue = nums[query];
            List<Integer> indices = valueIndicesMap.get(targetValue);
            int minDistance = Integer.MAX_VALUE;

            // Calculate minimum distance using both direct and circular paths
            if (indices != null && indices.size() > 1) {
                for (int index : indices) {
                    if (index != query) {
                        int directDist = Math.abs(index - query);
                        int circularDist = Math.min(directDist, n - directDist);
                        minDistance = Math.min(minDistance, circularDist);
                    }
                }
                results.add(minDistance);
            } else {
                results.add(-1);
            }
        }
        return results;
    }
}
# @lc code=end