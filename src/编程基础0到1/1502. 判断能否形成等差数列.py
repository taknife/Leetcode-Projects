#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Leetcode-Projects -> 1502. 判断能否形成等差数列.py
# @Author  : Taknife
# @Time    : 2025/11/19 10:59
# @Software: PyCharm

def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr.sort()
    c = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != c:
            return False
    return True


if __name__ == '__main__':
    print(canMakeArithmeticProgression([1,2,4]))