//
// @lc app=leetcode id=3777 lang=cpp
//
// [3777] Minimum Deletions to Make Alternating Substring
//
// @lc code=start
class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        int n = s.length();
        
        // Convert to binary: 'A' = 0, 'B' = 1
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = (s[i] == 'B') ? 1 : 0;
        }
        
        // BIT for tracking transitions (diff[i] = 1 if arr[i] != arr[i-1])
        vector<int> bit(n + 1, 0);
        
        auto update = [&](int i, int delta) {
            for (++i; i <= n; i += i & (-i))
                bit[i] += delta;
        };
        
        auto prefixSum = [&](int i) -> int {
            int sum = 0;
            for (++i; i > 0; i -= i & (-i))
                sum += bit[i];
            return sum;
        };
        
        auto rangeSum = [&](int l, int r) -> int {
            if (l > r) return 0;
            return prefixSum(r) - (l > 0 ? prefixSum(l - 1) : 0);
        };
        
        // Initialize BIT with transition values
        for (int i = 1; i < n; i++) {
            if (arr[i] != arr[i-1]) {
                update(i, 1);
            }
        }
        
        vector<int> answer;
        
        for (auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                
                // Update transitions before flipping
                if (j > 0) {
                    bool wasDiff = (arr[j] != arr[j-1]);
                    bool willDiff = (1 - arr[j] != arr[j-1]);
                    if (wasDiff && !willDiff) update(j, -1);
                    else if (!wasDiff && willDiff) update(j, 1);
                }
                if (j + 1 < n) {
                    bool wasDiff = (arr[j+1] != arr[j]);
                    bool willDiff = (arr[j+1] != 1 - arr[j]);
                    if (wasDiff && !willDiff) update(j + 1, -1);
                    else if (!wasDiff && willDiff) update(j + 1, 1);
                }
                
                arr[j] = 1 - arr[j];
            } else {
                int l = q[1], r = q[2];
                int len = r - l + 1;
                // Number of runs = 1 + number of transitions in [l+1, r]
                int transitions = rangeSum(l + 1, r);
                int numRuns = 1 + transitions;
                answer.push_back(len - numRuns);
            }
        }
        
        return answer;
    }
};
// @lc code=end