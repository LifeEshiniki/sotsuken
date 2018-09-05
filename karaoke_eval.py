import librosa
import madmom
import numpy as np
import scipy as sp
from matplotlib import pylab as plt
import os,sys
import pandas as pd
import seaborn as sns

def reading_audio(file):
    audio = input("オーディオファイルの名前を入力")
    if not os.path.isfile("./" + audio):
        print("ファイルがありません")
    else:
        try:
            wav,fs = librosa.load("./" + audio,sr = 44100)
            stftobj = librosa.stft(wav)
            librosa.display.specshow(librosa.logamplitude(np.abs(stftobj) ** 2 , ref_power = np.max),y_axis = "log",x_axis = "time")
            plt.title('Power spectrogram')
            plt.colorbar(format='%+2.0f dB')
            plt.tight_layout()
        except OSError:
            print("オーディオファイルではありません")


class pitch_rating():

    def __init__(self):
        self.score = 0.0



class rhythm_rating():

    def __init__(self):
        self.score = 0.0

class volume_rating():

    def __init__(self):
        self.score = 0.0

def overall_score_ranker(s1,s2,s3,w1,w2,w3):
    # 重みづけ和を返す
    return w1*s1 + w2*s2 + w3*s3

def main():
    print("hoge")
    file = input("オーディオファイルを入力してください")
    reading_audio(file)

if __name__ == "__main__ ":
    main()