# -*- coding: utf-8 -*-

import tkinter as tk
import numpy as np

# 表示の設定
# ビンゴの数字の最大値
BINGO_SIZE = 75

# 次の数字が表示されるまでの時間（推奨:100）
DISPLAY_TIMES = 500

# ウィンドウの高さ（推奨:700）
WINDOW_HEIGHT = 700

# ウィンドウの幅（推奨:1000）
WINDOW_WIDTH = 1000

# 選ばれた数字のフォントサイズ（推奨:400）
CENTER_NUM_SIZE = 400

# その他のフォントサイズ（推奨:50）
FONT_SIZE = 50


class bingoClass():
    def __init__(self, size):
        self.bingoSize = size
        self.numList = np.arange(self.bingoSize+1, dtype=int)[1:]
        np.random.shuffle(self.numList)
        # print(self.numList)
        self.count = 0
        self.makeGUI()

    def nextNum(self):
        for i in range(0, DISPLAY_TIMES):
            index = self.randNum(self.bingoSize-self.count)+self.count-1
            self.label["text"] = self.numList[index]
            self.label.update()
        self.label["text"] = self.numList[self.count]
        self.label.update()
        self.addNum()
        self.count += 1
        if self.count == self.bingoSize:
            self.fin()

    def start(self):
        self.button["text"] = "次へ"
        self.button["command"] = lambda: self.nextNum()
        self.nextNum()

    def addNum(self):
        self.list.insert(0, "[%03d]. %3d" %
                         (self.count+1, self.numList[self.count]))
        self.show.update()

    def randNum(self, num):
        return np.random.random_integers(1, num)

    def fin(self):
        self.button["text"] = "終了！"
        self.button["command"] = self.root.destroy

    def makeGUI(self):
        # rootウィンドウを作成
        self.root = tk.Tk()
        self.root.title("BINGO")
        self.root.geometry("%dx%d" % (WINDOW_WIDTH, WINDOW_HEIGHT))

        # 中央の数字とボタンの表示
        self.frame1 = tk.Frame(self.root)
        self.label = tk.Label(self.frame1, text="", font=(
            "", CENTER_NUM_SIZE), height="1", width="2")
        self.label.pack()
        self.button = tk.Button(self.frame1, text="ビンゴ開始！",
                                command=lambda: self.start(), font=("", FONT_SIZE))
        self.button.pack()
        self.frame1.grid(row=0, column=0)

        # 出た数字の表示
        self.frame2 = tk.Frame(self.root)
        self.show = tk.Label(self.frame2, text="出た数字：", font=("", FONT_SIZE))
        self.show.grid()
        self.list = tk.Listbox(self.frame2, font=(
            "", FONT_SIZE), height=8, width=10)
        self.list.grid()
        self.frame2.grid(row=0, column=1)


bingo = bingoClass(75)
# メインループ
bingo.root.mainloop()
