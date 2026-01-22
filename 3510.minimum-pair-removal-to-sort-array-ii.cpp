#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        
        vector<long long> vals(n);
        for (int i = 0; i < n; i++) {
            vals[i] = nums[i];
        }
        
        vector<int> nxt(n), prv(n);
        for (int i = 0; i < n; i++) {
            nxt[i] = i + 1;
            prv[i] = i - 1;
        }
        
        vector<bool> deleted(n, false);
        
        int badCount = 0;
        for (int i = 0; i < n - 1; i++) {
            if (vals[i] > vals[i + 1]) {
                badCount++;
            }
        }
        
        if (badCount == 0) return 0;
        
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        
        for (int i = 0; i < n - 1; i++) {
            pq.push({vals[i] + vals[i + 1], i});
        }
        
        int ops = 0;
        while (badCount > 0) {
            auto [sum, leftIdx] = pq.top();
            pq.pop();
            
            if (deleted[leftIdx]) continue;
            int rightIdx = nxt[leftIdx];
            if (rightIdx >= n || deleted[rightIdx]) continue;
            if (vals[leftIdx] + vals[rightIdx] != sum) continue;
            
            ops++;
            
            if (vals[leftIdx] > vals[rightIdx]) badCount--;
            
            int prevIdx = prv[leftIdx];
            if (prevIdx >= 0 && !deleted[prevIdx]) {
                if (vals[prevIdx] > vals[leftIdx]) badCount--;
            }
            
            int nextRightIdx = nxt[rightIdx];
            if (nextRightIdx < n && !deleted[nextRightIdx]) {
                if (vals[rightIdx] > vals[nextRightIdx]) badCount--;
            }
            
            vals[leftIdx] = sum;
            deleted[rightIdx] = true;
            
            nxt[leftIdx] = nextRightIdx;
            if (nextRightIdx < n) prv[nextRightIdx] = leftIdx;
            
            if (prevIdx >= 0 && !deleted[prevIdx]) {
                if (vals[prevIdx] > vals[leftIdx]) badCount++;
                pq.push({vals[prevIdx] + vals[leftIdx], prevIdx});
            }
            if (nextRightIdx < n && !deleted[nextRightIdx]) {
                if (vals[leftIdx] > vals[nextRightIdx]) badCount++;
                pq.push({vals[leftIdx] + vals[nextRightIdx], leftIdx});
            }
        }
        
        return ops;
    }
};
# @lc code=end