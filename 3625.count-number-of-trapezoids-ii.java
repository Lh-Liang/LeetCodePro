#
# @lc app=leetcode id=3625 lang=java
#
# [3625] Count Number of Trapezoids II
#
# @lc code=start
import java.util.*;

class Solution {
    private static int gcd(int a, int b) {
        return b == 0 ? Math.abs(a) : gcd(b, a % b);
    }

    // Normalize slope as (dy, dx) with dx >= 0
    private static String slope(int[] p1, int[] p2) {
        int dy = p2[1] - p1[1];
        int dx = p2[0] - p1[0];
        if (dx == 0) return "inf";
        int sign = dx > 0 ? 1 : -1;
        int g = gcd(dy, dx);
        dy /= g; dx /= g;
        return (sign * dy) + "/" + (sign * dx);
    }

    public int countTrapezoids(int[][] points) {
        int n = points.length;
        Map<String, List<int[]>> slopeMap = new HashMap<>();
        // Step 1: For each pair, compute and group by slope
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                String s = slope(points[i], points[j]);
                slopeMap.computeIfAbsent(s, k -> new ArrayList<>()).add(new int[]{i, j});
            }
        }
        Set<String> trapezoids = new HashSet<>();
        // Step 2: For each slope, check pairs of non-overlapping segments
        for (List<int[]> segs : slopeMap.values()) {
            int m = segs.size();
            for (int a = 0; a < m; ++a) {
                for (int b = a+1; b < m; ++b) {
                    int[] seg1 = segs.get(a), seg2 = segs.get(b);
                    Set<Integer> all = new HashSet<>();
                    for (int idx : seg1) all.add(idx);
                    for (int idx : seg2) all.add(idx);
                    if (all.size() < 4) continue; // overlap
                    int[] quad = all.stream().mapToInt(x->x).toArray();
                    // Ensure convexity: check all triangles have same orientation
                    int[][] ps = new int[4][];
                    for (int k = 0; k < 4; ++k) ps[k] = points[quad[k]];
                    boolean convex = true;
                    int last = 0;
                    for (int k = 0; k < 4; ++k) {
                        int[] p = ps[k], q = ps[(k+1)%4], r = ps[(k+2)%4];
                        int cross = (q[0]-p[0])*(r[1]-q[1]) - (q[1]-p[1])*(r[0]-q[0]);
                        if (k == 0) last = Integer.compare(cross, 0);
                        else if (Integer.compare(cross, 0) != last) { convex = false; break; }
                    }
                    if (!convex) continue;
                    Arrays.sort(quad);
                    trapezoids.add(Arrays.toString(quad));
                }
            }
        }
        return trapezoids.size();
    }
}
# @lc code=end