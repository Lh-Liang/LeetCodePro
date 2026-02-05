class Solution {
    public int countCoprime(int[][] mat) {
        int MOD = 1_000_000_007;
        int m = mat.length;
        java.util.Map<Integer, Integer> dp = new java.util.HashMap<>();
        for (int x : mat[0]) dp.put(x, dp.getOrDefault(x, 0) + 1);
        for (int i = 1; i < m; ++i) {
            java.util.Map<Integer, Integer> ndp = new java.util.HashMap<>();
            for (java.util.Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int prev = e.getKey(), cnt = e.getValue();
                for (int x : mat[i]) {
                    int g = gcd(prev, x);
                    ndp.put(g, (int)(((long)ndp.getOrDefault(g, 0) + cnt) % MOD));
                }
            }
            dp = ndp;
        }
        return dp.getOrDefault(1, 0);
    }
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}