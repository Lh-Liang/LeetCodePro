#
# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution {
public:
    int LOG = 18;
    vector<vector<int>> sparse;
    
    void buildSparse(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return;
        sparse.assign(LOG, vector<int>(n, 0));
        for (int i = 0; i < n; i++) sparse[0][i] = arr[i];
        for (int j = 1; j < LOG; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                sparse[j][i] = max(sparse[j-1][i], sparse[j-1][i + (1 << (j-1))]);
            }
        }
    }
    
    int queryMax(int l, int r) {
        if (l > r || sparse.empty()) return 0;
        int k = __lg(r - l + 1);
        return max(sparse[k][l], sparse[k][r - (1 << k) + 1]);
    }
    
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        int totalOnes = count(s.begin(), s.end(), '1');
        
        vector<array<int, 2>> segs;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            segs.push_back({i, j - 1});
            i = j;
        }
        
        int m = segs.size();
        
        vector<int> pairSum, oneStart, oneEnd, leftStart, rightEnd;
        
        int firstZero = (s[0] == '0') ? 0 : 1;
        for (int i = firstZero; i + 2 < m; i += 2) {
            int z1 = i, z2 = i + 2;
            int oneIdx = i + 1;
            int sz1 = segs[z1][1] - segs[z1][0] + 1;
            int sz2 = segs[z2][1] - segs[z2][0] + 1;
            pairSum.push_back(sz1 + sz2);
            oneStart.push_back(segs[oneIdx][0]);
            oneEnd.push_back(segs[oneIdx][1]);
            leftStart.push_back(segs[z1][0]);
            rightEnd.push_back(segs[z2][1]);
        }
        
        int numPairs = pairSum.size();
        
        if (numPairs == 0) {
            return vector<int>(queries.size(), totalOnes);
        }
        
        buildSparse(pairSum);
        
        vector<int> answer;
        for (auto& q : queries) {
            int l = q[0], r = q[1];
            
            int lo = lower_bound(oneStart.begin(), oneStart.end(), l + 1) - oneStart.begin();
            int hi = upper_bound(oneEnd.begin(), oneEnd.end(), r - 1) - oneEnd.begin() - 1;
            
            int bestGain = 0;
            
            if (lo <= hi) {
                int lo2 = lower_bound(leftStart.begin() + lo, leftStart.begin() + hi + 1, l) - leftStart.begin();
                int hi2 = upper_bound(rightEnd.begin() + lo, rightEnd.begin() + hi + 1, r) - rightEnd.begin() - 1;
                
                if (lo2 <= hi2) {
                    bestGain = max(bestGain, queryMax(lo2, hi2));
                }
                
                for (int i = lo; i < min(lo2, hi + 1); i++) {
                    int idx = firstZero + i * 2;
                    int leftGain = segs[idx][1] - l + 1;
                    int rightGain;
                    if (rightEnd[i] <= r) {
                        rightGain = segs[idx+2][1] - segs[idx+2][0] + 1;
                    } else {
                        rightGain = r - segs[idx+2][0] + 1;
                    }
                    bestGain = max(bestGain, leftGain + rightGain);
                }
                
                for (int i = max(hi2 + 1, lo); i <= hi; i++) {
                    int idx = firstZero + i * 2;
                    int leftGain;
                    if (leftStart[i] >= l) {
                        leftGain = segs[idx][1] - segs[idx][0] + 1;
                    } else {
                        leftGain = segs[idx][1] - l + 1;
                    }
                    int rightGain = r - segs[idx+2][0] + 1;
                    bestGain = max(bestGain, leftGain + rightGain);
                }
            }
            
            answer.push_back(totalOnes + bestGain);
        }
        
        return answer;
    }
};
# @lc code=end