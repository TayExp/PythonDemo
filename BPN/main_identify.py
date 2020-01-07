import cv2
import BPNetwork
import numpy as np
import matplotlib.pyplot as plt
HEIGHT = 32
WIDTH = 32

#图像预处理:
def preprocess_image(fpath, angle):
        img = cv2.imread(fpath)
        img = cv2.resize(img,(HEIGHT,WIDTH))
        # 图像颜色转换，转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray) # 进行非操作
        M = cv2.getRotationMatrix2D((WIDTH / 2, HEIGHT / 2), angle, 1)
        gray = cv2.warpAffine(gray,M,(HEIGHT,WIDTH))
        # 第三个参数：变换后的图像大小
        # 图像二值化
        thresh = cv2.threshold(gray,0,1,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # img_list
        return [j for item in thresh for j in item]
def whatShape(result):
    if result[0]<result[1]:
        return ("三角形")
    else:
        return("正方形")

# 分类训练

def main():
    #训练参数
    NumOfSamples = 100
    NumOfTraning = 42 # 70%
    NumOfValidation = 9 # 15%
    NumOfTesting = 9 # 15%
    output_array = np.asarray([[0, 1], [1, 0]]*50)
    input_array = np.empty((100, HEIGHT*WIDTH))
    angles = [10,20,30,40,50,60,75,85,95,105,0]
    for angle in range(10):
        for i in range(10):
            fpath = "D:\MIAOSFILE\BPN\\" + str(i+1) + ".jpg"
            input_array[10*angle+i,:] = np.asarray(preprocess_image(fpath,angles[angle]))

    net1 = BPNetwork.net(WIDTH*HEIGHT,44,2)
    net1.training(input_array,output_array,90)
    for i in range(90,100):
        result = net1.test(input_array[i])
        print("输出为[%.2f, %.2f],判断为%s-----实际图片：%s"%(result[0],result[1], whatShape(result),whatShape(output_array[i])))

if __name__ == '__main__':
    main()
