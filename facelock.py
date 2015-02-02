#!/usr/bin/env python2

"""
OpenCV example. Show webcam image and detect face.
"""

# Location of CV face cascades on your system
TRAINSET = "/usr/share/opencv/lbpcascades/lbpcascade_frontalface.xml"
# Downscale the image supplied to opencv by this factor. Increase
# if the recognition is to slow.
DOWNSCALE = 2
# take a photo if a face is visible for longer than this amount of seconds
PHOTOTRESHOLD = 5
# your webcam's resolution
CAMRES = (800, 448)
# your screen's resolution
SCREENRES = (1366, 768)
# directory where photos are stored
PHOTODIR = "images"

import cv2
import cv2.cv as cv
import time
import os

webcam = cv2.VideoCapture(0)
cv2.namedWindow("facelock")
classifier = cv2.CascadeClassifier(TRAINSET)

webcam.set(cv.CV_CAP_PROP_FRAME_WIDTH, CAMRES[0])
webcam.set(cv.CV_CAP_PROP_FRAME_HEIGHT, CAMRES[1])

if webcam.isOpened():  # try to get the first frame
    rval, frame = webcam.read()
else:
    rval = False
if not os.path.isfile(TRAINSET):
    print "Face cascades not found. Face recognition disabled."


last = 0
while rval:

    # detect faces and draw bounding boxes
    minisize = (frame.shape[1] / DOWNSCALE, frame.shape[0] / DOWNSCALE)
    miniframe = cv2.resize(frame, minisize)
    faces = classifier.detectMultiScale(miniframe)
    x, y = 100, 100
    detected = False
    for f in faces:
        x, y, w, h = [v * DOWNSCALE for v in f]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))
        cv2.rectangle(miniframe, (x / DOWNSCALE, y / DOWNSCALE), ((x + w) / DOWNSCALE, (y + h) / DOWNSCALE), (0, 0, 255))
        if w > 100:
            detected = True

    # live preview
    pframe = cv2.resize(frame, SCREENRES)
    cv2.putText(pframe, "Smile to unlock", (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255))
    cv2.imshow("facelock", pframe)

    # record
    if detected and len(faces) > 0 and time.time() - last > PHOTOTRESHOLD:
        if not os.path.exists(PHOTODIR):
            os.makedirs(PHOTODIR)
        cv2.imwrite("%s/%f.jpg" % (PHOTODIR,time.time()), miniframe)
        last = time.time()

    # get next frame
    rval, frame = webcam.read()

    key = cv2.waitKey(20)
    if key in [27, ord('Q'), ord('q')]:  # exit on ESC
        break
