import cv2
import os
import sys
#第一个参数输入的是视频的路径
input_path =sys.argv[1]
#第二个参数输入的是设定每隔多少帧截取一帧
frame_interval = int(sys.argv[2])
#列出文件下所有的视频文件
filenames = os.listdir(input_path)
#获取文件的名称
video_prefix=input_path.split(os.sep)[-1]
#建立一个新的文件夹，名称为原来文件夹后加上_frames
frame_path="{}_frame".format(input_path)
if not os.path.exists(frame_path):
	os.mkdir(frame_path)
#初始化一个videoCapture 对象
cap = cv2.VideoCapture()
#遍历所有文件
for filename in filenames:
	filepath=os.path.join([input_path,filename])
    # VideoCapture::open 函数 可以从文件中获取视频
    cap.open(filepath)

    #获取视频的帧数
    n_frames =int (cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #同样为了避免视频头几帧质量低下，黑屏或者无关等
    for i in range(42):
        cap.read()

    for i in range(n_frames):
        ret ,frame =cap.read()
        #每隔frame_interval帧进行一次截屏操作
        if i% frame_interval == 0:
            imagename= "{}_{}_{:>6d}.jpg".format(video_prefix,filename.split(".")[0],i)
            imagepath=os.sep.join([frame_path,imagename])
            print("export {} !".format(imagepath))
            cv2.imwrite(imagepath,frame)
#执行结束后释放资源
cap.release()




