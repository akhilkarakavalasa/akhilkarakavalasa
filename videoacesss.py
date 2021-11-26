# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:36:11 2021

@author: 15406
"""
import cv2
import numpy as np
import matplotlib.pyplot as pl
import os
import sys
s=0
if len(sys.argv)>1:
    s=sys.argv[1]
source=cv2.VideoCapture(s)
win_name='camera preview'
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
while cv2.waitKey(1) != 27:
    has_frame, frame=source.read()
    if not has_frame:
        break
    cv2.imshow(win_name,frame)
source.release()
cv2.destroywindow(win_name)