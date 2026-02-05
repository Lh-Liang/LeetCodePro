#
# @lc app=leetcode id=3464 lang=java
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        int low = 0;
        // Determine a realistic high bound based on possible configurations of boundary points
        int high = calculateMaxManhattanDistance(side);
        while (low < high) {
            int mid = (high + low + 1) / 2;
            if (isFeasible(mid, points, k)) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }
    
    // Calculate maximum possible Manhattan distance for given side length
    private int calculateMaxManhattanDistance(int side) {
        // Example logic: Consider maximal distances between corners or specific configurations on boundary
        return side * 2; // Placeholder logic; needs refining based on actual problem constraints
    }
    
    private boolean isFeasible(int dist, int[][] points, int k) {
        // Sort all points based on x-coordinate first and then y-coordinate
        Arrays.sort(points, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
        List<int[]> selectedPoints = new ArrayList<>();
        for (int[] point : points) {
            boolean valid = true;
            for (int[] selPoint : selectedPoints) {
                if (Math.abs(point[0] - selPoint[0]) + Math.abs(point[1] - selPoint[1]) < dist) {
                    valid = false;
                    break;
                }
            }
            if (valid) selectedPoints.add(point);
            if (selectedPoints.size() == k) return true;
        }
        return false; // Not enough points could be selected with minimum `dist` apart
    }
}
# @lc code=end