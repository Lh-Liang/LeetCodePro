#
# @lc app=leetcode id=1206 lang=python3
#
# [1206] Design Skiplist
#
# @lc code=start
class _Node:
    __slots__ = ("val", "next")

    def __init__(self, val: int, level: int):
        self.val = val
        self.next = [None] * level


class Skiplist:
    MAX_LEVEL = 20  # enough for n up to ~1e6 with p=0.5

    def __init__(self):
        self.head = _Node(-1, self.MAX_LEVEL)
        self.level = 1
        # xorshift32 seed
        self._seed = 2463534242

    def _randbit(self) -> int:
        # xorshift32
        x = self._seed & 0xFFFFFFFF
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        self._seed = x
        return x & 1

    def _random_level(self) -> int:
        lvl = 1
        while lvl < self.MAX_LEVEL and self._randbit() == 1:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            while cur.next[i] is not None and cur.next[i].val < target:
                cur = cur.next[i]
        cur = cur.next[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = [None] * self.MAX_LEVEL
        cur = self.head

        for i in range(self.level - 1, -1, -1):
            while cur.next[i] is not None and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl

        node = _Node(num, lvl)
        for i in range(lvl):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        cur = self.head

        for i in range(self.level - 1, -1, -1):
            while cur.next[i] is not None and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur

        target = update[0].next[0]
        if target is None or target.val != num:
            return False

        # Remove on every level where the node exists
        for i in range(self.level):
            if update[i].next[i] is target:
                update[i].next[i] = target.next[i]

        # Decrease current level if highest levels are empty
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1

        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
# @lc code=end