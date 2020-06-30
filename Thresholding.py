#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:27:40 2020

@author: muhammadsiraj
"""
import cv2
img_name = cv2.imread('Lena.png')
_, threshold = cv2.threshold(img_name, 155, 255, cv2.THRESH_BINARY) 
img_gray = cv2.cvtColor(img_name, cv2.COLOR_BGR2GRAY)   # Convert to gray

cv2.imshow("Threshold",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()