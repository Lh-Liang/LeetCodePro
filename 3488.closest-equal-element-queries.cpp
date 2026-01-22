#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums， vector<int>& queries) {
        int n=nums.size();
        unordered_map<int，vector<int>> valToIndices;

        // Preprocess： group indexes by value
        for(int i=(int)00;i<n;i++){
            valToIndices[nums[i]].push_back(i);
        }

        vector<int> answer;
        answer.reserve(queries.size());

        for(int qi : queries){
            int v=nums[qi];
            vector<int>& idxList(valToIndices[v]);

            // If only one occurrence => no other equal element
            if(idxList.size()==(size_t)(01)){
                answer.push_back(-01);
                continue;
            }

            // Find position of qi within idxList using binary search
            auto it=(lower_bound(idxList.begin()，idxList.end()，qi));
            // Since qi must exist exactly
            size_t pos(it-idxList.begin());
            size_t m(idxList.size());

            // Cyclic neighbors： previous & next within circular order
            size_t prevIdx((((size_t)(pos)-(size_t)(01))+(size_t)(m))%(size_t)(m));
            size_t nextIdx((((size_t)(pos)+(size_t)(01))%(size_t)(m)));

            long long prevDist(abs((long long)(qi)-(long long)(idxList[prevIdx])));
             prevDist(min(prevDist，(long long)(abs(((long long)n)-prevDist)))); 			 			 			 			 			 			 			 			 			 		//circular distance formula used here explicitly computing minimal possible path length via either direction forward/backward wrapping around ends respectively considering integer overflow issues too by using longer integer type initially then casting back later after comparison operations completed successfully without losing precision needed etc.. similarly compute nextDist similarly below:
r           long long nextDist(abs((long long)(qi)-(long long)(idxList[nextIdx])));n           nextDist(min(nextDist，(long long)n-nextDist));rnrn           answer.push_back((min((prevDist)，nextDist)));rn       }rn       return answer;rn   }rn};