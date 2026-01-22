#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

// @lc code=start
class Solution {
public:
    int minLength(string s,intnumops){
        int ns=s.length();
        // helper lambda : check whether target 'len' achievable
        auto check=[](string &str,intlen,intbudget)->bool{
            const int INF=100000000;
            // dp arrays : current ending bit ( idx ), streak
            vector<vector<int>>dpCurr(,(vector<int>(len+,INF))); // indices use streak values ..len
            // initialize first position
            int bFirst=str[]-'';
            dpCurr[bFirst][]=;// match existing bit
            dpCurr[-bFirst][]=;// flipped bit
            
            for(int idx= ; idx<str.size(); ++idx){
                vector<vector<int>>dpNext(,(vector<int>(len+,INF)));
                int origBit=str[idx]-'';
                
                for(int prevBit= ; prevBit< ; ++prevBit){
                    for(int streak= ; streak<=len;++streak){
                        int curVal=dpCurr[prevBit][streak];
                        if(curVal>=INF ) continue;
                        // try putting next bit 'newBit'
                        for(int newBit= ;newBit<;++newBit){
                            int addCost =(newBit!=origBit)? :;
                            int newStreak;
                            if(newBit!=prevBit){
                                newStreak =;
                            }else{
                                newStreak =streak+;
                                if(newStreak &gt; len ) continue;// exceed limit?/* skip */}/*else*/}/*if*//*else*//*skip*//*skip*//*skip*//*skip*//*skip*//*skip*//*skip*//*skip*//*skip*/}\";\"\"\"\"\"\"\"\"\"\"\"\"\"\" \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ }}}}}\}\\";\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\}\\\\";\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\}\\\\\\\\";\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\}\\\\\\\\";\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\}\\\\\\\\";\\\\\\\\}\\\\\\\\";}"});}}}}}"";}}}}}}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"")}}"