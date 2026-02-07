# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        unordered_map<string, unordered_map<string, double>> graphDay1;
        unordered_map<string, unordered_map<string, double>> graphDay2;
        
        // Build graph for day 1
        for (int i = 0; i < pairs1.size(); ++i) {
            string start = pairs1[i][0];
            string end = pairs1[i][1];
            double rate = rates1[i];
            graphDay1[start][end] = rate;
            graphDay1[end][start] = 1.0 / rate;
        }
        
        // Build graph for day 2
        for (int i = 0; i < pairs2.size(); ++i) {
            string start = pairs2[i][0];
            string end = pairs2[i][1];
            double rate = rates2[i];
            graphDay2[start][end] = rate;
            graphDay2[end][start] = 1.0 / rate;
        }
        
        // BFS to find max amount after day 1 conversions
        unordered_map<string, double> maxAmountDay1;
        queue<pair<string, double>> q;
        q.push({initialCurrency, 1.0});
        maxAmountDay1[initialCurrency] = 1.0;
        while (!q.empty()) {
            auto [currentCurrency, currentAmount] = q.front(); q.pop();
            for (auto& [nextCurrency, rate] : graphDay1[currentCurrency]) {
                double newAmount = currentAmount * rate;
                if (newAmount > maxAmountDay1[nextCurrency]) {
                    maxAmountDay1[nextCurrency] = newAmount;
                    q.push({nextCurrency, newAmount});
                }
            }
        }
        
        // BFS to find max amount after day 2 conversions starting from results of day 1
        unordered_map<string, double> maxAmountDay2 = maxAmountDay1; // Initialize with results from day 1
        double result = maxAmountDay1[initialCurrency];
        queue<pair<string,double>> q2; // Prepare queue for second day's exploration
	for(auto&[currency,amount]:maxAmountDay1){if(amount>0){q2.push({currency,amount});}}	while(!q2.empty()){	auto[currentCurrency,currentAmount]=q2.front();q2.pop();for(auto&[nextCurrency,	rate]:graphDay2[currentCurrency]){
double newAmount=currentAmount*rate;if(newAmount>maxAmountDay2[nextCurren]){maxAmountDay2[nextCurrency]=newAmount;q.push({nextCurren,newAmoun});}if(newAmount>result&&nextCurrency==initialCurrency){result=newAmoun;}return result;}	}	}	}; # @lc code=end