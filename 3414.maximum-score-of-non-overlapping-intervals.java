//
// @lc app=leetcode id=3414 lang=java
//
// [3414] Maximum Score of Non-overlapping Intervals
//

// @lc code=start
import java.util.*;
class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        // Sort intervals by end time
        intervals.sort((a, b) -> a.get(1).compareTo(b.get(1)));
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]); // Max-heap based on weight
        List<Integer> result = new ArrayList<>();
        int currentEnd = -1;
        for (int i = 0; i < intervals.size(); i++) {
            List<Integer> interval = intervals.get(i);
            int start = interval.get(0), end = interval.get(1), weight = interval.get(2);
            if (start > currentEnd) { // Non-overlapping condition
                pq.offer(new int[]{weight, i}); // Add to heap if it does not overlap with last chosen interval
                if (pq.size() > 4) pq.poll(); // Keep at most 4 highest weights in the heap
                currentEnd = end; // Update current end time for next comparison
            }
        }
        while (!pq.isEmpty()) result.add(pq.poll()[1]); // Extract indices from max-heap into result list 
        Collections.sort(result); // Sort indices to ensure lexicographical order 
        return result.stream().mapToInt(Integer::intValue).toArray(); 
    } 
}
// @lc code=end