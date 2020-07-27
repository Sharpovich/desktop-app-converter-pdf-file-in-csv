'''
Настольное приложение для конвертации данных из файла
формата PDF, в файл формата CSV
(C) 2019
'''

''' sys нужен для передачи argv в QApplication '''
import sys
''' import gui_EH импортирует наш интерфейс '''
from gui_EH import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF2 import PdfFileReader
''' пакет tabula-py для обработки формата PDF '''
import tabula

class MyWin(QtWidgets.QMainWindow):
    ''' Класс MyWin объединяет главный файл с интерфейсом.
    Так как файл с дизайном будет полностью перезаписываться
    каждый раз при изменении дизайна, мы не будем изменять его '''
    def __init__(self, parent=None):
        ''' модуль для доступа к переменным, методам в пакете gui_EH.py '''
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        ''' инициализации дизайна из пакета gui_EH '''
        self.ui.setupUi(self)
        ''' событие нажатия на кнопку '''
        self.ui.pushButton.clicked.connect(self.DomainCheck)

    ''' логика события взаимодействия с pushButton '''
    def DomainCheck(self):
        while True:
            try:
                ''' создание диалогового окна для ввода пользователем '''
                str_, btn = QtWidgets.QInputDialog.getText(self, 'Ввод', 'Файл PDF:',
                                                           text='')
                if btn:
                    x = str_
                ''' выставляется флаг False при нажатии на close() и закрывается программа '''
                if btn == False:
                    break
                ''' подсчёт количества страниц в файле '''
                with open(str(x) + '.pdf', 'rb') as f:
                    pdf = PdfFileReader(f)
                    number_of_pages = pdf.getNumPages()

                if number_of_pages >= 4:
                    n = number_of_pages - 2
                else:
                    n = number_of_pages - 1
                ''' Алгоритм моделя из пакета Tabula-py '''
                pageses = '1-' + str(n)
                tabula.convert_into(str(x) + '.pdf', 'Equipment.csv', output_format="csv", pages=pageses)
            except:
                continue
            else:
                break

if __name__=="__main__":
    ''' Новый экземпляр QApplication '''
    app = QtWidgets.QApplication(sys.argv)
    ''' Создаём объект класса MyWin '''
    myapp = MyWin()
    ''' Показываем окно '''
    myapp.show()
    ''' и запускаем приложение '''
    sys.exit(app.exec_())
