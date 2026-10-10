#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""猜数字小游戏

电脑随机生成一个 1-100 之间的整数，玩家不断输入猜测，
程序提示"大了"或"小了"，直到猜中为止，并统计猜测次数。
"""

import random

LOW = 1
HIGH = 100


def read_guess(attempt):
    """读取并校验用户输入，返回一个 [LOW, HIGH] 范围内的整数。"""
    while True:
        raw = input(f"第 {attempt} 次猜测，请输入 {LOW}-{HIGH} 之间的整数：").strip()
        if not raw:
            print("输入不能为空，请重新输入。")
            continue
        try:
            guess = int(raw)
        except ValueError:
            print(f"“{raw}”不是有效的整数，请重新输入。")
            continue
        if guess < LOW or guess > HIGH:
            print(f"请输入 {LOW} 到 {HIGH} 之间的数字。")
            continue
        return guess


def play_once():
    """进行一局游戏，返回本局猜测次数。"""
    answer = random.randint(LOW, HIGH)
    count = 0

    print("=" * 40)
    print(f"我已经想好了一个 {LOW}-{HIGH} 之间的数字，快来猜猜看吧！")
    print("=" * 40)

    while True:
        count += 1
        guess = read_guess(count)

        if guess > answer:
            print("大了")
        elif guess < answer:
            print("小了")
        else:
            print(f"恭喜你，猜中了！答案就是 {answer}。")
            print(f"你一共猜了 {count} 次。")
            return count


def main():
    print("欢迎来到猜数字小游戏！")
    best = None

    while True:
        count = play_once()
        best = count if best is None else min(best, count)

        again = input("再来一局？(y/n)：").strip().lower()
        if again not in ("y", "yes", "是"):
            print(f"本次最佳成绩：{best} 次。感谢游玩，再见！")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n游戏已退出，再见！")
