import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.select_data)


    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        self.con = sqlite3.connect('coffee')

        # Создание курсора
        cur = self.con.cursor()

        # Выполнение запроса и получение всех результатов
        res = cur.execute("""SELECT * FROM Espresso""").fetchall()

        # Вывод результатов на экран
        for elem in res:
            print(elem)

        self.con.close()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())