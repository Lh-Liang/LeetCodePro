#
# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#
# @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    vector<vector<int>> children;
    vector<int> vals;
    
    bool hasDuplicateDigits(int num) {
        int digitCount[10] = {0};
        if (num == 0) return false;
        while (num > 0) {
            int d = num % 10;
            digitCount[d]++;
            if (digitCount[d] > 1) return true;
            num /= 10;
        }
        return false;
    }
    
    int getDigitMask(int num) {
        int mask = 0;
        if (num == 0) return 1;
        while (num > 0) {
            int d = num % 10;
            mask |= (1 << d);
            num /= 10;
        }
        return mask;
    }
    
    map<int, long long> dfs(int node, vector<long long>& maxScore) {
        map<int, long long> dp;
        dp[0] = 0;
        
        if (!hasDuplicateDigits(vals[node])) {
            int nodeMask = getDigitMask(vals[node]);
            dp[nodeMask] = vals[node];
        }
        
        for (int child : children[node]) {
            map<int, long long> childDp = dfs(child, maxScore);
            map<int, long long> newDp;
            
            for (auto& [mask1, score1] : dp) {
                newDp[mask1] = max(newDp[mask1], score1);
                
                for (auto& [mask2, score2] : childDp) {
                    if ((mask1 & mask2) == 0) {
                        int newMask = mask1 | mask2;
                        newDp[newMask] = max(newDp[newMask], score1 + score2);
                    }
                }
            }
            dp = newDp;
        }
        
        long long maxVal = 0;
        for (auto& [mask, score] : dp) {
            maxVal = max(maxVal, score);
        }
        maxScore[node] = maxVal;
        
        return dp;
    }
    
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        int n = vals.size();
        this->vals = vals;
        children.resize(n);
        vector<long long> maxScore(n);
        
        for (int i = 1; i < n; i++) {
            children[par[i]].push_back(i);
        }
        
        dfs(0, maxScore);
        
        long long totalSum = 0;
        for (long long score : maxScore) {
            totalSum = (totalSum + score) % MOD;
        }
        
        return (int)totalSum;
    }
};
# @lc code=end