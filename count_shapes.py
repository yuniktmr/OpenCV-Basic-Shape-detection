import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required = True, help = "input path to the image")

args = vars(ap.parse_args())

frame = cv2.imread(args["image"])
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (3,3), 0)
edged = cv2.Canny(blurred,50,130 )

cnts, _= cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts = imutils.grab_contours(cnts)
total = 0
print(type(cnts))
cv2.drawContours(frame,cnts,-1,(204,0,255),2 )

for c in cnts:
    if cv2.contourArea(c) < 25:
        continue
    #cv2.drawContours(frame,[c],-1,(204,0,255),2 )
    total = total +1
print("[INFO] FOUND {} shapes".format(total))
cv2.imshow("image", frame)
cv2.waitKey(0)
