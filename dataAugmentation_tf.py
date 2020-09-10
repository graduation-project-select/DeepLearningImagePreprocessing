import urllib

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers
AUTOTUNE = tf.data.experimental.AUTOTUNE

import tensorflow_docs as tfdocs
import tensorflow_docs.plots

import tensorflow_datasets as tfds

import PIL.Image

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12, 5)

import numpy as np
from imutils import paths

import cv2 as cv
import os


root_dir_path = './argTest/' # target images directory
root_dir = os.listdir(root_dir_path)

result_root_dir = './augmentation_images' # 결과 저장할 폴더


def save(keyPath, file_name, type, img):
  saved_dir = result_root_dir
  if os.path.isdir(saved_dir) != True:
    os.mkdir(saved_dir) #./augmentation_images
  if os.path.isdir(keyPath) != True:
    os.mkdir(keyPath) #./augmentation_images/top

  saved_name = os.path.join(keyPath, "{}{}.{}".format(file_name.split('.')[0], type, 'jpg'))
  tf.keras.preprocessing.image.save_img(saved_name, img)

def augmente(keyName, rate=None, if_scale=False):
  saved_dir = result_root_dir
  keyPath = os.path.join(root_dir_path, keyName)  # keypath direct to root path
  # category = keyPath.split(os.sep)[-1]  # 카테고리 별로 폴더 나누기 위해 지정 -> 제대로 작동 x
  category = keyPath.split("/")[-1]
  saved_dir = saved_dir + "/" + category
  datas = os.listdir(keyPath)
  data_total_num = len(datas)
  print("Overall data in {} Path :: {}".format(keyPath, data_total_num))

  try:
    for data in datas:
      # type = "_scale_"
      data_path = os.path.join(keyPath, data)
      img = cv.imread(data_path)
      shape = img.shape
      ###### data saturated ######
      # data_saturated(saved_dir, data, img, True)

      ###### data brightness ######
      data_brightness(saved_dir, data, img, True)

      ####### Image Scale #########
      # if if_scale == True:
      #   print("Start Scale!")
      #   x = shape[0]
      #   y = shape[1]
      #   f_x = x + (x * (rate / 100))
      #   f_y = y + (y * (rate / 100))
      #   cv.resize(img, None, fx=f_x, fy=f_y, interpolation=cv.INTER_CUBIC)
      #   img = img[0:y, 0:x]
      #
      #   save(saved_dir, data, img, rate, type)
      ############################

    # plt.imshow(img)
    # plt.show()
    return "success"

  except Exception as e:
    print(e)
    return "Failed"

def data_saturated(saved_dir, file_name, img, saving_enable=False):
  img = tf.image.adjust_saturation(img, 3)
  if saving_enable == True:
    save(saved_dir, file_name, "_saturated", img)

def data_brightness(saved_dir, file_name, img, saving_enable=False):
  img = tf.image.adjust_brightness(img, -0.1) # 0.1, -0.1
  if saving_enable == True:
    save(saved_dir, file_name, "_bright-01", img)

def main_TransformImage(keyNames):
  try:
    for keyname in keyNames:
      # print(keyname)
      augmente(keyname)  # scaling
    return "Augment Done!"
  except Exception as e:
    print(e)
    return "Augment Error!"


main_TransformImage(root_dir)


# image_path = "cat.png"
# PIL.Image.open(image_path)
#
# image_string=tf.io.read_file(image_path)
# image=tf.image.decode_jpeg(image_string,channels=3)
#
# data_saturated('bright1.png', image, True)





