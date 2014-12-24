#!/usr/bin/env python

# Copyright (c) 2014 Krzysztof Gorzynski <gorzynskikrzysztof@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

__version__ = '0.0.1'

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

