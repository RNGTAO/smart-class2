"""
人脸检测测试
测试点：1、电脑摄像头能否正常打开 2、人脸特征库能否正常加载 3、捕捉到的图像能否正常显示
4、摄像头和显示窗口能否正常关闭
"""

import cv2
# 使用第1个摄像头
camera_port = 0
cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
# 加载人脸特征库
face_cascade = cv2.CascadeClassifier(
    'D:/python3.8/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

while True:
    # 读取一帧的图像
    ret, frame = cap.read()
    # 将读取的彩色图像转换为灰色图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))  # 检测人脸
    # 用矩形圈出人脸
    # 对人脸的四个特征值进行遍历
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 显示灰色图像q
    cv2.imshow('Face Recognition', gray)
    # 0xFF:位掩码，将数据的前24位置为0
    # 判断键盘键入的值是否是ESC，若是ESC，则退出视频显示
    # ESC的unicode编码为27
    if (cv2.waitKey(1) & 0xFF) == 27:
        break

# 释放摄像头
cap.release()
# 关闭显示窗口
cv2.destroyAllWindows()
