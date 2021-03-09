# 将图片以二进制流的方式存放到数据库中

import cv2
import pymysql
import CONFIG
def toBinary(fileAddress):
    fp=open(fileAddress,'rb')
    img=fp.read()
    fp.close()
    conn=pymysql.connect(host=CONFIG.host,port=3306,user="root",password=CONFIG.hostps,db=CONFIG.db,charset="utf8")
    cur=conn.cursor()
    sql="insert into face_picture(image) values (%s);"
    args=(img)
    try:
        cur.execute(sql,args)
        conn.commit()
    except Exception as e:
        print("人脸图像上传数据库失败")
        print(e)
        conn.rollback()
    # cv2.namedWindow("test",cv2.WINDOW_NORMAL)
    # cv2.imshow("test",picture)
    # cv2.waitKey(0)

if __name__=='__main__':
    toBinary(CONFIG.test_picture)

