#
# @lc app=leetcode id=3455 lang=python3
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        # Step 1: Special case handling for '**' (matches empty substring)
        if p == '**':
            return 0

        # Step 2: Decompose pattern into prefix, infix, suffix
        first = p.find('*')
        second = p.find('*', first + 1)
        prefix = p[:first]
        infix = p[first+1:second]
        suffix = p[second+1:]

        n = len(s)
        min_len = float('inf')
        found = False

        # Step 3: Precompute all prefix start positions
        prefix_starts = [i for i in range(n - len(prefix) + 1) if s[i:i+len(prefix)] == prefix]
        # Step 4: Precompute all suffix end positions
        suffix_ends = [j + len(suffix) - 1 for j in range(n - len(suffix) + 1) if s[j:j+len(suffix)] == suffix]

        # Step 5: For each prefix, look for infix and suffix, ensuring order and non-overlap
        for start in prefix_starts:
            after_prefix = start + len(prefix)
            # If infix is empty, start search from after_prefix
            infix_pos = after_prefix if not infix else s.find(infix, after_prefix)
            while infix_pos != -1 and (not infix or infix_pos >= after_prefix):
                after_infix = infix_pos + len(infix)
                # Find the first suffix occurrence after after_infix-1
                # Use binary search to efficiently locate the suffix_end
                l, r = 0, len(suffix_ends) - 1
                candidate = -1
                while l <= r:
                    m = (l + r) // 2
                    if suffix_ends[m] >= after_infix - 1:
                        candidate = suffix_ends[m]
                        r = m - 1
                    else:
                        l = m + 1
                if candidate != -1:
                    window_start = start
                    window_end = candidate
                    candidate_window = s[window_start:window_end+1]
                    # Step 6: Explicitly verify that the candidate window matches the pattern
                    # Confirm prefix, infix, suffix order and non-overlap
                    prefix_ok = candidate_window.startswith(prefix)
                    suffix_ok = candidate_window.endswith(suffix)
                    infix_ok = True
                    search_start = len(prefix)
                    search_end = len(candidate_window) - len(suffix)
                    # Check infix (must be found between prefix and suffix, can be empty)
                    if infix:
                        infix_pos_in_window = candidate_window.find(infix, search_start, search_end)
                        infix_ok = infix_pos_in_window != -1
                    if prefix_ok and infix_ok and suffix_ok:
                        found = True
                        min_len = min(min_len, window_end - window_start + 1)
                # Next infix occurrence
                if infix:
                    next_search = infix_pos + 1
                    infix_pos = s.find(infix, next_search)
                else:
                    break

        # Step 7: Return result if found, else -1
        return min_len if found else -1
# @lc code=end