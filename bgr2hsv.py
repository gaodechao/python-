import cv2
img =cv2.imread("D:\\worksapce\\picture\\6.jpg")
#将BGR属性转化为HSV
img_hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# H空间中，绿色比黄色的值高一点，所以给每个像素+15，黄的树叶会变成绿色
turn_green_hsv =img_hsv.copy()
turn_green_hsv[:,:,0] = (turn_green_hsv[:,:,0]+15)%180
turn_green_img =cv2.cvtColor(turn_green_hsv,cv2.COLOR_HSV2BGR)
cv2.imwrite("D:\\worksapce\\picture\\6-turn_green.jpg",turn_green_img)
#减小饱和度会让图片损失鲜艳变得更灰
colorless_hsv = img_hsv.copy()
colorless_hsv[:,:,1] = 0.5 * colorless_hsv [:,:,1]
colorless_img =cv2.cvtColor(colorless_hsv,cv2.COLOR_HSV2BGR)
cv2.imwrite("D:\\worksapce\\picture\\6-colorless.jpg",colorless_img)
darker_hsv =img_hsv.copy()
darker_hsv[:,:,2] =0.5 * darker_hsv[:,:,2]
darker_img =cv2.cvtColor(darker_hsv,cv2.COLOR_HSV2BGR)
cv2.imwrite("D:\\worksapce\\picture\\6-darker.jpg",darker_img)
