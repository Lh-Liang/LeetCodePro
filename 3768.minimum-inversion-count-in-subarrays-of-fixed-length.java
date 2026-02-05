#
# @lc app=leetcode id=3768 lang=java
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#
# @lc code=start
import java.util.*;

class Solution {
    public long minInversionCount(int[] nums, int k) {
        int n = nums.length;
        long minInversions = Long.MAX_VALUE;
        // Step to compress coordinates
        int[] sortedNums = Arrays.copyOf(nums, n);
        Arrays.sort(sortedNums);
        Map<Integer, Integer> valueToCompressed = new HashMap<>();
        for (int i = 0; i < n; i++) {
            valueToCompressed.put(sortedNums[i], i + 1); // Use values as indexes for FenwickTree
        }
        
        FenwickTree fenwickTree = new FenwickTree(n); // Size based on compressed range
        long currentInversions = 0;

        for (int i = 0; i < n; i++) {
            int compressedValue = valueToCompressed.get(nums[i]);
            if (i >= k) {
                int outValue = valueToCompressed.get(nums[i - k]);
                // Remove element that is sliding out of the window from Fenwick Tree
                fenwickTree.update(outValue, -1);
                currentInversions -= fenwickTree.query(outValue - 1); // Remove left inversions for outValue
            }
            // Add current element to Fenwick Tree and count right inversions before adding it fully
            currentInversions += fenwickTree.query(n) - fenwickTree.query(compressedValue);
            fenwickTree.update(compressedValue, 1);
            if (i >= k - 1) { // Start calculating from when we have a full window
                minInversions = Math.min(minInversions, currentInversions);
            }
        }
        return minInversions;
    }
}

class FenwickTree {
    private int[] tree;
    private int maxVal;
    
    public FenwickTree(int maxVal) {
        this.maxVal = maxVal;
        tree = new int[maxVal + 1];
    }
    
    public void update(int index, int delta) {
        while (index <= maxVal) {
            tree[index] += delta;
            index += index & (-index);
        }	}	public long query(int index) {		long sum = 0;		while (index > 0) {			sum += tree[index];			index -= index & (-index);		}		return sum;	}	}	# @lc code=end