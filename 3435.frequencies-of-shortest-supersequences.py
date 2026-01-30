#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        from collections import deque, defaultdict
        # Step 1: Gather unique letters
        n = len(words)
        # Each state: tuple of matched indices for each word
        initial = tuple([0] * n)
        queue = deque()
        queue.append((initial, ''))
        visited = defaultdict(set)  # state -> set of minimal seqs
        visited[initial].add('')
        found_len = None
        results = set()
        while queue:
            layer_size = len(queue)
            layer_solutions = []
            for _ in range(layer_size):
                state, seq = queue.popleft()
                # Step 2: Check if all words matched
                if all(state[i] == 2 for i in range(n)):
                    if found_len is None:
                        found_len = len(seq)
                    if len(seq) == found_len:
                        freq = [0] * 26
                        for ch in seq:
                            freq[ord(ch) - ord('a')] += 1
                        results.add(tuple(freq))
                        layer_solutions.append((state, seq))
                    continue
                # Step 3: Find all possible next characters
                next_chars = set()
                for i in range(n):
                    if state[i] < 2:
                        next_chars.add(words[i][state[i]])
                for ch in next_chars:
                    new_state = list(state)
                    for i in range(n):
                        if state[i] < 2 and words[i][state[i]] == ch:
                            new_state[i] += 1
                    new_state = tuple(new_state)
                    new_seq = seq + ch
                    # Step 4: State tracking for minimal-length paths
                    if (new_state not in visited) or (len(new_seq) <= min((len(s) for s in visited[new_state]), default=float('inf'))):
                        if found_len is None or len(new_seq) <= found_len:
                            visited[new_state].add(new_seq)
                            queue.append((new_state, new_seq))
            # Step 5: Stop only after processing full minimal layer
            if found_len is not None and not queue:
                break
        # Step 6: Output frequency arrays, deduplicated
        return [list(freq) for freq in results]
# @lc code=end