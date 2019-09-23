from PyQt5 import QtCore, QtWidgets
from show_scenery_rank.DAL import DB
from show_scenery_rank.BLL import chartAnalysis,saveWeight

operate = DB.operateDB()
# 如果权重表为空现将权重表填满
if operate.countSceneryWeight() == 0:
    saveWeight.calAffection()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # footer
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.gofront(MainWindow))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.gonext(MainWindow))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 510, 61, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 510, 61, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 510, 51, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.goskip(MainWindow))

        # table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 71, 731, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(13)
        for i in range(13):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # header
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 111, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 51, 20))
        self.label.setObjectName("label")
        self.QPushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.QPushButton_0.setGeometry(QtCore.QRect(440, 28, 51, 24))
        self.QPushButton_0.setObjectName("commandLinkButton")
        self.QPushButton_0.clicked.connect(lambda: self.gogo(MainWindow))
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 30, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 30, 51, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(676, 28, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.paintall(MainWindow))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "景点信息"))
        self.pushButton.setText(_translate("MainWindow", "上一页"))
        self.pushButton_2.setText(_translate("MainWindow", "下一页"))
        for i in range(13):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", str(i+1)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "城市编码"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "景点编码"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "景点名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "排名"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "等级"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "简介"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "操作"))
        self.label.setText(_translate("MainWindow", "城市名："))
        self.QPushButton_0.setText(_translate("MainWindow", "查找"))
        self.label_2.setText(_translate("MainWindow", "景点名："))
        self.label_3.setText(_translate("MainWindow", "0/0页"))
        self.pushButton_3.setText(_translate("MainWindow", "跳转"))
        self.pushButton_4.setText(_translate("MainWindows", "总体绘图"))

    # 列表内添加按钮
    def buttonForRow(self,id):
        widget=QtWidgets.QWidget()

        # 生成图形
        getChart = QtWidgets.QPushButton('图形')
        getChart.setStyleSheet("QPushButton{background:#CCCCFF;font:10px}")
        getChart.clicked.connect(lambda:self.buildChart(id))

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(getChart)
        hLayout.setContentsMargins(13, 2, 15, 2)
        widget.setLayout(hLayout)
        return widget

    # 构图函数
    def buildChart(self,id):
        try:
            scenery_name = self.tableWidget.item(id, 2).text()
            scenery_number = self.tableWidget.item(id, 1).text()
            chartAnalysis.getThread(scenery_name,scenery_number).start()
        except:
            print('ERROR')

    # 表格数据填入
    def inputData(self,scenery_name,num):
        self.tableWidget.clearContents()
        if scenery_name == '':
            results = operate.searchScenery(scenery_name,num)
        else:
            results = operate.searchScenery(scenery_name,num)
        i = 0
        j = 0
        for rows in results:
            for result in rows:
                if j == 6:
                    break
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(result)))
                j += 1
            self.tableWidget.setCellWidget(i, 6, self.buttonForRow(i))
            j = 0
            i += 1

    # 数据查找
    def gogo(self,MainWindow):
        city_name = self.lineEdit.text()
        scenery_name = self.lineEdit_2.text()
        if city_name == '':
            city_name = '大连'
        result = operate.searchCity(city_name)
        if result:
            city_number = result[0][0]
            if scenery_name == '':
                result_2 = operate.countScenery(city_number, '')
            else:
                result_2 = operate.countScenery(city_number,scenery_name)
            if result_2:
                self.inputData(scenery_name,0)
                self.label_3.setText("1/%d页"%(result_2/13 + 1))
            else:
                QtWidgets.QMessageBox.about(MainWindow, "ERROR", "没有类似该名称景点")
        else:
            QtWidgets.QMessageBox.about(MainWindow, "ERROR", "没有该城市")


    # 页面跳转
    def goskip(self,MainWindow):
        scenery_name = self.lineEdit_2.text()
        if not self.lineEdit_3.text():
            QtWidgets.QMessageBox.about(MainWindow, "ERROR", "跳转页面不能为空")
        else:
            allpage = int((self.label_3.text().split('/')[1])[:-1])
            page = int(self.lineEdit_3.text())
            if page > allpage or page == 0:
                QtWidgets.QMessageBox.about(MainWindow, "ERROR", "超过页面总数")
                self.lineEdit_3.setText('')
            else:
                self.inputData(scenery_name,page)
                self.label_3.setText("%d/%d页" % (page, allpage))
                self.lineEdit_3.setText('')

    # 下一页
    def gonext(self,MainWindow):
        scenery_name = self.lineEdit_2.text()
        tmppage = self.label_3.text().split('/')
        allpage = int((tmppage[1])[:-1])
        page = int(tmppage[0])
        page += 1
        if page > allpage:
            QtWidgets.QMessageBox.about(MainWindow, "ERROR", "超过页面总数")
        else:
            self.inputData(scenery_name,page)
            self.label_3.setText("%d/%d页" % (page, allpage))

    # 上一页
    def gofront(self,MainWindow):
        scenery_name = self.lineEdit_2.text()
        tmppage = self.label_3.text().split('/')
        allpage = int((tmppage[1])[:-1])
        page = int(tmppage[0])
        page -= 1
        if page <= 0:
            QtWidgets.QMessageBox.about(MainWindow, "ERROR", "页面数不能小于1")
        else:
            self.inputData(scenery_name,page)
            self.label_3.setText("%d/%d页" % (page, allpage))

    # 绘制已查询的评论线形图
    def paintall(self, MainWindow):
        try:
            scenery_name = self.lineEdit_2.text()
            chartAnalysis.getThread(scenery_name,'').start()
        except:
            print("ERROR")

    # 热评景点显示
    def showhot(self, MainWindow):
        pass
