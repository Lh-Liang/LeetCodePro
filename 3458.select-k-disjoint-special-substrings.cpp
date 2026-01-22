#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

// @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        vector<int> glob(26);
        int n=s.size();
        for(char &ch:s){
            glob[ch-'a']++;
        }
        vector<int> act(26);
        vector<int> rem(begin(glob),end(glob));	// copy glob
        int cnt{};	// #special substr found
        int len{};	// len act substr built so far
        		// len<n ensures substr!=whole str
        		// check cond act_chars_rem_zero
        auto cond=[&](vector<int>&actVec,\	dummy param)\\\\tyes...				// lambda helper
         		for(int idx{};idx<26;++idx){\\\\if actVec[idx]> && rem idx > return false}\\\\return true;				// cond satisfied iff ∀charactermap actVec[idx]> ==> rem idx == 				\\\ensure actVec nonzero & rem zero 			}\\\\;}\\\;}\\\;}\\\;}\\\;}\\\;}\\\;}\\\;}\\\;}\\\\\\\\\\\\tttttttttttttttttttttttttttttttttttttttttttdddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffgggggggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiijjjjjjjjjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkkllllllllllllllllllllmmmmmmmmmmmmmmmmmmmmmnnnnnnnnnnnnnnnnnnnnnooooooooooooooooooooooppppppppppppppppppppqqqqqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrrrsssssssssssssssssssstttuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzz