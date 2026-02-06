#
# @lc app=leetcode id=3594 lang=java
#
# [3594] Minimum Time to Transport All Individuals
#
# @lc code=start
import java.util.*;
class Solution {
    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        if (k == 1 && n > 1) return -1.0;
        int FULL = (1 << n) - 1;
        Map<Integer, Double>[] memo = new Map[m];
        for (int i = 0; i < m; ++i) memo[i] = new HashMap<>();
        double res = dfs(FULL, 0, n, k, m, time, mul, memo);
        return res == Double.POSITIVE_INFINITY ? -1.0 : res;
    }
    private double dfs(int mask, int stage, int n, int k, int m, int[] time, double[] mul, Map<Integer, Double>[] memo) {
        if (mask == 0) return 0.0; // all at destination
        if (memo[stage].containsKey(mask)) return memo[stage].get(mask);
        double minTime = Double.POSITIVE_INFINITY;
        List<Integer> people = new ArrayList<>();
        for (int i = 0; i < n; ++i) if (((mask >> i) & 1) != 0) people.add(i);
        // Try all groupings to cross (size 1 to k)
        int sz = people.size();
        List<List<Integer>> groups = new ArrayList<>();
        getGroups(people, k, 0, new ArrayList<>(), groups);
        for (List<Integer> group : groups) {
            int nextMask = mask;
            int maxTime = 0;
            for (int p : group) {
                nextMask ^= (1 << p);
                maxTime = Math.max(maxTime, time[p]);
            }
            double trip = maxTime * mul[stage];
            int stageAdv = ((int)Math.floor(trip)) % m;
            int newStage = (stage + stageAdv) % m;
            if (nextMask == 0) {
                minTime = Math.min(minTime, trip);
            } else {
                // try each of the group as returnee
                for (int ret : group) {
                    int backMask = nextMask | (1 << ret);
                    double retTime = time[ret] * mul[newStage];
                    int retAdv = ((int)Math.floor(retTime)) % m;
                    int retStage = (newStage + retAdv) % m;
                    double candidate = trip + retTime + dfs(backMask, retStage, n, k, m, time, mul, memo);
                    minTime = Math.min(minTime, candidate);
                }
            }
        }
        memo[stage].put(mask, minTime);
        return minTime;
    }
    // Generate all possible groupings
    private void getGroups(List<Integer> people, int k, int idx, List<Integer> curr, List<List<Integer>> groups) {
        if (!curr.isEmpty() && curr.size() <= k) groups.add(new ArrayList<>(curr));
        if (curr.size() == k || idx == people.size()) return;
        for (int i = idx; i < people.size(); ++i) {
            curr.add(people.get(i));
            getGroups(people, k, i + 1, curr, groups);
            curr.remove(curr.size() - 1);
        }
    }
}
# @lc code=end