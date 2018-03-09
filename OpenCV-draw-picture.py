import numpy as np
import cv2
#定义一块宽600，高400的画布，初始化为白色
canvas =np.zeros((400,600,3),dtype=np.uint8)+255
#画一条纵向的正中央的黑色分界线
cv2.line(canvas,(300,0),(300,399),(0,0,0),2)
#画一条右半部分画面以150为界的横向分界线
cv2.line(canvas,(300,149),(599,149),(0,0,0),2)
#左半部分的右下角画个红色的圆
cv2.circle(canvas,(200,300),75,(0,0,255),5)
#左半部分的左下角画一个蓝色的矩形
cv2.rectangle(canvas,(20,240),(100,360),(255,0,0),thickness=3)
#定义两个三角形，并执行内部绿色填充
triangles = np.array([
    [(200,240),(145,333),(255,333)],
    [(60,180),(20,237),(100,237)],])
cv2.fillPoly(canvas,triangles,(0,255,0))
#画一个黄色五角星
#第一步通过旋转角度的办法求出5个顶点
phi= 4*np.pi/5
rotations =[[[np.cos(i*phi),-np.sin(i*phi)],[i*np.sin(phi),np.cos(i*phi)]] for i in range(1,5)]
pentagram= np.array([[[[0,-1]]   +   [np.dot(m,(0,-1)) for m in rotations]]],dtype=np.float)
#定义缩放的倍数和平移向量，把五角星画在左半部分画面的上方
pentagram =np.round(pentagram*80 + np.array([160,120])).astype(np.int)
#将五个顶点作为多边形顶点的连线，得到五角星
cv2.polylines(canvas,pentagram,True,(0,255,255),9)
#按照像素为间隔，从左到右在画面上画出HSV空间的色调的连续变化
for x in range(302,600):
    color_pixel = np.array([[[round(180*float(x-302)/298),255,255]]],dtype=np.uint8)
    line_color =[int(c) for c in cv2.cvtColor(color_pixel,cv2.COLOR_HSV2BGR)[0][0]]
    cv2.line(canvas,(x,0),(x,147),line_color)
#如果定义圆的线宽大于半径，则等效于画原点，随机在画面右下角的框内生成坐标
np.random.seed(42)
n_pts =30
pts_x =np.random.randint(310,590,n_pts)
pts_y =np.random.randint(160,390,n_pts)
pts =zip(pts_x,pts_y)
#画出每个点,颜色随机
for pt in pts:
    pt_color =[int(c) for c in np.random.randint(0,255,3)]
    cv2.circle(canvas,pt,3,pt_color,5)
cv2.putText(canvas,
            "python-opencv Drawing Example",
            (5,15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,0,0),
            1)
cv2.imshow('Example of basic drawing functions',canvas)
cv2.waitKey()



