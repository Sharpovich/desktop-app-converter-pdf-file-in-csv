from PyPDF2 import PdfFileReader
import tabula
from os import path


def chekFormatFile(pathToFile: str, endOfFile: str = 'pdf') -> bool:
    """
    Функция проверяет соответствие расширения файла заданному указанному расширению
    :param pathToFile: путь к файлу
    :param endOfFile: проверяемое расширение
    :return: возвращает True если расширение совпадает и False если расширение не совпадает
    """

    return pathToFile.endswith(f'.{endOfFile}')


def convertPDFtoCSV(pathToFile: str):
    """
    Конвертирует файл с рашсирением PDF в файл с расширением CSV
    :param pathToFile: Путь к файлу
    :return:
    """
    head_tail = path.split(pathToFile)
    # подсчёт количества страниц в файле
    with open(pathToFile, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()

    if number_of_pages >= 4:
        n = number_of_pages - 2
    else:
        n = number_of_pages - 1
    pageses = '1-' + str(n)
    tabula.convert_into(path.join(head_tail[0], head_tail[1]),
                        path.join(head_tail[0], f'{head_tail[1].split(".")[0]}.csv'),
                        output_format="csv",
                        pages=pageses)


if __name__ == '__main__':
    pathToFile = path.split('fileParser.py')

    print(pathToFile[0], pathToFile[1])


