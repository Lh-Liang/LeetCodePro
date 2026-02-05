//
// @lc app=leetcode id=3625 lang=java
//
// [3625] Count Number of Trapezoids II
//
// @lc code=start
import java.util.*;
class Solution {
    public int countTrapezoids(int[][] points) {
        int n = points.length;
        Set<String> seen = new HashSet<>();
        int count = 0;
        // Generate all combinations of 4 points
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    for (int l = k + 1; l < n; ++l) {
                        int[][] quad = {points[i], points[j], points[k], points[l]};
                        // Instead of all permutations, only check all unique cyclic orderings to avoid redundancy
                        for (int[] order : new int[][]{{0,1,2,3},{0,1,3,2},{0,2,1,3}}) {
                            int[][] poly = {
                                quad[order[0]], quad[order[1]], quad[order[2]], quad[order[3]]
                            };
                            if (isConvex(poly) && hasParallelSides(poly)) {
                                int[][] sortedPoly = Arrays.copyOf(poly, 4);
                                Arrays.sort(sortedPoly, (a, b) -> {
                                    if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
                                    return Integer.compare(a[1], b[1]);
                                });
                                StringBuilder sb = new StringBuilder();
                                for (int[] pt : sortedPoly) sb.append(pt[0]).append(',').append(pt[1]).append(';');
                                String key = sb.toString();
                                if (!seen.contains(key)) {
                                    seen.add(key);
                                    count++;
                                }
                                break; // Only count once per set of 4 points
                            }
                        }
                    }
                }
            }
        }
        return count;
    }
    private boolean isConvex(int[][] quad) {
        int n = quad.length;
        int prev = 0;
        for (int i = 0; i < n; ++i) {
            int[] a = quad[i];
            int[] b = quad[(i + 1) % n];
            int[] c = quad[(i + 2) % n];
            int cross = crossProduct(a, b, c);
            if (cross == 0) return false;
            if (prev == 0) prev = cross > 0 ? 1 : -1;
            else if ((cross > 0 ? 1 : -1) != prev) return false;
        }
        return true;
    }
    private int crossProduct(int[] a, int[] b, int[] c) {
        int x1 = b[0] - a[0];
        int y1 = b[1] - a[1];
        int x2 = c[0] - b[0];
        int y2 = c[1] - b[1];
        return x1 * y2 - y1 * x2;
    }
    private boolean hasParallelSides(int[][] quad) {
        return isParallel(quad[0], quad[1], quad[2], quad[3]) ||
               isParallel(quad[1], quad[2], quad[3], quad[0]);
    }
    private boolean isParallel(int[] a, int[] b, int[] c, int[] d) {
        int dx1 = b[0] - a[0];
        int dy1 = b[1] - a[1];
        int dx2 = d[0] - c[0];
        int dy2 = d[1] - c[1];
        return dx1 * dy2 == dy1 * dx2;
    }
}
// @lc code=end