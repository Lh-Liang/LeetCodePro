#
# @lc app=leetcode id=3625 lang=python3
#
# [3625] Count Number of Trapezoids II
#

from itertools import combinations
from typing import List, Tuple

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        def slope(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
            # Calculate slope and handle vertical line case
            if p1[0] == p2[0]:
                return float('inf')  # Vertical line slope representation
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        
        def is_trapezoid(p1, p2, p3, p4) -> bool:
            # Calculate slopes for opposite sides
            slopes = [
                slope(p1, p2), slope(p3, p4), 
                slope(p1, p3), slope(p2, p4), 
                slope(p1, p4), slope(p2, p3)
            ]
            # Check if at least one pair of opposite sides has equal slopes
            return (slopes[0] == slopes[1]) or (slopes[2] == slopes[3]) or (slopes[4] == slopes[5])
        
        unique_trapezoids = set()
        for quad in combinations(points, 4):
            if is_trapezoid(*quad):
                # Create a canonical form for the trapezoid to check uniqueness
                sorted_quad = tuple(sorted(quad))
                unique_trapezoids.add(sorted_quad)
        return len(unique_trapezoids)