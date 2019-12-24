import numpy as np 
import argparse 
import imutils  
import cv2  
# construct the argument parser and parse the arguments 
ap = argparse.ArgumentParser() 
ap.add_argument("-b", "--bg", required=True,help="path to background image") 
ap.add_argument("-f", "--fg", required=True, help="path to foreground image") 
args = vars(ap.parse_args())
bg = cv2.imread(args["bg"]) 
fg = cv2.imread(args["fg"])
bgGray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY) 
fgGray = cv2.cvtColor(fg, cv2.COLOR_BGR2GRAY)

sub = bgGray.astype("int32") - fgGray.astype("int32")
sub = np.absolute(sub).astype("uint8")

cv2.imshow("delta",sub)
cv2.waitKey(0)
