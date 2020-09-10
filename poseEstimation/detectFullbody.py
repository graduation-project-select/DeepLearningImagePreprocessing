# fashion_pose.py : MPII를 사용한 신체부위 검출
import cv2

# MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
              "Background": 15}

POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
              ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
              ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]

# 각 파일 path
# protoFile = "D:\\python_D\\fashion_data\\pose_deploy_linevec_faster_4_stages.prototxt"
# weightsFile = "D:\\python_D\\fashion_data\\pose_iter_160000.caffemodel"
protoFile = "./pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "./pose_iter_160000.caffemodel"


def findX1(output, W, imageWidth):
    x1 = -1
    # 2,3,4 중 가장 작은
    for i in range(2,5):
        # 해당 신체부위 신뢰도 얻음.
        probMap = output[0, i, :, :]
        # global 최대값 찾기
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        # 원래 이미지에 맞게 점 위치 변경
        x = (imageWidth * point[0]) / W
        if prob > 0.1:
          if x1 == -1 or (x != -1 and x < x1):
              x1 = x
        # else:
        #     print(str(i)+" is 'else'")
    return x1

def findX2(output, W, imageWidth):
    x2 = -1
    # 5,6,7 중 가장 큰 값
    for i in range(5,8):
        # 해당 신체부위 신뢰도 얻음.
        probMap = output[0, i, :, :]
        # global 최대값 찾기
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        # 원래 이미지에 맞게 점 위치 변경
        x = (imageWidth * point[0]) / W
        if prob > 0.1:
          if x2 == -1 or (x != -1 and x > x2):
              x2 = x
        # else:
        #     print(str(i)+" is 'else'")
    return x2

def findY1(output, H, imageHeight):
    y1 = -1
    probMap = output[0, 1, :, :] # 목부분
    # global 최대값 찾기
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
    # 원래 이미지에 맞게 점 위치 변경
    y = (imageHeight * point[1]) / H
    # 키포인트 검출한 결과가 0.1보다 크면(검출한곳이 위 BODY_PARTS랑 맞는 부위면) points에 추가, 검출했는데 부위가 없으면 None으로
    # if prob > 0.1:
    y1 = y
    # else:
    #     print("1 is 'else'")
    return y1

def findY2(output, H, imageHeight):
    # 10,13 중 더 큰 값
    y2 = -1
    probMap10 = output[0, 10, :, :]
    minVal10, prob10, minLoc10, point10 = cv2.minMaxLoc(probMap10)
    probMap13 = output[0, 13, :, :]
    minVal13, prob13, minLoc13, point13 = cv2.minMaxLoc(probMap13)
    y10 = (imageHeight * point10[1]) / H
    y13 = (imageHeight * point13[1]) / H
    if y10 < y13 and prob13 > 0.1:
        y2 = y13
    elif y10 >= y13 and prob10 > 0.1:
        y2 = y10
    elif prob13 > 0.1:
        y2 = y13
    elif prob10 > 0.1:
        y2 = y10
    return y2

def detectFullbody(image, output, imageWidth, imageHeight):
    H = output.shape[2]
    W = output.shape[3]

    x1 = findX1(output, W, imageWidth)
    x2 = findX2(output, W, imageWidth)
    y1 = findY1(output, H, imageHeight)
    y2 = findY2(output, H, imageHeight)
    print("x1:" + str(x1) + ", x2: " + str(x2) + ", y1: " + str(y1) + ", y2: " + str(y2))

    if x1 != -1 and x2 != -1 and y1 != -1 and y2 != -1:
        alpha = 2
        if int(y1) - alpha > 0:
            y1 = int(y1) - alpha
        if int(x1) - alpha > 0:
            x1 = int(x1) - alpha
        if int(y2) + alpha < imageHeight:
            y2 = int(y2) + alpha
        if int(x2) + alpha < imageWidth:
            x2 = int(x2) + alpha

        cropped_img = image[int(y1): int(y2), int(x1): int(x2)]
        # cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), thickness=1)
        # cv2.imshow("Output-Keypoints", image)
        # cv2.waitKey(0)
        return cropped_img
    else:
        return []