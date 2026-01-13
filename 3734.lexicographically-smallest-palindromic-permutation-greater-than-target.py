#
# @lc app=leetcode id=3734 lang=python3
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        odd = [i for i in range(26) if freq[i] % 2 == 1]
        if n % 2 == 0:
            if odd:
                return ""
            mid = ""
        else:
            if len(odd) != 1:
                return ""
            mid = chr(odd[0] + 97)

        m = n // 2
        half = [f // 2 for f in freq]
        tp = target[:m]

        def can_form_exact(t: str) -> bool:
            cnt = half[:]
            for ch in t:
                idx = ord(ch) - 97
                cnt[idx] -= 1
                if cnt[idx] < 0:
                    return False
            return True

        def build_suffix(cnt):
            # smallest arrangement from remaining counts
            parts = []
            for i in range(26):
                if cnt[i]:
                    parts.append(chr(i + 97) * cnt[i])
            return "".join(parts)

        def next_greater_multiset(tp: str):
            # returns smallest multiset permutation strictly greater than tp, or None
            if m == 0:
                return None

            # prefixUsed[i] = counts used by tp[:i]
            prefixUsed = [[0] * 26 for _ in range(m + 1)]
            for i, ch in enumerate(tp):
                prefixUsed[i + 1] = prefixUsed[i][:]
                prefixUsed[i + 1][ord(ch) - 97] += 1

            for i in range(m - 1, -1, -1):
                # check if tp[:i] is feasible
                rem = [half[j] - prefixUsed[i][j] for j in range(26)]
                if any(x < 0 for x in rem):
                    continue

                cur = ord(tp[i]) - 97
                for nxt in range(cur + 1, 26):
                    if rem[nxt] > 0:
                        rem[nxt] -= 1
                        suffix = build_suffix(rem)
                        return tp[:i] + chr(nxt + 97) + suffix
            return None

        def make_pal(L: str) -> str:
            return L + mid + L[::-1]

        # 1) If we can exactly match the left half to tp, check if that palindrome already beats target.
        if can_form_exact(tp):
            cand = make_pal(tp)
            if cand > target:
                return cand

        # 2) Otherwise find the smallest left half strictly greater than tp.
        L2 = next_greater_multiset(tp)
        if L2 is None:
            return ""
        return make_pal(L2)

# @lc code=end
