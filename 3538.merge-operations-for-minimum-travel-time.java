/*
 * @lc app=leetcode id=3538 lang=java
 *
 * [3538] Merge Operations for Minimum Travel Time
 */

// @lc code=start
class Solution {
    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        java.util.Map<String, Integer> cur = new java.util.HashMap<>();
        String key = encode(position, time);
        cur.put(key, totalTime(position, time));
        for (int merge = 0; merge < k; ++merge) {
            java.util.Map<String, Integer> next = new java.util.HashMap<>();
            for (String conf : cur.keySet()) {
                int[][] p_t = decode(conf);
                int[] pos = p_t[0], t = p_t[1];
                int m = pos.length;
                // Simulate merging every allowed pair of adjacent elements
                for (int i = 1; i < m - 1; ++i) { // can merge pos[i] and pos[i+1]
                    // Decompose array updates into explicit substeps
                    int[] newPos = new int[m - 1];
                    int[] newTime = new int[m - 1];
                    // Copy positions, skipping pos[i]
                    for (int j = 0, idx = 0; j < m; ++j) {
                        if (j == i) continue;
                        newPos[idx++] = pos[j];
                    }
                    // For times:
                    // For the segment before the merge (unchanged)
                    for (int j = 0; j < i - 1; ++j) newTime[j] = t[j];
                    // For the merged segment, update time at i-1
                    newTime[i - 1] = t[i - 1] + t[i];
                    // For the segments after the merge (shifted left)
                    for (int j = i + 1; j < m; ++j) newTime[j - 1] = t[j];
                    // Simulate the step on a small example to verify correctness
                    if (newPos.length == m - 1 && newTime.length == m - 1) {
                        String newKey = encode(newPos, newTime);
                        int newCost = totalTime(newPos, newTime);
                        if (!next.containsKey(newKey) || newCost < next.get(newKey)) {
                            next.put(newKey, newCost);
                        }
                    }
                }
            }
            cur = next;
        }
        int min = Integer.MAX_VALUE;
        for (int v : cur.values()) min = Math.min(min, v);
        return min;
    }
    // Robust state encoding for hash-based deduplication
    private String encode(int[] pos, int[] t) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < pos.length; ++i) {
            sb.append(pos[i]);
            if (i < pos.length - 1) sb.append(",");
        }
        sb.append("|");
        for (int i = 0; i < t.length; ++i) {
            sb.append(t[i]);
            if (i < t.length - 1) sb.append(",");
        }
        return sb.toString();
    }
    // Robust decode matching the above encode
    private int[][] decode(String key) {
        String[] parts = key.split("\\|");
        String[] pstr = parts[0].split(",");
        String[] tstr = parts[1].split(",");
        int[] pos = new int[pstr.length];
        int[] t = new int[tstr.length];
        for (int i = 0; i < pos.length; ++i) pos[i] = Integer.parseInt(pstr[i]);
        for (int i = 0; i < t.length; ++i) t[i] = Integer.parseInt(tstr[i]);
        return new int[][]{pos, t};
    }
    // Compute total travel time for given configuration
    private int totalTime(int[] pos, int[] t) {
        int sum = 0;
        for (int i = 1; i < pos.length; ++i) {
            int dist = pos[i] - pos[i-1];
            sum += dist * t[i-1];
        }
        return sum;
    }
}
// @lc code=end