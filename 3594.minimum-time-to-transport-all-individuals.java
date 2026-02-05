class Solution {
    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        Map<Long, Double> memo = new HashMap<>();
        int FULL = (1 << n) - 1;
        double res = dfs(FULL, 1, 0, n, k, m, time, mul, memo);
        if (res == Double.MAX_VALUE || Double.isInfinite(res) || Double.isNaN(res)) {
            return -1.0;
        }
        return res;
    }
    private double dfs(int baseMask, int boatAtBase, int stage, int n, int k, int m, int[] time, double[] mul, Map<Long, Double> memo) {
        if (baseMask == 0 && boatAtBase == 0) {
            return 0.0;
        }
        long key = (((long) baseMask) << 6) | (boatAtBase << 3) | stage;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        double ans = Double.MAX_VALUE;
        if (boatAtBase == 1) {
            List<Integer> basePeople = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                if (((baseMask >> i) & 1) == 1) {
                    basePeople.add(i);
                }
            }
            int sz = basePeople.size();
            for (int mask = 1; mask < (1 << sz); ++mask) {
                if (Integer.bitCount(mask) > k) continue;
                int groupMax = 0;
                int newBaseMask = baseMask;
                for (int j = 0; j < sz; ++j) {
                    if (((mask >> j) & 1) == 1) {
                        groupMax = Math.max(groupMax, time[basePeople.get(j)]);
                        newBaseMask ^= (1 << basePeople.get(j));
                    }
                }
                double crossTime = groupMax * mul[stage];
                int advance = (int) Math.floor(crossTime) % m;
                int nextStage = (stage + advance) % m;
                double recur = dfs(newBaseMask, 0, nextStage, n, k, m, time, mul, memo);
                if (recur != Double.MAX_VALUE) {
                    ans = Math.min(ans, crossTime + recur);
                }
            }
        } else {
            int destMask = ((1 << n) - 1) ^ baseMask;
            List<Integer> destPeople = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                if (((destMask >> i) & 1) == 1) {
                    destPeople.add(i);
                }
            }
            // If there are still people at base but nobody at destination to return the boat, infeasible
            if (baseMask != 0 && destPeople.isEmpty()) {
                memo.put(key, Double.MAX_VALUE);
                return Double.MAX_VALUE;
            }
            for (int idx : destPeople) {
                double retTime = time[idx] * mul[stage];
                int advance = (int) Math.floor(retTime) % m;
                int nextStage = (stage + advance) % m;
                int newBaseMask = baseMask | (1 << idx);
                double recur = dfs(newBaseMask, 1, nextStage, n, k, m, time, mul, memo);
                if (recur != Double.MAX_VALUE) {
                    ans = Math.min(ans, retTime + recur);
                }
            }
        }
        memo.put(key, ans);
        return ans;
    }
}