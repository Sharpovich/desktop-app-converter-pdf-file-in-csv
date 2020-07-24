import sys
# sys нужен для передачи argv в QApplication
from gui_EH import * # Импортируем наш интерфейс
from PyQt5 import QtCore, QtGui, QtWidgets
from PyPDF2 import PdfFileReader
import tabula

# Так как файл с дизайном будет полностью перезаписываться
# каждый раз при изменении дизайна, мы не будем изменять его.
# Вместо этого мы создадим новый класс MyWin,
# который объединим с кодом дизайна для использования
# всех его функций: #
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле test.py
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # Это нужно для инициализации нашего дизайна
# В этом классе мы будем взаимодействовать с элементами интерфейса,
# добавлять соединения и всё остальное, что нам потребуется.
# Но для начала нам нужно инициализировать класс при запуске кода.
# С этим мы разберёмся в функции main():
        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.DomainCheck)

        # при нажатии на кнопку
    def DomainCheck(self):
        while True: # цикл исполнения
            try: # условие
                str_, btn = QtWidgets.QInputDialog.getText(self, 'Ввод', 'Файл PDF:',
                                                           text='')  # создание диалогового окна для ввода пользователем
                if btn:
                    x = str_
                if btn == False: # выставляется флаг False при нажатии на close() и закрывается программа
                    break
                with open(str(x) + '.pdf', 'rb') as f: # подсчёт количества страниц в файле
                    pdf = PdfFileReader(f)
                    number_of_pages = pdf.getNumPages()

                if number_of_pages >= 4:
                    n = number_of_pages - 2
                else:
                    n = number_of_pages - 1
                # Алгоритм табулы. main
                pageses = '1-' + str(n)
                tabula.convert_into(str(x) + '.pdf', 'Equipment.csv', output_format="csv", pages=pageses)
            except: # обработка исключений
                continue
            else:
                break

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
    myapp = MyWin() # Создаём объект класса MyWin
    myapp.show() # Показываем окно
    sys.exit(app.exec_()) # и запускаем приложение
