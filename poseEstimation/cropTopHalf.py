import cv2
import os

# 이미지를 절반으로 자르고 위만 남김

path_dir = "./data"
file_list = os.listdir(path_dir)

cropped_dir = path_dir + "/half_cropped"
if not os.path.isdir(cropped_dir):
    os.mkdir(cropped_dir)

for fileName in file_list:
    image_path = path_dir+"/"+fileName

    try:
        image = cv2.imread(image_path)
        print(image_path)
        image = cv2.imread(image_path)
        imageHeight, imageWidth, _ = image.shape
        cropped_img = image[0: int(imageHeight/2), :]
        cv2.imwrite(cropped_dir + "/" + fileName, cropped_img)
    except:
        print("crop 에러")

    # cv2.waitKey(0)
