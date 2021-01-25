import cv2
import numpy as np

image = cv2.imread("blobs.jpg")
cv2.imshow('Original',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
detector = cv2.SimpleBlobDetector()
keypoints = detector.detect(image)
blank = np.zeros((1,1))
blobs = cv2.drawKeyPoints(image,keypoints,blank,(0,0,255),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
n = len(keypoints)
text = 'Blobs : '+str(n)
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_SIMPLEX,1
            ,(100,0,255),2)
cv2.imshow("Blobs using default param",blobs)
cv2.waitKey(0)