#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Leetcode-Projects -> 896. 单调数列.py
# @Author  : Taknife
# @Time    : 2025/11/19 13:41
# @Software: PyCharm

def isMonotonic(nums: list[int]) -> bool:
    d = nums.copy()
    c = nums.copy()
    d.sort(reverse=True)
    c.sort(reverse=False)
    print(d)
    print(c)
    print(nums)
    if nums == d or nums == c:
        return True
    else:
        return False

if __name__ == '__main__':
    print(isMonotonic([1,3,2]))