#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        # Count characters in s
        cnt = Counter(s)
        # Check if a palindrome can be formed
        odd_count = sum(v % 2 for v in cnt.values())
        if odd_count > 1:
            return ""
        # We need to construct the lexicographically smallest palindrome > target.
        # Approach: generate the smallest palindrome from s, and then try to find next greater.
        # But we can directly construct by trying to build from left to right.
        # Since palindrome is symmetric, we can build first half (or first ceil(n/2) characters).
        # Let's think of constructing the palindrome as a string of length n.
        # We'll build the left half (first ceil(n/2) chars) and mirror to right.
        # We need to find the smallest palindrome lexicographically > target.
        # We can use backtracking with pruning.
        # Sort the available characters? Actually we need to consider counts.
        # Let's precompute sorted list of characters available.
        chars = sorted(cnt.keys())
        # We'll try to build the palindrome from left to right, ensuring we can complete.
        # At each position i (0-indexed, up to mid), we try placing a character c that is >= target[i] if we are matching prefix so far.
        # But we need strictly > target overall, so we need to consider when we deviate.
        # Let's define a recursive function that builds the left half and keeps track of whether the current prefix is already greater than target's prefix.
        # Since n <= 300, recursion depth up to 150 might be okay but we need efficient pruning.
        # We'll implement iterative construction with backtracking using stack or recursion.
        
        # Prepare list of characters with counts for backtracking.
        # We'll use a list of (char, count) pairs sorted.
        char_list = sorted(cnt.items())  # sorted by char
        
        # Convert to list for mutable counts
        freq = {c: v for c, v in char_list}
        
        # We'll store the result as list of chars for left half.
        res = []
        mid = (n + 1) // 2  # length of left half (including middle if odd)
        
        def backtrack(pos, greater):
            nonlocal res
            if pos == mid:
                # We have built left half. Now construct full palindrome and return True.
                return True
            
            # Determine which characters we can place at this position.
            available_chars = [c for c in chars if freq[c] > 0]
            if not greater:
                # Current prefix equals target's prefix so far. We need to place a character >= target[pos]
                min_char = target[pos]
                available_chars = [c for c in available_chars if c >= min_char]
            else:
                min_char = 'a'  # any character allowed, but we want smallest lexicographically
                
            for c in available_chars:
                if not greater and c == target[pos]:
                    next_greater = False
                else:
d                    next_greater = True or c > target[pos]  Actually: if c > target[pos], then it's greater; if equal, not greater yet.
d                    Let's compute correctly: next_greater = greater or (c > target[pos])
d                But careful: greater is boolean indicating if prefix already larger. So:
d                    new_greater = greater or (c > target[pos])
d                However, when greater is False and c == target[pos], new_greater remains False.
d                When greater is False and c > target[pos], new_greater becomes True.
d                When greater is True, new_greater remains True regardless of c.
d                So:
d                    new_greater = greater or (c > target[pos])
d                
d                Now we need to check feasibility after placing c.
d                We need to decrement count for c by 1 or 2? Because palindrome: placing at left half uses one occurrence. If n is odd and pos == mid-1 (middle), then only one occurrence used. Otherwise, two occurrences used (left and right).
d                Actually: For each character placed in left half except possibly the middle character (if n odd), we consume two occurrences: one on left and its mirror on right. For middle character (if n odd), consume one occurrence.
d                So let's compute remaining counts accordingly.
d                
d                Implementation plan: We maintain freq counts total. When placing char c at position pos:
d                    if n % 2 == 1 and pos == mid - 1:   # middle position
                        needed = 1
                    else:
d                        needed = 2
                    if freq[c] < needed:
d                        continue
                    freq[c] -= needed
                    res.append(c)
d                    if backtrack(pos+1, new_greater):
d                        return True
                    res.pop()
d                    freq[c] += needed
            return False
            
d            However this approach might be too slow? n <=300, but number of distinct chars <=26. The branching factor limited. Should be fine.
d            
d            Need to handle case when pos >= len(target)? Actually target length equals n. But our left half length mid might be less than n. However when comparing prefix, we compare with target[:mid]? Wait: The palindrome is built symmetrically. The left half determines the whole string. The lexicographic comparison between full palindrome and target depends on entire string. However because of symmetry, comparing left half might not be sufficient? Example: Suppose left half "ab" and right half "ba" gives "abba". Compare with target "acaa"? Actually lexicographic order compares character by character from start. So indeed comparing full string is same as comparing first differing character. Since the palindrome is symmetric, but the comparison with target does not have symmetry constraints. So we must compare the entire constructed string with target. However during construction of left half only, we don't know the right half until after construction. But we can compute the full string after constructing left half. However during backtracking we need to know whether at current prefix position pos (in left half) the decision leads to a full string that could be > target. This is tricky because the right half influences later characters beyond mid. For example, suppose left half prefix matches target's first pos characters exactly, but later in right half it could differ. However since right half is determined by left half reversed (except middle), once left half is fixed, entire string is fixed. So we can simulate comparison during backtracking by constructing the full string after building left half completely. That's what backtrack does when pos==mid it returns True only if full string > target? Wait requirement: strictly greater than target. So after building left half completely, we must check that the full palindrome > target. In backtrack above I returned True immediately without checking >target? I assumed that during building we ensured that either prefix already greater or at last step it becomes greater? Actually my condition "greater" tracks whether current prefix (of length pos) is already strictly greater than target[:pos]. But this only accounts for prefix up to pos; however after building full palindrome, even if prefix equals up to mid-1 but later characters in right half might make it less than target overall? Example: Consider palindrome "abba" vs target "abca". Left half "ab" matches first two chars 'a','b'. Prefix equal so far; then right half 'b','a' gives third char 'b' vs 'c' -> less => overall smaller. So my approach would have considered prefix equal up to pos=2 (mid=2) and returned True because pos==mid without checking further? That would incorrectly accept "abba" which is less than "abca". Therefore I must compare entire constructed string with target after building left half.
adjustment: When pos==mid, construct full palindrome and check if it > target; only then return True.nAlso during backtracking I can prune using more precise condition: At each step pos < mid, I know that future characters are constrained by remaining counts; but I also know that even if current prefix equals so far, there might be no way to make final string >target because remaining positions might be forced smaller due to limited chars? That's more complex.nSimpler approach: Generate all palindromic permutations? Not feasible due to n up to 300.nAlternative approach: Construct smallest possible palindrome from s (call it base). If base >target return base; else find next permutation of palindrome similar to next_permutation algorithm but on palindrome structure.nWe can treat palindrome as a sequence of length n built from multiset of characters such that first ceil(n/2) characters sorted non-decreasing? Actually smallest lexicographic palindrome uses smallest possible characters from front.nSo compute smallest palindrome possible from s; then try to find next larger palindrome by adjusting from middle outward similar to next_permutation on first half.nLet's try that method:nStep1: Check feasibility.nStep2: Build smallest palindrome by taking counts; for left half positions from 0..mid-1 assign smallest available character that leaves enough counts for remaining positions.nThat yields smallest palindromic permutation.nIf this smallest_palindrome >target return it.nOtherwise we need next larger palindromic permutation.nWe can think of generating palindromes in lex order by generating all possible first halves sorted lexicographically? Again combinatorial explosion.nBut since alphabet size small (26), maybe iterate through possible first halves via recursion as before but now prune heavily using condition that final string must be >target.nWe can also incorporate condition during building: For each position i in [0..mid-1], let L be built prefix length i; R will be suffix determined later.nWe can compare built prefix with target[:i]; if equal continue; if already greater then any completion yields larger than target? Not necessarily because later characters could make it smaller? Actually once you have a larger character at some early position, regardless of later chars the whole string will be larger because lexicographic order compares first differing character. So yes! If at some position i < n where our constructed char at i is larger than target[i], then entire final string will be larger regardless of rest. Conversely if smaller then final string will be smaller regardless of rest.nThus during construction of full string character by character (not just left half), once you have a larger char at some index you can fill remaining positions with smallest possible characters.nBut constructing full string symmetrically means indices beyond mid are determined by earlier indices.nHowever note that index i corresponds either in left half or right half; but since right half mirrors left except middle, the sequence of characters for indices >=mid are determined by earlier indices (<mid). So effectively when building left half positions sequentially from 0..mid-1 you also determine characters at mirrored positions in reverse order.nSo while building left-half positions sequentially you also implicitly determine characters at certain later indices:nFor i from 0..mid-1:n   corresponding mirrored index j = n-1-i.nIf i < j then both positions set simultaneously when placing char at i; j will get same char later automatically when mirroring.nSo you cannot independently set later indices after establishing early larger char because they are constrained by earlier choices.nnWait think differently:nWe want final constructed string ans[0..N-1]. It must satisfy ans[i]==ans[N-1-i]. And ans must use exactly counts from s.nnWe can build ans from both ends inward perhaps easier? Or build from center outward.nnGiven time constraints maybe implement backtracking with proper pruning using condition above about early larger char.nnLet's design recursion that builds ans index by index from 0..N-1 while respecting symmetry.nnWe maintain an array ans of length N initially empty places None.nnAt each index i from 0..N-1:n   If ans[i] already set (by mirror), skip.nn   Otherwise choose a character c such that:n      - enough count remainingnn      - If i < N-1-i then setting ans[i]=c also sets ans[N-1-i]=c requiring two copies unless i==N-1-i where only one copy.nn   And also ensure lexicographic condition:n      Let current_prefix be ans[0:i] concatenated with chosen c at position i.nn      Compare current_prefix with target[0:i+1]: If current_prefix <target[0:i+1] => invalid because even filling rest with smallest cannot catch up since first differing already smaller.nn      If current_prefix ==target[0:i+1] => continue with requirement that final must be strictly greater eventually.nn      If current_prefix >target[0:i+1] => then any valid completion works; so we should choose smallest possible c that satisfies this condition? Actually once larger already happen we want overall smallest lexicographic result satisfying >target => so choose smallest possible valid continuation thereafter.nnThus algorithm:nDefine recursive function dfs(i, greater): where i is current index being filled (0..N-1). 'greater' indicates whether already some earlier index made ans>target so far.nnIf i==N:n   Return True iff greater==True (since strict)>nnAt position i:n   If ans[i] already set due symmetry earlier skip dfs(i+1).nn   Determine mirrored index j=N-1-i.nn   needed=2 if i!=j else 1nn   Get list of candidate chars sorted ascending so that we try smaller ones first for lexicographically smallest result overall! But careful about ordering based on 'greater':nn   If not greater:n       candidate must satisfy:c >=target[i]n       Among those candidates try in ascending order because even though c>=target[i], picking larger than necessary may yield valid solution but not necessarily smallest overall because later positions matter? Actually since not yet greater we want minimal possible while still having chance eventually become strictly>target overall.Need also consider future constraints.So typical approach try candidates in ascending order regardless.If candidate equals target[i], then new_greater=False else True.So try candidates sorted ascending.For each candidate,n       Check feasibility:freq[c]>=needednn       Then place,freq-=needednn       new_greater=greater or(c>target[i])nn       Recurse dfs(i+1,new_greater)n       If true return Truen       Backtracknn   Else(greater==True): Then any candidate allowed.We want overall smallest result so try candidates sorted ascending regardless.Check feasibility,freq>=needed place etc.Recurse dfs(i+1,gTrue) since already greater remains true.If success return true.nnThis approach explores all possibilities but prunes heavily via early cutoff when candidate makes current_prefix<target[:i+1]. In code implementation,nwe compare before setting candidate: let cur_char=candidate,ncompare combined prefix:string built so far(ans[:i]) + cur_char vs targets[:i+1].Since earlier positions already matched up,i.e.,ans[:i]==target[:i](if not yet greater).But actually after earlier decisions maybe some previous indexes were chosen equal making not yet greater.So condition becomes:nif not greater:n    require candidate >=target[i]n    After choosing candidate,n    new_greater=candidate>target[i]n    Then proceed without further checks about rest because future still must ensure eventual>if still not yet.But note even after choosing candidate equal,there may still fail later.So okay.Now implement recursively using index i as described.But note recursion depth N up300 okay,but branching factor limited due alphabet size(<=26).Should pass within time limits.We'll implement iterative using stack maybe easier,but recursion fine.We'll use memoization perhaps on state(i,freq tuple)?Not feasible due many states.Instead rely on pruning.Before starting dfs check feasibility quickly again.Use global variable res initially None.When reaching leaf(i==N)andgreater=True set res=list(ans)andreturnTrue.To ensure earliest found solution is lexicographically smallest,because explore candidates ascending order.So stop at first found solution which will be minimal.Code below implements this plan.