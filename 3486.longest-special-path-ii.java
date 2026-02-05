#
# @lc app=leetcode id=3486 lang=java
#
# [3486] Longest Special Path II
#

# @lc code=start
import java.util.*;
class Solution {
    public int[] longestSpecialPath(int[][] edges, int[] nums) {
        int n = nums.length;
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(new int[]{e[1], e[2]});
            graph[e[1]].add(new int[]{e[0], e[2]});
        }
        int[] result = new int[]{0, Integer.MAX_VALUE}; // {maxLength, minNodes}
        Map<Integer, Integer> count = new HashMap<>();
        dfs(0, -1, 0, 1, nums, graph, count, 0, result);
        // Final verification step could be added here if needed
        return result;
    }
    private void dfs(int node, int parent, int currLen, int currNodes, int[] nums, List<int[]>[] graph, Map<Integer, Integer> count, int dup, int[] result) {
        count.put(nums[node], count.getOrDefault(nums[node], 0) + 1);
        if (count.get(nums[node]) == 2) dup++;
        // Explicit constraint check
        if (dup <= 1) {
            if (currLen > result[0]) {
                result[0] = currLen;
                result[1] = currNodes;
            } else if (currLen == result[0]) {
                result[1] = Math.min(result[1], currNodes);
            }
            for (int[] nei : graph[node]) {
                int next = nei[0], weight = nei[1];
                if (next != parent) {
                    dfs(next, node, currLen + weight, currNodes + 1, nums, graph, count, dup, result);
                }
            }
        }
        if (count.get(nums[node]) == 2) dup--;
        count.put(nums[node], count.get(nums[node]) - 1);
    }
}
# @lc code=end