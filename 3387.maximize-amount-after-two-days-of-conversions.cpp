#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        unordered_map<string, double> maxCurrencyDay1;
        maxCurrencyDay1[initialCurrency] = 1.0;
        
        // Dynamic programming approach for Day 1 conversions
        for (int iteration = 0; iteration < pairs1.size(); ++iteration) {
            for (int i = 0; i < pairs1.size(); ++i) {
                string from = pairs1[i][0], to = pairs1[i][1];
                double rate = rates1[i];
                if (maxCurrencyDay1.find(from) != maxCurrencyDay1.end()) {
                    maxCurrencyDay1[to] = max(maxCurrencyDay1[to], maxCurrencyDay1[from] * rate);
                }
            }
        }
        
        double maxAmountAfterDay2 = 0.0;
        
        // Use results from Day 1 to start conversions for Day 2
        for (auto& [currency, amount] : maxCurrencyDay1) {
            unordered_map<string, double> maxCurrencyDay2;
            maxCurrencyDay2[currency] = amount;
            
            // Dynamic programming approach for Day 2 conversions
            for (int iteration = 0; iteration < pairs2.size(); ++iteration) {
                for (int i = 0; i < pairs2.size(); ++i) {
                    string from = pairs2[i][0], to = pairs2[i][1];
                    double rate = rates2[i];
                    if (maxCurrencyDay2.find(from) != maxCurrencyDay2.end()) {
                        maxCurrencyDay2[to] = max(maxCurrencyDay2[to], maxCurrencyDay2[from] * rate);
                    }
                }
            }
            
            // Obtain maximum in initial currency after all possible conversions on both days
            if (maxCurrencyDay2.find(initialCurrency) != maxCurrencyDay2.end()) {
                maxAmountAfterDay2 = max(maxAmountAfterDay2, maxCurrencyDay2[initialCurrency]);
            }
        }
        return maxAmountAfterDay2;
    }
}; 
ewline # @lc code=end