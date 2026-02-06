#\n# @lc app=leetcode id=3776 lang=python3\n#\n# [3776] Minimum Moves to Balance Circular Array\n#\n\n# @lc code=start\nclass Solution:\n    def minMoves(self, balance: List[int]) -> int:\n        total = sum(balance)\n        if total < 0:\n            return -1\n        \n        n = len(balance)\n        neg_index = next((i for i, b in enumerate(balance) if b < 0), None)\n        if neg_index is None:\n            return 0 # Already balanced if no negatives exist\n        \n        moves = 0\n        while balance[neg_index] < 0:\n            left_index = (neg_index - 1) % n\n            right_index = (neg_index + 1) % n\n            \n            left_transfer = min(-balance[neg_index], max(0, balance[left_index]))\		balance[neg_index] += left_transfer
		balance[left_index] -= left_transfer
		moves += left_transfer

            right_transfer = min(-balance[neg_index], max(0, balance[right_index]))\		balance[neg_index] += right_transfer
		balance[right_index] -= right_transfer
		moves += right_transfer

		if left_transfer == 0 and right_transfer == 0:	break # Check for progress globally next cycle
		neg_index = (neg_index + 1) % n # Move forward in circular fashion until resolved or impossible

	return moves if all(b >= 0 for b in balance) else -1# @lc code=end