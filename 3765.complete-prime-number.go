#
# @lc app=leetcode id=3765 lang=golang
#
# [3765] Complete Prime Number
#

# @lc code=start
package main

import (
    "math"
    "strconv"
)

func isPrime(n int) bool {
    if n <= 1 { return false }
    if n <= 3 { return true }
    if n%2 == 0 || n%3 == 0 { return false }
    for i := 5; i*i <= n; i += 6 {
        if n%i == 0 || n%(i+2) == 0 { return false }
    }
    return true
}

func completePrime(num int) bool {
    strNum := strconv.Itoa(num)
    length := len(strNum)
    // Check all prefixes:for i := 1; i <= length; i++ {         prefix, _ := strconv.Atoi(strNum[:i])         if !isPrime(prefix) { return false } } // Check all suffixes:for i := length; i > 0; i-- {         suffix, _ := strconv.Atoi(strNum[i-1:])         if !isPrime(suffix) { return false } } return true } # @lc code=end