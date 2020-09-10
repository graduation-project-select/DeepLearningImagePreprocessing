<<<<<<< HEAD
#-*- coding:utf-8 -*-
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os
from matplotlib import pyplot as plt

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
face_cascade = cv2.CascadeClassifier('./cvlib/haarcascades/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('./cvlib/haarcascades/haarcascade_fullbody.xml')
upperbody_cascade = cv2.CascadeClassifier('./cvlib/haarcascades/haarcascade_upperbody.xml')

def cropFace(fileName, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.03, 5)
    height, width = image.shape[:2]
    # print(height, width)
    detectFace = False
    min_height = int(height/3)
    for (x, y, w, h) in faces:
        detectFace = True
        if (y+h) < min_height:
            min_height = y+h
        # print(x, y, x + w, y + h)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if detectFace:
        # 이미지 자르기
        # croppedWinName = "cropped"
        crop_img = image[min_height:, :]
        # cv2.moveWindow(croppedWinName, 40, 30)
        # cv2.imshow(croppedWinName, crop_img)
        cv2.imwrite(fileName, crop_img)
        print("[Crop]"+fileName)

def detectHuman(fileName, image):
    # detect people in the image
    body = body_cascade.detectMultiScale(image, 1.01, 10)
    detectBody = False
    for (x, y, w, h) in body:
        detectBody = True
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    if detectBody:
        cv2.imshow(fileName, image)

    # (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    #
    # # apply non-maxima suppression to the bounding boxes using a
    # # fairly large overlap threshold to try to maintain overlapping
    # # boxes that are still people
    # rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    # pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    # # draw the final bounding boxes
    # for (xA, yA, xB, yB) in pick:
    #     cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    # print("[INFO] {} people".format(len(rects)))
    # cv2.imshow(fileName, image)
    # if len(rects) > 0:
    #     return True
    # else:
    #     return False

def detectUpperBody(fileName, image):
    # detect people in the image
    body = upperbody_cascade.detectMultiScale(image, 1.01, 10)
    findUpperBody = False
    for (x, y, w, h) in body:
        findUpperBody = True
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    if findUpperBody:
        cv2.imshow(fileName, image)


root_dir = "./testdata"
root_file_list = os.listdir(root_dir)
for folderName in root_file_list:
    path_dir = root_dir + "/" + folderName
    print("=======================================")
    print(path_dir)
    print("=======================================")
    # path_dir="./fabric/wool"
    file_list = os.listdir(path_dir)

    for fileName in file_list:
        image_path = path_dir+"/"+fileName
        image = cv2.imread(image_path)
        print(image_path)
        # cropFace(image_path, image)
        # detectHuman(fileName, image)
        detectUpperBody(fileName, image)

        # if detectHuman(image):
            # remove image
            # print("[Remove] {}".format(fileName))
            # os.remove(fileName)

    cv2.waitKey(0)
=======
#-*- coding:utf-8 -*-
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import os
from matplotlib import pyplot as plt

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
face_cascade = cv2.CascadeClassifier('./cvlib/haarcascades/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('./cvlib/haarcascades/haarcascade_fullbody.xml')

def cropFace(fileName, image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.03, 5)
    height, width = image.shape[:2]
    # print(height, width)
    detectFace = False
    min_height = int(height/3)
    for (x, y, w, h) in faces:
        detectFace = True
        if (y+h) < min_height:
            min_height = y+h
        # print(x, y, x + w, y + h)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if detectFace:
        # 이미지 자르기
        # croppedWinName = "cropped"
        crop_img = image[min_height:, :]
        # cv2.moveWindow(croppedWinName, 40, 30)
        # cv2.imshow(croppedWinName, crop_img)
        cv2.imwrite(fileName, crop_img)
        print("[Crop]"+fileName)


def detectHuman(fileName, image):
    # detect people in the image
    body = body_cascade.detectMultiScale(image, 1.01, 10)
    detectBody = False
    for (x, y, w, h) in body:
        detectBody = True
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)
    if detectBody:
        cv2.imshow(fileName, image)

    # (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    #
    # # apply non-maxima suppression to the bounding boxes using a
    # # fairly large overlap threshold to try to maintain overlapping
    # # boxes that are still people
    # rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    # pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    # # draw the final bounding boxes
    # for (xA, yA, xB, yB) in pick:
    #     cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
    # print("[INFO] {} people".format(len(rects)))
    # cv2.imshow(fileName, image)
    # if len(rects) > 0:
    #     return True
    # else:
    #     return False


root_dir = "./texture_crop"
root_file_list = os.listdir(root_dir)
for folderName in root_file_list:
    path_dir = root_dir + "/" + folderName
    print("=======================================")
    print(path_dir)
    print("=======================================")
    # path_dir="./fabric/wool"
    file_list = os.listdir(path_dir)

    for fileName in file_list:
        image_path = path_dir+"/"+fileName
        image = cv2.imread(image_path)
        print(image_path)
        cropFace(image_path, image)
        # detectHuman(fileName, image)

        # if detectHuman(image):
            # remove image
            # print("[Remove] {}".format(fileName))
            # os.remove(fileName)

    cv2.waitKey(0)
>>>>>>> 348e7c879d0063e94acabf2f2085943ac6f45a4d
