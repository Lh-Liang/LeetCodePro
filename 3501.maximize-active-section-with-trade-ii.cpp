#
# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#

#include <vector>
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        vector<int> result;
        
        for (auto& query : queries) {
            int l = query[0], r = query[1];
            string sub = "1" + s.substr(l, r - l + 1) + "1";
            int maxActive = 0;
            
            // Function to count active sections ('1')
            auto countActiveSections = [](const string& str) {
                int count = 0;
                bool inSection = false;
                for (char c : str) {
                    if (c == '1') {
                        if (!inSection) {
                            inSection = true;
                            count++;
                        }
                    } else {
                        inSection = false;
                    }
                }
                return count;
            };
            
            // Initial count of active sections without any trade
            int initialActiveSections = countActiveSections(sub);
            maxActive = initialActiveSections; // Initialize maxActive with current active sections count

            // Traverse through the string and consider possible trades:
auto tryTrade=[&](int start,int end){int beforeTrade=countActiveSections(sub);for(int i=start;i<end;++i){sub[i]='0';}int afterTrade=countActiveSections(sub);maxActive=max(maxActive,afterTrade);for(int i=start;i<end;++i){sub[i]='1';}};int n=sub.size();for(int i=0;i<n;){if(sub[i]=='0'){int j=i;while(j<n&&sub[j]=='0'){j++;}if(i>0&&j<n){tryTrade(i,j);}i=j;}else{i++;}}result.push_back(maxActive);}return result;};// @lc code=end