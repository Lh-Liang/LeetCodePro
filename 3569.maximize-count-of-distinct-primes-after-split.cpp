//
// @lc app=leetcode id=3569 lang=cpp
//
// [3569] Maximize Count of Distinct Primes After Split
//

// @lc code=start
class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int size = n - 1;
        
        const int MAX_VAL = 100001;
        vector<bool> isPrime(MAX_VAL, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i < MAX_VAL; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < MAX_VAL; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        vector<int> tree(4 * size + 10, 0);
        vector<int> lazy(4 * size + 10, 0);
        
        auto pushDown = [&](int node, int start, int end) {
            if (lazy[node] != 0 && start != end) {
                lazy[2*node] += lazy[node];
                tree[2*node] += lazy[node];
                lazy[2*node+1] += lazy[node];
                tree[2*node+1] += lazy[node];
                lazy[node] = 0;
            }
        };
        
        function<void(int, int, int, int, int, int)> rangeAdd = [&](int node, int start, int end, int l, int r, int val) {
            if (start > r || end < l) return;
            if (start >= l && end <= r) {
                tree[node] += val;
                lazy[node] += val;
                return;
            }
            pushDown(node, start, end);
            int mid = (start + end) / 2;
            rangeAdd(2*node, start, mid, l, r, val);
            rangeAdd(2*node+1, mid+1, end, l, r, val);
            tree[node] = max(tree[2*node], tree[2*node+1]);
        };
        
        unordered_map<int, set<int>> primePositions;
        
        auto updatePrime = [&](int p, int idx, bool isAdd) {
            auto& positions = primePositions[p];
            
            int oldMin = positions.empty() ? -1 : *positions.begin();
            int oldMax = positions.empty() ? -1 : *positions.rbegin();
            bool wasEmpty = positions.empty();
            
            if (!wasEmpty && oldMin < oldMax) {
                int left = max(1, oldMin + 1);
                int right = min(size, oldMax);
                if (left <= right) rangeAdd(1, 1, size, left, right, -1);
            }
            
            if (isAdd) positions.insert(idx);
            else positions.erase(idx);
            
            int newMin = positions.empty() ? -1 : *positions.begin();
            int newMax = positions.empty() ? -1 : *positions.rbegin();
            bool isNowEmpty = positions.empty();
            
            if (wasEmpty && !isNowEmpty) rangeAdd(1, 1, size, 1, size, 1);
            else if (!wasEmpty && isNowEmpty) rangeAdd(1, 1, size, 1, size, -1);
            
            if (!isNowEmpty && newMin < newMax) {
                int left = max(1, newMin + 1);
                int right = min(size, newMax);
                if (left <= right) rangeAdd(1, 1, size, left, right, 1);
            }
        };
        
        for (int i = 0; i < n; i++) {
            if (isPrime[nums[i]]) {
                updatePrime(nums[i], i, true);
            }
        }
        
        vector<int> result;
        for (auto& q : queries) {
            int idx = q[0], val = q[1];
            
            if (nums[idx] != val) {
                if (isPrime[nums[idx]]) updatePrime(nums[idx], idx, false);
                nums[idx] = val;
                if (isPrime[val]) updatePrime(val, idx, true);
            }
            
            result.push_back(tree[1]);
        }
        
        return result;
    }
};
// @lc code=end