#!/usr/bin/env python3
# coding=utf-8

import time


def print_hi(name):
    print(f'Hi, {name}')


def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f'{year}年是闰年')
        # print(f'\033[0;32m{year}年是闰年\033[0m')
    else:
        print(f'{year}年不是闰年')
        # print(f'\033[0;31m{year}年不是闰年\033[0m')


def pythagorean_triple():
    total = 0
    for_total = 0
    # for a in range(1, 101):
    #     for b in range(1, 101):
    #         for c in range(1, 101):
    #             for_total += 1
    #             if a * a + b * b == c * c:
    #                 total += 1
    #                 print(f'勾股数: {a} {b} {c}')
    for c in range(1, 101):
        for b in range(1, c):
            for a in range(1, b):
                for_total += 1
                # time.sleep(0.00000001)
                if a * a + b * b == c * c:
                    total += 1
                    print(f'勾股数: {a} {b} {c}')
    print(f'\n勾股数共 {total} 个， 总循环 {for_total} 次。')


if __name__ == '__main__':
    print_hi('Hong Kai')
    # is_leap_year(100)
    # is_leap_year(400)
    # is_leap_year(2021)
    # is_leap_year(2020)
    # is_leap_year(2000)
    # is_leap_year(1900)

    # while True:
    #     input_year = int(input('请输入年份:'))
    #     is_leap_year(input_year)

    pythagorean_triple()
