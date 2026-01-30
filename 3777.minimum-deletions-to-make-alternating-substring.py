#
# @lc app=leetcode id=3777 lang=python3
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        answer = []
        s = list(s)  # Convert to list for mutability
        for query in queries:
            if query[0] == 1:
                j = query[1]
                # Flip character at index j
                s[j] = 'A' if s[j] == 'B' else 'B'
            elif query[0] == 2:
                l, r = query[1], query[2]
                # Compute minimum deletions for s[l:r+1] to be alternating
                count1 = 0  # Count changes assuming start with 'A'
                count2 = 0  # Count changes assuming start with 'B'
                current_expected_char_1 = 'A'
                current_expected_char_2 = 'B'
                for i in range(l, r + 1):
                    if s[i] != current_expected_char_1:
                        count1 += 1
                    if s[i] != current_expected_char_2:
                        count2 += 1
                    # Alternate expected characters
                    current_expected_char_1 = 'B' if current_expected_char_1 == 'A' else 'A'
                    current_expected_char_2 = 'A' if current_expected_char_2 == 'B' else 'B'
                answer.append(min(count1, count2))
        return answer
# @lc code=end