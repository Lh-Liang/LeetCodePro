#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#

# @lc code=start
from typing import List
from collections import defaultdict

def mod_inv(a, m):
    if gcd(a, m) != 1:
        return None  # Modular inverse doesn't exist if a and m are not coprime.
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return (x1 + m0) % m0 if x1 < 0 else x1 

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def calculate_x_value(nums: List[int], k: int, start: int, xi: int) -> int:
    n = len(nums)
    prefix_product = [1] * (start + 1)
    for i in range(start):
        prefix_product[i+1] = (prefix_product[i] * nums[i]) % k 
    product_mod_count = defaultdict(int)
    suffix_product = 1
    result = 0 
    for i in range(n-1, start-1, -1): 
        product_mod_count[suffix_product % k] += 1 
        suffix_product = (suffix_product * nums[i]) % k 
        inv_prefix_mod = mod_inv(prefix_product[start], k) 
        if inv_prefix_mod is not None:
            target_mod = (suffix_product * inv_prefix_mod) % k 
            result += product_mod_count[(xi - target_mod + k) % k]
    return result 
class Solution:
def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
data = [] 	for indexi, valuei, starti, xi in queries:
data.append(calculate_x_value(nums[:indexi]+[valuei]+nums[indexi+1:],k,starti)) 	return data 	# @lc code=end