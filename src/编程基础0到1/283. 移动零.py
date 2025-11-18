#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Leetcode-Projects -> 283. 移动零.py
# @Author  : Taknife
# @Time    : 2025/11/18 16:38
# @Software: PyCharm


nums = [0,1,0,2,0,3,12]
n = nums.count(0)
while True:
    if 0 in nums:
        nums.remove(0)
    else:
        break

for _ in range(n):
    nums.append(0)

print(nums)