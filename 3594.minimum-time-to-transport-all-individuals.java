# \@lc code=start
class Solution {
    private double[][][] memo;
    private int n, k, m;
    private int[] time;
    private double[] mul;

    public double minTime(int n, int k, int m, int[] time, double[] mul) {
        this.n = n;
        this.k = k;
        this.m = m;
        this.time = time;
        this.mul = mul;
        this.memo = new double[1 << n][1 << n][m];
        for (double[][] side : memo) {
            for (double[] stage : side) {
                Arrays.fill(stage, -1);
            }
        }
        // Start DFS from initial state with all individuals on base side
        return dfs((1 << n) - 1, 0, 0);
    }

    private double dfs(int baseSideMask, int destSideMask, int currentStage) {
        if (baseSideMask == 0) return 0; // All transported
        if (memo[baseSideMask][destSideMask][currentStage] != -1)
            return memo[baseSideMask][destSideMask][currentStage];

        double minTime = Double.MAX_VALUE;
        // Try sending up to 'k' individuals from base side to destination
        for (int subset = baseSideMask; subset > 0; subset = (subset - 1) & baseSideMask) {
            if (Integer.bitCount(subset) <= k) { // Check boat capacity
                double maxTime = getMaxTime(subset);
                double crossingTime = maxTime * mul[currentStage];
                int nextStage = (currentStage + ((int)Math.floor(crossingTime)) % m) % m;
                minTime = Math.min(minTime,
dfs(baseSideMask ^ subset, destSideMask | subset, nextStage) + crossingTime);
            }
        }

        // Consider returning an individual if needed
        if ((baseSideMask | destSideMask) != ((1 << n) - 1)) { // Not all on base or dest
            for (int r = 0; r < n; r++) {
                if ((destSideMask & (1 << r)) != 0) { // If person 'r' is at destination
                    double returnTime = time[r] * mul[currentStage];
inextStage = (currentStage + ((int)Math.floor(returnTime)) % m) % m;
timeOption = dfs(baseSideMask | (1 << r), destSideMask ^ (1 << r), nextStage)+ returnTime;
inminTime = Math.min(minTime, timeOption);
in}
in}
in}
memo[baseSideMask][destSideMask][currentStage] = minTime != Double.MAX_VALUE ? minTime : -1;
inreturn minTime;}private double getMaxTime(int mask){
double maxT=0;or(inti=0;i<n;i++){if((mask&(1<<i))!=0){maxT=Math.max(maxT,time[i]);}
in}
inreturn maxT;}\@lc code=end