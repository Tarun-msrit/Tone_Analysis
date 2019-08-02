# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:56:52 2019

@author: VYBHAV JAIN
"""

mysp=__import__("my-voice-analysis")
p="output5" # Audio File title
c=r"C:\Users\VYBHAV JAIN\Desktop\Tone Analysis" # Path to the Audio_File directory (Python 3.7)
mysp.myspgend(p,c)
mysp.myspsr(p,c)
mysp.myspatc(p,c)
mysp.myspst(p,c)

## Same text 3 different ways ....3 outputs here 1nad 3 male and female
## Check superior code in github
## Manual time length for speech
## Subjective and objective test resutk 