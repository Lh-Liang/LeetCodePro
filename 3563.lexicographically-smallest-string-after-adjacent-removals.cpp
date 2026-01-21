#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
class Solution {
public:
    string lexicographicallySmallestString(string s) {
        queue<string> q;
        unordered_set<string> visited;
        string result = s;
        
        q.push(s);
        visited.insert(s);
        
        while (!q.empty()) {
            string curr = q.front();
            q.pop();
            
            if (curr < result) {
                result = curr;
            }
            
            // Try all possible removals
            for (int i = 0; i < (int)curr.length() - 1; i++) {
                if (isConsecutive(curr[i], curr[i+1])) {
                    string next = curr.substr(0, i) + curr.substr(i+2);
                    if (visited.find(next) == visited.end()) {
                        visited.insert(next);
                        q.push(next);
                    }
                }
            }
        }
        
        return result;
    }
    
private:
    bool isConsecutive(char a, char b) {
        int diff = abs(a - b);
        return diff == 1 || diff == 25; // 25 is for 'a' and 'z'
    }
};
# @lc code=end