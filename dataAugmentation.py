# import modules for image preprocessing
import cv2 as cv
import matplotlib.pyplot as plt
import os, sys


#image parse in directory

root_dir_path = './argTest/' #target images directory
root_dir = os.listdir(root_dir_path)
# print(root_dir)

result_root_dir = "./augmentation_images"

def save(keyPath, file_name, cv_img, rate, type):
    '''
    save method need to save before image preprocessing.
    It has five arguments and requirement all.
    
    keyPath is root path of original image.
    file_name is original image file name
    cv_img is whole signal of the image
    rate is for scale value
    
    '''
    saved_dir = result_root_dir
    if os.path.isdir(saved_dir) != True:
        os.mkdir(saved_dir)
    if os.path.isdir(keyPath) != True:
        os.mkdir(keyPath)
    
    saved_name = os.path.join(keyPath,"{}{}.{}".format(file_name.split('.')[0], type, 'jpg'))
    #print(saved_name)
    # cv_img = cv.cvtColor(cv_img, cv.COLOR_BGR2GRAY) #gray scale (모델 train 시 전처리에 사용)
    cv.imwrite(saved_name, cv_img)


def augmente(keyName, rate=None, if_scale=False):
    saved_dir = result_root_dir
    
    keyPath = os.path.join(root_dir_path, keyName) # keypath direct to root path
    print(keyPath)
    # category = keyPath.split(os.path.sep)[-1] # 카테고리 별로 폴더 나누기 위해 지정
    category = keyPath.split("/")[-1]
    saved_dir = saved_dir + "/" + category
    datas = os.listdir(keyPath)
    data_total_num = len(datas)
    print("Overall data in {} Path :: {}".format(keyPath, data_total_num))
    
    try:
        for data in datas:
            type = "_scale_"
            data_path = os.path.join(keyPath, data)
            img = cv.imread(data_path)
            shape = img.shape
            ###### data rotate ######
            # data_rotate(saved_dir, data, img, 20, "_rotate_", saving_enable=True)
            
            ###### data flip and save #####
            data_flip(saved_dir, data, img, rate, 1, True) # verical random flip
            # data_flip(saved_dir, data, img, rate, 0, False) # horizen random flip
            # data_flip(saved_dir, data, img, rate, -1, False) # both random flip
            
            ####### Image Scale #########
            if if_scale == True:
                print("Start Scale!")
                x = shape[0]
                y = shape[1]
                f_x = x + (x * (rate / 100))
                f_y = y + (y * (rate / 100))
                cv.resize(img, None, fx=f_x, fy=f_y, interpolation = cv.INTER_CUBIC)
                img = img[0:y, 0:x]
                
                save(saved_dir, data, img, rate, type)
            ############################
                        
        #plt.imshow(img)
        #plt.show()
        return "success"
    
    except Exception as e:
        print(e)
        return "Failed"


def data_flip(saved_dir, data, img, rate, type, saving_enable=False):
    
    img = cv.flip(img, type)
    try:
        if type == 0:
            type = "_horizen_"
        elif type == 1:
            type = "_vertical_"
        elif type == -1:
            type = "_bothFlip_"
        
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)
    
    except Exception as e:
        print(e)
        return "Failed"

def data_rotate(saved_dir, data, img, rate, type, saving_enable=False):
    
    xLength = img.shape[0]
    yLength = img.shape[1]
    
    try:
        rotation_matrix = cv.getRotationMatrix2D((xLength/2 , yLength/2), rate, 1)
        img = cv.warpAffine(img, rotation_matrix, (xLength, yLength))
        #print(img.shape)        
        if saving_enable == True:
            save(saved_dir, data, img, rate, type)
        
        return "Success"
    except Exception as e:
        print(e)
        return "Failed"

def main_TransformImage(keyNames):
    try:
        for keyname in keyNames:
            print(keyname)
            augmente(keyname, 20) # scaling

        return "Augment Done!"
    except Exception as e:
        print(e)
        return "Augment Error!"


main_TransformImage(root_dir)