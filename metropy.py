#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: metropy.py
Author: Krzysztof Górzyński
Email: gorzynski<dot>krzysztof<at>gmail<dot>com
Github: https://github.com/gorzk
Description: The simply terminal metronome
"""

import time
import sys

try:
    import pygame
except ImportError:
    print("ERROR: PyGame needed to run this program.'\n'Please install it and try again.")
    sys.exit(2)

def makeBeat(click, bpm):
    if bpm < 30:
        bpm = 30
    if bpm > 300:
        bpm = 300
    sec = float(60.00/bpm)
    while True:
        playClick(click)
        time.sleep(sec)

def playClick(click):
    sound = pygame.mixer.Sound(click)
    channel = sound.play()
    sound.set_volume(0.9)

def main():
    pygame.init()
    wave = str(sys.argv[1])
    bpm = float(sys.argv[2])
    print 'METROPY by gorzk'
    print 'Audio: {0} | Tempo: {1}BPM'.format(wave, bpm)
    makeBeat(wave, bpm)

if __name__=='__main__':
    main()

