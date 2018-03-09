import cv2
import numpy as np
img=cv2.imread("D:\\worksapce\\picture\\5.jpg")
#沿着横纵轴放大1.6倍，然后平移到（150,240），最后沿着原图大小截取，等效于裁剪并放大
M_crop_elephant = np.array(
    [[1.6,0,-150.0],
    [1, 1.6, -240]],
    dtype=np.float32
)
img_water= cv2.warpAffine(img,M_crop_elephant,(1200,750))
cv2.imwrite("D:\\worksapce\\picture\\5-water.jpg",img_water)
# x轴的剪切变换，角度15
theta =15 * np.pi/180
M_shear =np.array(
    [[1,np.tan(theta),0],
    [0, 1, 0]],
    dtype=np.float32)
img_shared =cv2.warpAffine(img,M_shear,(1200,750))
cv2.imwrite("D:\\worksapce\\picture\\5-share.jpg",img_shared)
M_rotate= np.array([
    [np.cos(theta),-np.sin(theta),0],
    [np.sin(theta),np.cos(theta),0]],
    dtype=np.float32)
img_rotate =cv2.warpAffine(img,M_rotate,(1200,750))
cv2.imwrite("D:\\worksapce\\picture\\5-rotate.jpg" ,img_rotate)
#某种变换，具体的几何意义可以通过SVD分解理解
M= np.array([
    [1,1.5,-400],
    [0.5,2,-100]
],dtype=np.float32)
img_transformed =cv2.warpAffine(img,M,(1200,750))
cv2.imwrite("D:\\worksapce\\picture\\5-rotate.jpg",img_transformed)
