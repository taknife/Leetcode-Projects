#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : Leetcode-Projects -> 66. 加一.py
# @Author  : Taknife
# @Time    : 2025/11/18 16:49
# @Software: PyCharm


def plusOne(digits: list[int]):
    w = 0
    digits.reverse()
    while True:
        digits[w] += 1
        if digits[w] < 10:
            digits.reverse()
            return digits
        else:
            if w < len(digits) - 1:
                digits[w] = 0
                w += 1
            else:
                digits[w] = 0
                digits.append(1)
                digits.reverse()
                return digits



if __name__ == '__main__':
    print(plusOne([1, 1, 3, 9, 9]))
