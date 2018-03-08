import matplotlib.pyplot as plt
plt.figure('An Orange car')
#图片路径
pic_path="D:\\worksapce\\picture\\1.jpg"
little_dog_img= plt.imread(pic_path)
plt.imshow(little_dog_img)
plt.show()
#Z 是随机生成的图像????
"""img0 = Z
img1 =3*Z +4
fig =plt.figure("Auto Mormalized Visualization")
ax0 =fig.add_subplot(121)
ax0.imshow(img0,camp='gray')
ax1 =fig.add_subplot(122)
ax1.imshow(img1,cmap='gray')
plt.show()
"""