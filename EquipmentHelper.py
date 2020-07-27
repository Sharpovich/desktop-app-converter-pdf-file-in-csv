'''
Настольное приложение для конвертации данных из файла
формата PDF, в файл формата CSV
(C) 2019
'''

import sys # sys нужен для передачи argv в QApplication
from gui_EH import * # import gui_EH импортирует наш интерфейс
from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF2 import PdfFileReader
import tabula # пакет tabula-py для обработки формата PDF

class MyWin(QtWidgets.QMainWindow):
    ''' 
    Класс MyWin объединяет главный файл с интерфейсом.
    Так как файл с дизайном будет полностью перезаписываться
    каждый раз при изменении дизайна, мы не будем изменять его 
    __init__: модуль для доступа к переменным, методам в пакете gui_EH.py
    DomainCheck: модуль взимодействия с логикой конвертатора
    '''
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # инициализации дизайна из пакета gui_EH
        self.ui.pushButton.clicked.connect(self.DomainCheck) # событие нажатия на кнопку
        
    def DomainCheck(self):
        '''
        Модуль DomainCheck служит для взаимодействия основного алгоритма конвертации с интерфейсом
        кнопки инициализации
        convert_into(): Алгоритм модуля из пакета Tabula-py
        '''
        while True:
            try:
                # создание диалогового окна для ввода пользователем
                str_, btn = QtWidgets.QInputDialog.getText(self, 'Ввод', 'Файл PDF:',
                                                           text='')
                if btn:
                    x = str_
                # выставляется флаг False при нажатии на close() и закрывается программа
                if btn == False:
                    break
                # подсчёт количества страниц в файле
                with open(str(x) + '.pdf', 'rb') as f:
                    pdf = PdfFileReader(f)
                    number_of_pages = pdf.getNumPages()

                if number_of_pages >= 4:
                    n = number_of_pages - 2
                else:
                    n = number_of_pages - 1
                pageses = '1-' + str(n)
                convert_into(str(x) + '.pdf', 'Equipment.csv', output_format="csv", pages=pageses)
            except:
                continue
            else:
                break

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
    myapp = MyWin() # Создаём объект класса MyWin
    myapp.show() # Показываем окно
    sys.exit(app.exec_()) # и запускаем приложение
