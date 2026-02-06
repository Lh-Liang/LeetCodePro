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
        Map<Integer, List<int[]>> tree = new HashMap<>();
        for (int[] edge : edges) {
            tree.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
            tree.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(new int[]{edge[0], edge[2]});
        }
        int[] res = new int[]{0, Integer.MAX_VALUE};
        Map<Integer, Integer> count = new HashMap<>();
        dfs(0, -1, 0, 1, false, count, tree, nums, res);
        return res;
    }
    
    private void dfs(int node, int parent, int pathLen, int nodeCnt, boolean usedDup, Map<Integer, Integer> count, Map<Integer, List<int[]>> tree, int[] nums, int[] res) {
        count.put(nums[node], count.getOrDefault(nums[node], 0) + 1);
        boolean dupNow = usedDup;
        if (count.get(nums[node]) == 2) {
            if (usedDup) {
                count.put(nums[node], count.get(nums[node]) - 1);
                return; // prune, more than one duplicate
            }
            dupNow = true;
        }
        // update result if needed
        if (pathLen > res[0]) {
            res[0] = pathLen;
            res[1] = nodeCnt;
        } else if (pathLen == res[0]) {
            res[1] = Math.min(res[1], nodeCnt);
        }
        for (int[] nei : tree.getOrDefault(node, Collections.emptyList())) {
            int next = nei[0], len = nei[1];
            if (next == parent) continue;
            dfs(next, node, pathLen + len, nodeCnt + 1, dupNow, count, tree, nums, res);
        }
        count.put(nums[node], count.get(nums[node]) - 1);
    }
}
# @lc code=end