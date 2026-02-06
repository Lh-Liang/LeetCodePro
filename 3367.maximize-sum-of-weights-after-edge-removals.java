#
# @lc app=leetcode id=3367 lang=java
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
import java.util.*;
class Solution {
    public long maximizeSumOfWeights(int[][] edges, int k) {
        int n = edges.length + 1;
        List<int[]>[] tree = new ArrayList[n];
        for(int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for(int[] e : edges) {
            tree[e[0]].add(new int[]{e[1], e[2]});
            tree[e[1]].add(new int[]{e[0], e[2]});
        }
        return dfs(0, -1, tree, k)[0];
    }
    private long[] dfs(int u, int parent, List<int[]>[] tree, int k) {
        // dp[0]: max sum in subtree rooted at u
        // dp[1]: list of edge weights we can offer to parent for possible selection
        PriorityQueue<Long> gains = new PriorityQueue<>();
        long sum = 0;
        for(int[] nei : tree[u]) {
            int v = nei[0], w = nei[1];
            if(v == parent) continue;
            long[] child = dfs(v, u, tree, k);
            // child[0]: max sum in subtree rooted at v
            // child[1]: best gain if we keep edge u-v
            sum += child[0];
            gains.offer(child[1] + w);
            if(gains.size() > k) gains.poll();
        }
        long keep = 0;
        List<Long> list = new ArrayList<>();
        while(!gains.isEmpty()) {
            long val = gains.poll();
            keep += val;
            list.add(val);
        }
        return new long[]{sum + keep, list.size() == 0 ? 0 : Collections.max(list)};
    }
}
# @lc code=end