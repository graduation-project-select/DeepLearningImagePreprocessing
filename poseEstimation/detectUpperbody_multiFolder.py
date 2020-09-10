import cv2
import os
from detectUpperbody import detectUpperbody
from detectLowerbody import detectLowerbody
from detectFullbody import detectFullbody

# 각 파일 path
protoFile = "./pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "./pose_iter_160000.caffemodel"

# 위의 path에 있는 network 불러오기
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

root_dir = "./texture_crop"
root_file_list = os.listdir(root_dir)
for folderName in root_file_list:
    path_dir = root_dir + "/" + folderName
    print("=======================================")
    print(path_dir)
    print("=======================================")
    # path_dir="./fabric/wool"
    file_list = os.listdir(path_dir)

    cropped_img_path_ub = path_dir + "/cropped_ub"
    if not os.path.isdir(cropped_img_path_ub):
        os.mkdir(cropped_img_path_ub)
    cropped_img_path_lb = path_dir + "/cropped_lb"
    if not os.path.isdir(cropped_img_path_lb):
        os.mkdir(cropped_img_path_lb)
    cropped_img_path_fb = path_dir + "/cropped_fb"
    if not os.path.isdir(cropped_img_path_fb):
        os.mkdir(cropped_img_path_fb)

    for fileName in file_list:
        image_path = path_dir+"/"+fileName
        try:
            image = cv2.imread(image_path)
            print(image_path)
            image = cv2.imread(image_path)
            # frame.shape = 불러온 이미지에서 height, width, color 받아옴
            imageHeight, imageWidth, _ = image.shape
            # network에 넣기위해 전처리
            inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False)
            # network에 넣어주기
            net.setInput(inpBlob)
            # 결과 받아오기
            output = net.forward()
            print("이미지 ID : ", len(output[0]), ", H : ", output.shape[2], ", W : ", output.shape[3])  # 이미지 ID
            # 상의
            cropped_img_ub = detectUpperbody(image, output, imageWidth, imageHeight)
            if len(cropped_img_ub) != 0:
                # cv2.imshow("cropped_img", cropped_img)
                cv2.imwrite(cropped_img_path_ub + "/" + fileName, cropped_img_ub)
            else:
                print("Cannot find upper body")

            # 하의
            cropped_img_lb = detectLowerbody(image, output, imageWidth, imageHeight)
            if len(cropped_img_lb) != 0:
                # cv2.imshow("cropped_img", cropped_img)
                cv2.imwrite(cropped_img_path_lb + "/" + fileName, cropped_img_lb)
            else:
                print("Cannot find lower body")

            # 전신
            # cropped_img_fb = detectFullbody(image, output, imageWidth, imageHeight)
            # if len(cropped_img_fb) != 0:
            #     # cv2.imshow("cropped_img", cropped_img)
            #     cv2.imwrite(cropped_img_fb + "/" + fileName, cropped_img_fb)
            # else:
            #     print("Cannot find full body")
        except:
            print("이미지 불러오기 에러")

    # cv2.waitKey(0)
