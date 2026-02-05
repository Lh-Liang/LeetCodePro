#
# @lc app=leetcode id=3414 lang=java
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
import java.util.*;

class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        // Convert list of lists to an array for easier manipulation and sorting.
        int n = intervals.size();
        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i][0] = intervals.get(i).get(0); // li
            arr[i][1] = intervals.get(i).get(1); // ri
            arr[i][2] = intervals.get(i).get(2); // weighti
        }
        
        // Sort by end time, then start time for lexicographical order.
        Arrays.sort(arr, (a, b) -> {
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });
        
        // Dynamic programming table and choice tracking.
        int[] dp = new int[n + 1]; // Initialize DP table for max scores.
        List<Integer>[] choices = new List[n + 1]; // To track indices chosen for max score.
        for (int i = 0; i <= n; i++) choices[i] = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            int[] current = arr[i];
            int currentWeight = current[2];
            
            // Find last non-overlapping interval using binary search or linear scan backward.
            int k = -1;
            int l = 0, r = i - 1;
            while (l <= r) {
                int mid = l + (r - l) / 2;
                if (arr[mid][1] < current[0]) {
                    k = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            	// Option not to take current interval.			if(dp[i+1]<dp[i]){dp[i+1]=dp[i];choices[i+1].addAll(choices[i]);}			// Option to take current interval if possible.int weightWithCurrent=currentWeight+(k>=0?dp[k+1]:0);			if(weightWithCurrent>dp[i+1]){			    dp[i+1]=weightWithCurrent;			    choices[i+1].clear();			    if(k>=0)choices[i+1].addAll(choices[k+1]);choices[i+1].add(i);}       }	// Reconstruct result from choices stored in DP table.List<Integer> resultIndices=choices[n];Collections.sort(resultIndices);// Ensure lexicographical order.int[]resultArray=new int[Math.min(resultIndices.size(),4)];// Limit result to up to four indices.for(int i=0;i<resultArray.length;i++){resultArray[i]=resultIndices.get(i);}return resultArray;}# @lc code=end