Step 1: Carefully read and understand the problem statement and constraints.
Step 2: Break down the problem into subtasks:
  a. Find the minimal SCS length for the input words.
  b. Generate all SCSs of that minimal length ensuring each contains all words as subsequences.
  c. For each SCS, compute its frequency array over the 26 lowercase English letters.
  d. Deduplicate frequency arrays so only unique (non-permutation) solutions remain.
Step 3: After each subtask, verify correctness and completeness; for example, confirm all SCSs are minimal and include every input word as a subsequence, and that deduplication is accurate.
Step 4: Use efficient, general-purpose algorithms (e.g., BFS/backtracking/dynamic programming for SCS construction; hash sets for deduplication).
Step 5: Confirm that the output strictly matches the required List<List<Integer>> format.
Step 6: Perform a final checklist review to ensure all instructions, constraints, and output format requirements are fully satisfied.