from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QAction
from PyQt5.QtCore import QCoreApplication
from sys import argv, exit
import fileParser


class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Parse PDF to CSV')
        self.statusBar().showMessage('Ожидание пути к файлу')
        btn1 = QPushButton('Выход', self)
        btn1.setBaseSize(btn1.sizeHint())
        btn1.move(10, 50)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn2 = QPushButton('выбрать', self)
        btn2.setBaseSize(btn2.sizeHint())
        btn2.move(120, 50)
        btn2.clicked.connect(self.openFile)

        self.show()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '~/')
        self.statusBar().showMessage(f'обработка файла: {fname[0]}')
        if not fileParser.chekFormatFile(fname[0]):
            self.statusBar().showMessage('Файл не соответствует расширению PDF')
        else:
            self.statusBar().showMessage('Расширение проверено, идет обработка')
            fileParser.convertPDFtoCSV(fname[0])
            self.statusBar().showMessage('Файл сконвертирован в папку с файлом PDF')


if __name__ == '__main__':
    app = QApplication(argv)
    x = MyWin()
    exit(app.exec_())
