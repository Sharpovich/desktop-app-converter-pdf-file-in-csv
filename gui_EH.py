# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Equipment_Convert")
        MainWindow.resize(977, 490)
        MainWindow.move(58,50)
        MainWindow.setMaximumSize(QtCore.QSize(977, 490))
        MainWindow.setMinimumSize(QtCore.QSize(977, 490))
        MainWindow.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 500, 40))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(812, 45, 141, 151))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("LOGO1.png"))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 398, 200, 45))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 22pt \"Algerian\";\n"
                                      "selection-color: rgb(229, 188, 168);\n"
                                      "background-color: rgb(233, 172, 172);")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 50, 760, 340))
        self.textBrowser.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(7)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setTabStopWidth(80)
        self.textBrowser.setObjectName("textBrowser")
        self.labeloto = QtWidgets.QLabel(self.centralwidget)
        self.labeloto.setGeometry(QtCore.QRect(789, 432, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Pristina")
        font.setPointSize(14)
        self.labeloto.setFont(font)
        self.labeloto.setObjectName("labeloto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 892, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menubar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Equipment Helper", "Equipment Helper"))
        self.label.setText(_translate("MainWindow", "Для конвертации данных из PDF в CSV следуйте инструкции:"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\">Данный файл, </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:italic;\">Equipment Helper</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\">, разработан как дополнение к инструменту </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:italic;\">Merch Project</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\">.</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\">Инструмент </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:italic;\">Merch Project</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\"> в свою очередь создан для автоматизации заполнения </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:600; font-style:italic;\">шаблона БО</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-style:italic;\"> необходимым количеством оборудования и устранения ошибок при переносе данных.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600;\">Инструкция: </span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">1)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> В папку с файлом </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Equipment Helper</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> необходимо переместить </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">PDF</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> файл планограммы.                                            После открыть инструмент</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\"> Merch Project.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">2)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> Для осуществления конвертации нажмите </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">&quot;START&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> в файле </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Equipment Helper </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">и</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\"> </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">введите название pdf файла, который находится в папке с файлом </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">(только название, без &quot;.pdf&quot;)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">, далее нажмите кнопку &quot;ОК&quot;</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">3)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> При верном указании наименования файла, файл будет успешно сконвертирован в формат таблицы с наименованием </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">&quot;Equipment&quot;. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">В случае если вы не верно укажете наименование файла, то </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Equipment Helper</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> предложит ввести наименование повторно.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">4)</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> Необходимо открыть и перейти в инструмент </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">Merch Project</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> на вкладку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">&quot;Выгрузка источник&quot;</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> и нажать на кнопку </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">&quot;Пуск&quot;. </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Откроется браузерное окно выбора файла. Необходимо выбрать файл 'Equipment.csv'. Данные будут перенесены в инструмент для расчёта оборудования автоматически.</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">---------------------------------------------------------------------------</span></p></body></html>"))
        self.labeloto.setText(_translate("MainWindow", "by Equipment for retail facilities"))
        self.menu.setTitle(_translate("MainWindow", "Converter"))
        self.action_2.setText(_translate("MainWindow", "Меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
