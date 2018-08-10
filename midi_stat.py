import os,sys,re
import mido
import numpy as np
import pandas as pd
import ngram
import nltk
from matplotlib.pylab import plot as plt
from collections import defaultdict,Counter

class midi_music_sheet():

    def __init__(self,midifilename):
        # 読み込むMIDIファイルの名前
        self.midifile = mido.MidiFile(midifilename)
        # デルタタイム
        self.delta = 240
        # スケール
        self.scale = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
        # その楽譜の音のシーケンス
        self.sequence = []

        # スケールの集計
        self.scale_count = {"C":0,"C#":0,"D":0,"D#":0,"E":0,"F":0,"F#":0,"G":0,"G#":0,"A":0,"A#":0,"B":0}
        #　音価のカウント
        self.dur_count = {}
        #　音高のbi-gram
        self.pitch_bi_gram = nltk.bigrams()

        #  音価のbi-gram
        self.dur_bi_gram = ngram.NGram(N=2)

        # すでに楽譜を読み込んでインスタンス化したか
        self.is_read = False


    def counting(self):
        if self.is_read == False:
            self.is_read = True
            #読み込んだMIDIファイルの全パートの音符を集計
            on_notes = dict()
            tmp_score = []
            for track in self.midifile.tracks:
                e_time = 0
                for msg in track:
                    e_time += msg.time
                    if msg.type == "note_on":
                        on_notes[msg.note] = e_time
                    elif msg.type == "note_off":
                        on_time = on_notes.pop(msg.note)
                        dur = (e_time - on_time)/self.delta
                        tmp_score.append([
                            msg.note,
                            self.scale[msg.note%12],
                            dur,
                            msg.velocity,
                            msg.channel,
                            on_time / self.delta
                        ])

                        self.scale_count[msg.note%12] += 1
                        self.dur_count[dur] += 1

            self.sequence = tmp_score
            scorecount = pd.DataFrame(tmp_score, columns=["NoteID","Note","Octabve","Duration","Velocity","Channel","time"])
            print(scorecount)

            duration  = pd.DataFrame(self.dur_count,columns=["numbers"])


def main ():
    msheet = input("MIDIファイルの名前を入力")
    if not os.path.isfile("./" + msheet):
        print("ファイルがありません")
    else:
        try:
            midi_music_sheet(msheet)
        except OSError:
            print("MIDIファイルではありません")




if __name__ == "__main__":
    main()






