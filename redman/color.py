# -*- coding=utf-8 -*-
from __future__ import absolute_import


class Color:
    # https://www.mm2d.net/main/prog/c/console-02.html

    黒 = "\033[30m"
    赤 = "\033[31m"
    緑 = "\033[32m"
    黄 = "\033[33m"
    青 = "\033[34m"
    紫 = "\033[35m"
    水 = "\033[36m"
    灰 = "\033[37m"

    背景黒 = "\033[40m"
    背景赤 = "\033[41m"
    背景緑 = "\033[42m"
    背景黄 = "\033[43m"
    背景青 = "\033[44m"
    背景紫 = "\033[45m"
    背景水 = "\033[46m"
    背景灰 = "\033[47m"

    RESET = "\033[0m"        # 装飾なし
    BOLD = "\033[01m"        # 太字
    THIN = "\033[02m"        # 細字
    ITALIC = "\033[03m"      # イタリック体
    UNDER = "\033[04m"       # 下線
    BLINK = "\033[05m"       # 点滅
    HIGH_BLINK = "\033[06m"  # 高速点滅
    REVERSE = "\033[07m"     # 反転
