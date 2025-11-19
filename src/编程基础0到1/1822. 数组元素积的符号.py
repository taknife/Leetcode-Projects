#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Leetcode-Projects -> 1822. 数组元素积的符号.py
# @Author  : Taknife
# @Time    : 2025/11/18 17:46
# @Software: PyCharm

def arraySign(nums: list[int]) -> int:
    if 0 in nums:
        return 0
    else:
        nums = [x for x in nums if x < 0]
        print(len(nums))
        if len(nums) % 2 == 0:
            return 1
        else:
            return -1

if __name__ == '__main__':
    print(arraySign([-1,-2,-3,-4,3,2,1]))