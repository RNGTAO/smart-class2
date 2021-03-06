# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'repair.ui'
# Created by: PyQt5 UI code generator 5.6
"""
教室保修模块
改模块实现了对教室物品的报修,并将保修信息存到后台数据库
该模块类中有四个函数
"""
"""
该模块已经测试完毕，能够正常运行各个方法
"""

from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtGui import *
import pymysql
import CONFIG


class Ui_Dialog_repair(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        # 设置窗口的大小(长和宽)
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 1051, 701))
        self.label_2.setStyleSheet("QLabel{\n""background:white;;\n""}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 760, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 91, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 260, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 260, 81, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 170, 161, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 350, 111, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 170, 171, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 170, 141, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 260, 171, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 260, 141, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 400, 961, 311))
        self.textEdit.setObjectName("textEdit")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        """
        # 读取图片
        # 显示图片
        self.beijing.setPixmap(pix)
        QPixmap用于在标签或者按钮上面显示图像
        QPixmap支持的图像格式有BMP、GIF、JPG、JPEG、PNG、PBM、PGM、PPM、XBM、XPM等
        """
        self.beijing.setPixmap(QPixmap(CONFIG.address))
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)
        # 提交按钮点击后执行register方法，将报修数据提交到数据库
        self.pushButton.clicked.connect(self.register)
        # 点击返回按钮将会清空当前所有输入框中的内容
        self.pushButton_2.clicked.connect(self.cleanall)
    """
    对窗口当中的输入框进行设置
    """
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        # 设置窗口名称
        Dialog.setWindowTitle(_translate("Dialog", "教室维修申请"))
        # self.lineEdit.setText(CONFIG.classroomAddress)
        self.lineEdit.setPlaceholderText(CONFIG.classroomAddress)
        self.pushButton.setText(_translate("Dialog", "提交"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">教室号：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">报修物品：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">损坏情况：</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">数量：</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">报修物品种类：</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">详情补充：</span></p></body></html>"))

# 该模块还需要对每一个文本框的输入进行验证

# 测试每一个输入框的值是否会出现乱码等现象
    def register(self):
        # 教室地址
        classroomAddress = self.lineEdit.text()
        # print(classroomAddress)
        # 保修物品名称
        objectname = self.lineEdit_2.text()
        # print(type(objectname))
        # print(objectname)
        # 保修物品种类
        type1= self.lineEdit_3.text()
        # 损坏情况
        situation = self.lineEdit_5.text()
        print(type(situation))
        # print(situation)
        # 损坏数量
        count = self.lineEdit_6.text()
        # print(count)
        # 详情补充
        remark = self.textEdit.toPlainText()
        # print(remark)
        # 数据库连接，连接数据库中的repair表
        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db=CONFIG.db, charset='utf8')
        cursor = conn.cursor()
        sql = "INSERT INTO repair (classroomAddress,objectname,type,situation,Problem_Count,remark,state) values ('%s','%s','%s','%s','%s','%s','%s')" % \
              (classroomAddress,objectname,type1,situation,count,remark,'未处理')
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            print("问题成功提交")
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            # 如果发生错误则回滚
            print("数据提交失败")
            print(e)
            conn.rollback()
        self.cleanall()


    def cleanall(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.textEdit.setText("")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_repair()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())