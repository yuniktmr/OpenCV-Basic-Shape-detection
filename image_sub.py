import argparse
import cv2
import imutils
import numpy as np

ap = argparse.ArgumentParser()

ap.add_argument("-b","--bg", required = True, help = "path to background img")
ap.add_argument("-f","--fg", required = True, help = "path to foreground img")
args = vars(ap.parse_args())

bg = cv2.imread(args["bg"])
fg = cv2.imread(args["fg"])

bgGray = cv2.cvtColor(bg , cv2.COLOR_BGR2GRAY)
fgGray = cv2.cvtColor(fg , cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(bgGray , fgGray)
diff2 = fgGray.astype("int32")-bgGray.astype("int32")
diff2 = np.absolute(diff2).astype("uint8")

cv2.imshow("delta", diff)
cv2.imshow("delta2", diff2)
cv2.waitKey(0)
