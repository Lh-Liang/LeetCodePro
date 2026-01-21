#
# @lc app=leetcode id=3470 lang=cpp
#
# [3470] Permutations IV
#
# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        const long long MAX_K = 1000000000000000LL;
        
        vector<int> result;
        vector<int> available;
        for (int i = 1; i <= n; i++) {
            available.push_back(i);
        }
        
        auto factorial = [&](int x) -> long long {
            long long res = 1;
            for (int i = 1; i <= x; i++) {
                res *= i;
                if (res > MAX_K) return MAX_K + 1;
            }
            return res;
        };
        
        auto countPerms = [&](const vector<int>& nums, bool needOdd) -> long long {
            if (nums.empty()) return 1;
            
            int oddCount = 0, evenCount = 0;
            for (int num : nums) {
                if (num % 2 == 1) oddCount++;
                else evenCount++;
            }
            
            int len = nums.size();
            int oddPosCount = 0, evenPosCount = 0;
            bool currentNeedOdd = needOdd;
            for (int i = 0; i < len; i++) {
                if (currentNeedOdd) oddPosCount++;
                else evenPosCount++;
                currentNeedOdd = !currentNeedOdd;
            }
            
            if (oddPosCount != oddCount || evenPosCount != evenCount) {
                return 0;
            }
            
            long long oddFact = factorial(oddCount);
            long long evenFact = factorial(evenCount);
            if (oddFact > MAX_K || evenFact > MAX_K) return MAX_K + 1;
            if (oddFact > MAX_K / evenFact) return MAX_K + 1;
            return oddFact * evenFact;
        };
        
        bool needOdd = false;
        
        for (int pos = 0; pos < n; pos++) {
            vector<int> validChoices;
            
            if (pos == 0) {
                for (int num : available) {
                    validChoices.push_back(num);
                }
            } else {
                for (int num : available) {
                    bool isOdd = (num % 2 == 1);
                    if ((needOdd && isOdd) || (!needOdd && !isOdd)) {
                        validChoices.push_back(num);
                    }
                }
            }
            
            bool found = false;
            for (int choice : validChoices) {
                vector<int> remaining;
                for (int num : available) {
                    if (num != choice) remaining.push_back(num);
                }
                
                bool nextNeedOdd = !(choice % 2 == 1);
                long long count = countPerms(remaining, nextNeedOdd);
                
                if (count == 0) continue;
                
                if (k <= count) {
                    result.push_back(choice);
                    available = remaining;
                    needOdd = nextNeedOdd;
                    found = true;
                    break;
                } else {
                    k -= count;
                }
            }
            
            if (!found) {
                return {};
            }
        }
        
        return result;
    }
};
# @lc code=end