import music21 as m21
import mido
import numpy as np
import nltk
from collections import Counter
import matplotlib.pylab as plt
import os,sys



def extract_feature(piece):
    piece.show()

def main():
    file =[]
    ok = False
    while ok == False:
        print("Musicxmlのファイル名を入力してください")
        music_file = input("ファイル名")
        if os.path.isfile("./" +music_file):
            try:
               file.append(music_file)
            except OSError:
                print("MusicXMLではありません")
        else:
            print("ファイルがありません")
        is_continue = input("続けますか？終了するなら0と入力")
        if is_continue == "0":
            ok = True

        for sheet in file:
            #楽譜の読み込み
            piece  = m21.converter.parse("./"+ sheet)
            #特徴集計
            piece.show()

            piece.parts[0].show()

            #ピッチクラス集計
            


if __name__ == "__main__":
    main()