//
// @lc app=leetcode id=3413 lang=java
//
// [3413] Maximum Coins From K Consecutive Bags
//
// @lc code=start
import java.util.*;
class Solution {
    public long maximumCoins(int[][] coins, int k) {
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> segs = new ArrayList<>();
        int n = coins.length;
        int prev = 0;
        for (int i = 0; i < n; ++i) {
            int l = coins[i][0], r = coins[i][1], c = coins[i][2];
            if (prev + 1 < l) {
                segs.add(new int[]{prev + 1, l - 1, 0});
            }
            segs.add(new int[]{l, r, c});
            prev = r;
        }
        long totalBags = 0;
        for (int[] seg : segs) {
            totalBags += (long)seg[1] - seg[0] + 1;
        }
        if (k > totalBags) return 0;
        int leftSeg = 0, rightSeg = 0;
        int leftPos = segs.get(0)[0], rightPos = segs.get(0)[0] - 1;
        long currSum = 0, maxSum = 0;
        int needed = k;
        while (needed > 0 && rightSeg < segs.size()) {
            int[] seg = segs.get(rightSeg);
            int segStart = Math.max(seg[0], rightPos + 1);
            int segLen = seg[1] - segStart + 1;
            int take = (int)Math.min(needed, segLen);
            currSum += (long)take * seg[2];
            rightPos += take;
            needed -= take;
            if (segStart + take - 1 == seg[1]) rightSeg++;
        }
        if (rightPos - leftPos + 1 == k) {
            maxSum = currSum;
        }
        while (rightPos < segs.get(segs.size() - 1)[1]) {
            int[] lseg = segs.get(leftSeg);
            currSum -= lseg[2];
            leftPos++;
            if (leftPos > lseg[1]) {
                leftSeg++;
                if (leftSeg < segs.size()) leftPos = segs.get(leftSeg)[0];
            }
            if (rightSeg < segs.size() && rightPos + 1 > segs.get(rightSeg)[1]) {
                rightSeg++;
            }
            if (rightSeg < segs.size()) {
                currSum += segs.get(rightSeg)[2];
            }
            rightPos++;
            if (rightPos - leftPos + 1 == k) {
                maxSum = Math.max(maxSum, currSum);
            }
        }
        return maxSum;
    }
}
// @lc code=end