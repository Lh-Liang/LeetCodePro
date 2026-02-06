#
# @lc app=leetcode id=3373 lang=java
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
import java.util.*;
class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        int n = edges1.length + 1;
        int m = edges2.length + 1;
        List<Integer>[] g1 = new ArrayList[n];
        List<Integer>[] g2 = new ArrayList[m];
        for (int i = 0; i < n; ++i) g1[i] = new ArrayList<>();
        for (int i = 0; i < m; ++i) g2[i] = new ArrayList<>();
        for (int[] e : edges1) {
            g1[e[0]].add(e[1]);
            g1[e[1]].add(e[0]);
        }
        for (int[] e : edges2) {
            g2[e[0]].add(e[1]);
            g2[e[1]].add(e[0]);
        }
        int[] parity1 = new int[n];
        int[] evenCount1 = new int[n];
        int[] oddCount1 = new int[n];
        bfsParity(g1, parity1, evenCount1, oddCount1);
        int[] parity2 = new int[m];
        int even2 = 0, odd2 = 0;
        boolean[] vis2 = new boolean[m];
        Queue<Integer> q2 = new LinkedList<>();
        q2.add(0);
        vis2[0] = true;
        parity2[0] = 0;
        while (!q2.isEmpty()) {
            int u = q2.poll();
            if (parity2[u] == 0) even2++;
            else odd2++;
            for (int v : g2[u]) {
                if (!vis2[v]) {
                    vis2[v] = true;
                    parity2[v] = parity2[u] ^ 1;
                    q2.add(v);
                }
            }
        }
        int[] ans = new int[n];
        for (int i = 0; i < n; ++i) {
            int even1 = evenCount1[i];
            int odd1 = oddCount1[i];
            ans[i] = Math.max(even1 + even2, odd1 + odd2);
        }
        return ans;
    }
    private void bfsParity(List<Integer>[] g, int[] parity, int[] evenCount, int[] oddCount) {
        int n = g.length;
        for (int start = 0; start < n; ++start) {
            boolean[] vis = new boolean[n];
            Queue<Integer> q = new LinkedList<>();
            q.add(start);
            vis[start] = true;
            parity[start] = 0;
            int even = 1, odd = 0;
            while (!q.isEmpty()) {
                int u = q.poll();
                for (int v : g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        parity[v] = parity[u] ^ 1;
                        if (parity[v] == 0) even++;
                        else odd++;
                        q.add(v);
                    }
                }
            }
            evenCount[start] = even;
            oddCount[start] = odd;
        }
    }
}
# @lc code=end