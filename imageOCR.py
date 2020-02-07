#!/usr/bin/env python2

import sys
from memeocr import MemeOCR

def getOCR(argv):
    # if len(argv) != 2:
    #     print ('usage:')
    #     print ('    ./main.py meme-file-name')
    #     return

    outString = ''
    meme_fname = argv
    ocr = MemeOCR()
    txt = ocr.recognize(meme_fname)
    for item in txt:
    	outString += item

    return outString

# print(getOCR('test2.png'))