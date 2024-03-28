from PyQt5 import QtCore, QtGui, QtWidgets
import Processing
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 430)
        MainWindow.setMinimumSize(QtCore.QSize(400, 430))
        MainWindow.setMaximumSize(QtCore.QSize(400, 430))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grbSelectFunc = QtWidgets.QGroupBox(self.centralwidget)
        self.grbSelectFunc.setGeometry(QtCore.QRect(10, 10, 380, 150))
        self.grbSelectFunc.setObjectName("grbSelectFunc")
        self.rdo1 = QtWidgets.QRadioButton(self.grbSelectFunc)
        self.rdo1.setGeometry(QtCore.QRect(10, 20, 360, 30))
        self.rdo1.setObjectName("rdo1")
        self.rdo2 = QtWidgets.QRadioButton(self.grbSelectFunc)
        self.rdo2.setGeometry(QtCore.QRect(10, 50, 360, 30))
        self.rdo2.setObjectName("rdo2")
        self.rdo3 = QtWidgets.QRadioButton(self.grbSelectFunc)
        self.rdo3.setGeometry(QtCore.QRect(10, 80, 360, 30))
        self.rdo3.setObjectName("rdo3")
        self.lblExp_2 = QtWidgets.QLabel(self.grbSelectFunc)
        self.lblExp_2.setGeometry(QtCore.QRect(202, 53, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lblExp_2.setFont(font)
        self.lblExp_2.setObjectName("lblExp_2")
        self.lblExp_3 = QtWidgets.QLabel(self.grbSelectFunc)
        self.lblExp_3.setGeometry(QtCore.QRect(132, 83, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lblExp_3.setFont(font)
        self.lblExp_3.setObjectName("lblExp_3")
        self.rdo4 = QtWidgets.QRadioButton(self.grbSelectFunc)
        self.rdo4.setGeometry(QtCore.QRect(10, 110, 360, 30))
        self.rdo4.setObjectName("rdo4")
        self.lbl2 = QtWidgets.QLabel(self.grbSelectFunc)
        self.lbl2.setGeometry(QtCore.QRect(117, 113, 15, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl2.setFont(font)
        self.lbl2.setObjectName("lbl2")
        self.grbTable = QtWidgets.QGroupBox(self.centralwidget)
        self.grbTable.setGeometry(QtCore.QRect(10, 170, 380, 140))
        self.grbTable.setObjectName("grbTable")
        self.spbNum = QtWidgets.QSpinBox(self.grbTable)
        self.spbNum.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.spbNum.setObjectName("spbNum")
        self.btnCre = QtWidgets.QPushButton(self.grbTable)
        self.btnCre.setGeometry(QtCore.QRect(80, 20, 60, 30))
        self.btnCre.setObjectName("btnCre")
        self.widgetY = QtWidgets.QWidget(self.grbTable)
        self.widgetY.setGeometry(QtCore.QRect(35, 100, 330, 30))
        self.widgetY.setObjectName("widgetY")
        self.layoutY = QtWidgets.QHBoxLayout(self.widgetY)
        self.layoutY.setContentsMargins(0, 0, 0, 0)
        self.layoutY.setObjectName("layoutY")
        self.lbl_Y = QtWidgets.QLabel(self.grbTable)
        self.lbl_Y.setGeometry(QtCore.QRect(10, 100, 30, 30))
        self.lbl_Y.setObjectName("lbl_Y")
        self.widgetX = QtWidgets.QWidget(self.grbTable)
        self.widgetX.setGeometry(QtCore.QRect(35, 60, 330, 30))
        self.widgetX.setObjectName("widgetX")
        self.layoutX = QtWidgets.QHBoxLayout(self.widgetX)
        self.layoutX.setContentsMargins(0, 0, 0, 0)
        self.layoutX.setObjectName("layoutX")
        self.lbl_X = QtWidgets.QLabel(self.grbTable)
        self.lbl_X.setGeometry(QtCore.QRect(10, 60, 30, 30))
        self.lbl_X.setObjectName("lbl_X")
        self.grbReturn = QtWidgets.QGroupBox(self.centralwidget)
        self.grbReturn.setGeometry(QtCore.QRect(10, 320, 380, 100))
        self.grbReturn.setObjectName("grbReturn")
        self.btnExec = QtWidgets.QPushButton(self.grbReturn)
        self.btnExec.setGeometry(QtCore.QRect(10, 20, 60, 30))
        self.btnExec.setObjectName("btnExec")
        self.lblHamso = QtWidgets.QLabel(self.grbReturn)
        self.lblHamso.setGeometry(QtCore.QRect(10, 60, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblHamso.setFont(font)
        self.lblHamso.setObjectName("lblHamso")
        self.lblExp = QtWidgets.QLabel(self.grbReturn)
        self.lblExp.setGeometry(QtCore.QRect(220, 50, 230, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblExp.setFont(font)
        self.lblExp.setText("")
        self.lblExp.setObjectName("lblExp")
        self.grbReturn.raise_()
        self.grbSelectFunc.raise_()
        self.grbTable.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnCre.clicked.connect(self.CreTextEdit)
        self.txtX_list = []
        self.txtY_list = []

        self.btnExec.clicked.connect(self.ProcessingFunc)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tìm hàm số bằng pp bình phương nhỏ nhất"))
        self.grbSelectFunc.setTitle(_translate("MainWindow", "Chọn dạng hàm số"))
        self.rdo1.setText(_translate("MainWindow", "Hàm số tuyến tính: y = ax + b"))
        self.rdo2.setText(_translate("MainWindow", "Hàm lũy thừa cơ số tự nhiên: y = ae"))
        self.rdo3.setText(_translate("MainWindow", "Hàm lũy thừa: y = ax"))
        self.lblExp_2.setText(_translate("MainWindow", "bx"))
        self.lblExp_3.setText(_translate("MainWindow", "b"))
        self.rdo4.setText(_translate("MainWindow", "Hàm bậc 2: y = ax + bx + c"))
        self.lbl2.setText(_translate("MainWindow", "2"))
        self.grbTable.setTitle(_translate("MainWindow", "Bảng giá trị thực tế"))
        self.btnCre.setText(_translate("MainWindow", "Tạo"))
        self.lbl_Y.setText(_translate("MainWindow", "Y:"))
        self.lbl_X.setText(_translate("MainWindow", "X:"))
        self.grbReturn.setTitle(_translate("MainWindow", "Kết quả"))
        self.btnExec.setText(_translate("MainWindow", "Thực thi"))
        self.lblHamso.setText(_translate("MainWindow", "Hàm số cần tìm là: y = "))

    def CreTextEdit(self):
        # Xóa hàng trước khi tạo hàng mới
        for cellX in self.txtX_list:
            self.layoutX.removeWidget(cellX)
            cellX.deleteLater()
        self.txtX_list = []
        for cellY in self.txtY_list:
            self.layoutY.removeWidget(cellY)
            cellY.deleteLater()
        self.txtY_list = []

        # Tạo bảng để nhập dữ liệu
        num = int(self.spbNum.text())
        for i in range(num):            
            self.txtX = QtWidgets.QTextEdit(self.centralwidget)
            self.txtX.setObjectName("X" + str(i))
            self.layoutX.addWidget(self.txtX)
            self.txtX_list.append(self.txtX)

            self.txtY = QtWidgets.QTextEdit(self.centralwidget)
            self.txtY.setObjectName("Y" + str(i))
            self.layoutY.addWidget(self.txtY)
            self.txtY_list.append(self.txtY)

    def ProcessingFunc(self):
        num = int(self.spbNum.text())
        valuesX = []
        valuesY = []
        for cellX in self.txtX_list:
            try:
                value = float(cellX.toPlainText())
            except:
                value = 0
            valuesX.append(value)
        for cellY in self.txtY_list:
            try:
                value = float(cellY.toPlainText())
            except:
                value = 0
            valuesY.append(value)
        
        preStr = "Hàm số cần tìm là: y = "
        expStr = ""
        try:
            if self.rdo1.isChecked():
                sumX2, sumXY = 0, 0
                sumX = sum(valuesX)
                sumY = sum(valuesY)
                for i in range(num):
                    sumX2 += valuesX[i]**2
                    sumXY += valuesX[i] * valuesY[i]
                a, b = Processing.solve_equation(sumX2, sumX, sumXY, sumX, num, sumY)
                if b < 0:
                    preStr = f"Hàm số cần tìm là: y = {a}x - {abs(b)}"
                else:
                    preStr = f"Hàm số cần tìm là: y = {a}x + {b}"
                expStr = ""
            if self.rdo2.isChecked():
                sumX2, sumXLnY, sumLnY = 0, 0, 0
                sumX = sum(valuesX)
                for i in range(num):
                    sumXLnY += valuesX[i] * math.log(valuesY[i])
                    sumLnY += math.log(valuesY[i])
                    sumX2 += valuesX[i]**2
                a, b = Processing.solve_equation(sumX2, sumX, sumXLnY, sumX, num, sumLnY)
                b = round(math.exp(b), 4)
                preStr = f"Hàm số cần tìm là: y = {b}.e"
                expStr = f"{a}x"
            if self.rdo3.isChecked():
                sumLnX, sumLnX2, sumLnXLnY, sumLnY = 0, 0, 0, 0
                for i in range(num):
                    sumLnXLnY += math.log(valuesX[i]) * math.log(valuesY[i])
                    sumLnY += math.log(valuesY[i])
                    sumLnX2 += math.log(valuesX[i])**2
                    sumLnX += math.log(valuesX[i])
                a, b = Processing.solve_equation(sumLnX2, sumLnX, sumLnXLnY, sumLnX, num, sumLnY)
                b = round(math.exp(b), 4)
                preStr = f"Hàm số cần tìm là: y = {b}.x"
                expStr = f"{a}"
            if self.rdo4.isChecked():
                sumX, sumX2, sumX3, sumX4, sumY, sumXY, sumX2Y = 0, 0, 0, 0, 0, 0, 0
                sumX, sumY = sum(valuesX), sum(valuesY)
                for i in range(num):
                    sumXY += valuesX[i] * valuesY[i]
                    sumX2Y += (valuesX[i]**2) * valuesY[i]
                    sumX2 += valuesX[i]**2
                    sumX3 += valuesX[i]**3
                    sumX4 += valuesX[i]**4
                a, b, c = Processing.solve_3_equations(sumX4, sumX3, sumX2, sumX2Y, sumX3, sumX2, sumX, sumXY, sumX2, sumX, num, sumY)
                if b < 0 or c < 0:
                    if b > 0:
                        preStr = f"Hàm số cần tìm là: y = {a}.x^2 + {b}x - {abs(c)}"
                    elif c > 0:
                        preStr = f"Hàm số cần tìm là: y = {a}.x^2 - {abs(b)}x + {c}"
                    else:
                        preStr = f"Hàm số cần tìm là: y = {a}.x^2 - {abs(b)}x - {abs(c)}"
                else:
                    preStr = f"Hàm số cần tìm là: y = {a}.x^2 + {b}x + {c}"
                expStr = ""
        except:
            preStr = "Không tìm được hàm số thỏa mãn!"
        self.lblHamso.setText(preStr)
        self.lblExp.setText(expStr)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
