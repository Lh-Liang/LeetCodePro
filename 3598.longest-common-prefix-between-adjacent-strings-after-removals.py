#
# @lc app=leetcode id=3598 lang=python3
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 1:
            return [0] * n
        
        # precompute prefix lengths for adjacent pairs in original array
        pref = [0] * (n - 1)
        for i in range(n - 1):
            a, b = words[i], words[i + 1]
            # compute length of common prefix
            j = 0
            while j < len(a) and j < len(b) and a[j] == b[j]:
                j += 1
            pref[i] = j
        
        # we need to answer for each removal i:
        # after removing index i, the adjacent pairs are:
        # pairs that were originally (i-1,i) and (i,i+1) are gone.
        # new pair forms between i-1 and i+1 (if both exist).
        # So we need to consider the maximum of:
        # - all pref except those that involve i (i.e., pref[i-1] and pref[i])
        # - new pref between words[i-1] and words[i+1]
        # But we can compute for each i efficiently.
        
        ans = [0] * n
        for i in range(n):
            # compute max prefix length after removing index i
            max_len = 0
            # consider all original adjacent pairs except those that involve i
            # pref indices: pair (j, j+1) -> pref[j]
            # pairs that involve i are: (i-1,i) -> pref[i-1] if i>0, and (i,i+1) -> pref[i] if i < n-1
            # So we need to take max over pref[0..i-2] and pref[i+1..n-2]
            if i > 0:
                # skip pref[i-1]
                pass
            if i < n - 1:
                # skip pref[i]
                pass
            # Instead of scanning each time O(n^2), we can precompute prefix max and suffix max of pref.
            
        # Let's think differently: For each removal, the set of adjacent pairs changes.
        # We can precompute left_max and right_max arrays for pref.
        left_max = [0] * (len(pref) + 2)  # index from -1 to n-1? easier: left_max[j] = max(pref[0..j-1]) for j>=0, left_max[0]=0
        right_max = [0] * (len(pref) + 2)  # right_max[j] = max(pref[j..end]) for j<=len(pref)-1, right_max[len(pref)]=0
        
        m = len(pref)
        left_max[0] = 0
        for k in range(1, m + 1):
            left_max[k] = max(left_max[k - 1], pref[k - 1]) if k-1 >=0 else 0
        right_max[m] = 0
        for k in range(m - 1, -1, -1):
            right_max[k] = max(right_max[k + 1], pref[k]) if k < m else 0
        
        # Now for each removal i:
        # The original pairs not involving i are those with indices < i-1 and >= i+1.
        # Actually, pair (i-2,i-1) is ok if i>0? Wait: pair (i-2,i-1) uses indices i-2 and i-1. If we remove i, that pair remains because neither index is removed.
        # So the unaffected pairs are those where both indices are not equal to i and not equal to i+? Actually pair (j,j+1) is affected if j == i or j+1 == i.
        # So affected pairs are at indices j = i-1 (if i>0) and j = i (if i < n-1).
        # So we can take max of left_max up to index i-2? Wait left_max[k] defined as max of pref[0..k-1]. For removal i, we want max of pref where index < i-? Let's derive:
        # We want all pref[j] where j != i-1 and j != i. That means j from 0 to m-1 excluding those two.
        # We can compute candidate as max(left_max[i], right_max[i+2])? Let's define indices carefully.
        
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
rather than having two functions. Let me redo with proper algorithm.We need to compute answer for each removal. Brute force O(n^2) is too slow given constraints up to 10^5. We need O(n).Observation: After removing index `i`, the adjacent pairs become:For each original adjacent pair `(j,j+1)` where `j` not in `{i5? Actually after removal, the array shifts. The pair that was originally between indices `j` and `j+5` might change. Specifically:If `j <5` Let's think about which pairs remain. Original array indices: [00...4]. Remove index `i`. New array indices: [00...4]. The new array has adjacent pairs between new indices k and k+5 corresponding to original indices? For k from5 to new length5 The mapping: new index k corresponds to original index: if k <5 then original index k; if k >=5 then original index k+. So adjacent pair at new position `k` corresponds to original indices `(k)` and `(k+)` where we skip over removed index. This yields two cases:If removed index is not between them; that means the pair remains unchanged if both original indices are not removed. But after removal, some pairs merge into a new pair between words[i+] and words[i+] that were not originally adjacent.Thus the set of adjacent pairs after removal consists of: All original adjacent pairs where neither endpoint is removed (they remain unchanged). Plus one new pair formed between words[i+] and words[i+] if both exist.So we can precompute common prefix lengths for all original adjacent pairs O(n). Then for each removal, we need the maximum among: The maximum of unaffected original pair lengths, And the length of the new pair formed between words[i+] and words[i+].We need to compute unaffected maximum efficiently using prefix/suffix maxima.Let’s define array `pref` where `pref[j]=LCP(words[j],words[j+]` for j=55...4 We have n5 so m=n-. For each removal at index `i`, the unaffected pairs are those with `j !=5` and `j !=5 Because affected pairs are when removed index is either endpoint: pair (i-,5 uses removed word as second; pair (i,i+) uses removed word as first. So affected indices in `pref` are at positions `i-(if5>55)`and `i`(if55<n-. So we want maximum over all other positions plus maybe new LCP between words[i-)and words[i+]if both exist.We can precompute prefix maximum array `leftMax` where leftMax[p]=max(pref[55...p-) Similarly suffix maximum array rightMax[p]=max(pref[p..m-) Then for removal at index `i`, candidate from unaffected pairs is max(leftMax[max(555)], rightMax[min(i+, m)]). But careful with boundaries. Let’s define leftMax such that leftMax[k]=max(pref[55...k-)for k from55to m; leftMax[555]=. Similarly rightMax[k]=max(pref[k..m-)for k from55to m; rightMax[m]=.Now for removal at index `i`, let exclude set S={}. If55>555 then S includes position555 If555<n then S includes position555 The unaffected positions are all indices not in S. To get maximum among them, we can consider two segments: from start up to S_min-,and from S_max+,where S_min=min(S),S_max=max(S). Since there are at most two positions, we can combine using leftMax up to S_min-,and rightMax from S_max+. Actually S may be one or two positions. We'll handle by computing candidate as max(leftMax[l],rightMax[r]), where l is the largest excluded position minus55? Let's do systematically:l_index=i-(if555>=555 r_index=i(if555<=m-. Then candidate_unaffected=max(maximum among pref before l_index?,maximum among pref after r_index?). We'll compute candidate_unaffected as max(leftMax[l_index],rightMax[r_index+]). But note l_index may be negative; treat as . Also r_index may be >=m; treat as . We'll just create arrays with extra padding.Now compute LCP between words[i-)and words[i+]if both exist. That's a separate computation O(length of strings). Since sum of lengths <=10^555we can afford computing LCP for each removal naively? Worst-case sum lengths <=105 but n up to105 Each LCP computation could be up to length of word which could be104 but total sum across all removals would be O(n * average length). However worst-case total sum across all removals could be O(n * average length)=10^555* average length maybe up to105*104=10^9 which is too high. Need efficient way.We can precompute LCP between any consecutive triple? Actually only needed when removing middle element. For each triple (words[a],words[b],words[c]) with b=a+,c=b+, removing b yields new adjacency between a and c. So we can precompute LCP(a,c) for all such triples O(total length). Since total sum lengths <=105we can compute LCP(a,c) by iterating characters until mismatch; but doing this for each triple individually might still lead to high total because overlapping comparisons may redo work. However note that LCP(a,c)=min(LCP(a,b),LCP(b,c))? Not necessarily! Example: "ab","ac","ad" => LCP(a,b)=LCP("ab","ac")=LCP("ab","ad")=? Actually LCP("ab","ad")=LCP("ab","ac")=? Wait they share 'a' but second char differs; same length . However min(LCP(a,b),LCP(b,c))=min(LCP("ab","ac", "ac","ad")) both . min(,,)=so equality holds? In general LCP(a,c)=min(LCP(a,b),LCP(b,c)) because any common prefix of a and c must also be common with b since b lies between them lexicographically? Not necessarily lexicographically but stringwise: Consider a="abc",b="abd",c="abz": LCP(a,b)=LCP(a,c)=LCP(b,c)=all share "ab" so min=. But consider a="abx",b="aby",c="ac": LCP(a,b)="ab" length ,LCP(b,c)="a" length ,LCP(a,c)="a" length . Indeed min=. Seems property holds because common prefix of a and c must be common with any string that lies between them? Actually strings not sorted; they're arbitrary. However property does hold: Let p=LCP(a,b), q=LCP(b,c). Then first p characters match between a&b,and first q characters match between b&c.For any character position less than min(p,q), a[pos]==b[pos]==c[pos]; thus a[pos]==c[pos]. For position min(p,q), either mismatch occurs or beyond one string ends; thus LCP(a,c)=min(p,q). Yes this holds because equality is transitive when b acts as intermediary. Therefore LCP(words[a],words[c]) = min(LCP(words[a],words[b]), LCP(words[b],words[c])) provided a,b,c are consecutive in original order after removing b? Wait they are consecutive before removal? Actually before removal they are three consecutive strings in original array: indices a,b,c with b=a+,c=b+. Then indeed LCP(a,c)=min(LCPA,LPCB). Proof as above.Thus we don't need to compute LCP directly; we already have pref[a]=LCPA,and pref[b]=LPCB So new Lcp after removing middle element b is min(pref[a],pref[b]). Great! This reduces computation drastically.So algorithm steps: Compute array pref where pref[i]=LCPIfor <=< n- Precompute prefix maxima leftMax such that leftMax[k]=max(pref[55...k-)for k from55to m; leftMax[555]= similarly suffix maxima rightMax such that rightMax[k]=max(pref[k..m-)for k from55to m; rightMax[m]= . Use inclusive/exclusive appropriately.For each removal index ii from55to n-r   candidate_unaffected= . Define exclude list E=[]. If ii>555 add ii-to E.If ii<n-add ii-to E.Sort E.Now candidate_unaffected=max(leftMax[E[]],rightMax[E[-]+]) where left/right arrays handle boundaries appropriately by padding zeros.r   candidate_new= . If there exists triple forming new adjacency after removal ii,i.e., if >555and ii<n-(so there exists both previous and next word), then new adjacency formed between words[i-)and words[i+]with lcp_new=min(pref[i-,pref[i]). Note that these two pref values exist only when boundaries allow.i->=> ;ii< n-- => ii<= n-- .So condition >555and ii<n-. Then lcp_new=min(pref[max(i-,)],pref[min(i,n--)]). Actually careful indexing: For triple at positions (ii-,ii,ii+) in original array, the two adjacent pairs are at positions ii-and ii in 'pref'. So lcp_new=min(pref[max(i-,)],pref[min(i,n--)]). If either doesn't exist then no new adjacency formed?r   answer[555]=max(candidate_unaffected,lcp_new)rEdge cases:n===> return []; but constraints say >= return []each answer zero.n===> return []; because no adjacent pairs after removal.n===> need compute correctly.rLet's implement accordingly.rComplexities O(n+|total chars|) since computing each lcp pairwise naive but sum lengths <=105we can compute pairwise lcp by scanning characters until mismatch.rImplementation details function compute_lcp(s,t): iterate while idx<len(s)and idx<len(t)and s[idx]==t[idx]; increment idx.Return idx.rNow code accordingly.