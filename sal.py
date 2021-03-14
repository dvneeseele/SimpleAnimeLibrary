#############################################################################
# me
#############################################################################


from sal_ui import salUI
import os
import sys
import sqlite3
import requests
import pandas as pd


from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QTextListFormat, QFont, QColor
from PyQt5.QtCore import QEvent, Qt, QSize, QDate, QTime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QPushButton, QListWidgetItem, QLabel, QVBoxLayout, QStackedWidget,
                            QColorDialog, QMessageBox, QFileDialog, QDialog, QFontDialog, QTableWidgetItem)



class SAL_app(salUI):
    def __init__(self):
        super().__init__()

        self.mainWindow = QMainWindow()
        self.setupUI(self.mainWindow)

        # Menubar functions

        # TODO

        # Toolbar functions

        # TODO

        # load function here
        self.dbLoad()






    def getCurrentStack(self):
        pass



    def newDB(self):
        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()

        createTable = "CREATE TABLE IF NOT EXISTS watchlist(Art BLOB, Title TEXT PRIMARY KEY, English_Title TEXT, Format TEXT, Completion_Date TEXT, Series_Type TEXT)"

        cursor.execute(createTable)

        # for testing
        with open("naruto.jpg", 'rb') as file:
            blob = file.read()

        entry_tuple = (blob, 'ani', 'Anime', 'SUB', '12/01/2021', 'ORI')

        # for testing
        # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Completion_Date, Series_Type) VALUES ({}, 'ani', 'Anime', 'SUB', '12/01/2021', 'ORI')".format(blob))

        # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Completion_Date, Series_Type) VALUES ({}, 'qwer', 'Anime22', 'DUB', '120/90/2021', 'SQ')".format(blob))

        cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?)", entry_tuple)

        conn.commit()

        # this = cursor.execute("SELECT * FROM watchlist")

        # for row in this:
        #     print('Row :', row)

        conn.close()






    def dbLoad(self):
        
        # pandas vs just for loop over db??

        if os.path.exists('saldb.sqlite'):
            # if os.path.exists method because the below creats the file if it doesn't exist
            #conn = sqlite3.connect('saldb.sqlite')
            conn = sqlite3.connect('saldb.sqlite')
            cursor = conn.cursor()            

        else:
            # qmessagebox to say there was not a 'saldb.sqlite' db found in the directory so a new one will be created.
            dbFileErrorMsg = QMessageBox.question(self.mainWindow, 'Error - Database Not Found', 'saldb.sqlite db file was not found in the current directory press ok and a new one will be created.', QMessageBox.Ok, QMessageBox.Cancel)

            if dbFileErrorMsg == QMessageBox.Ok:
                self.newDB()
                conn = sqlite3.connect('saldb.sqlite')
                cursor = conn.cursor()
            else:
                sys.exit()


                # need to make new tables to put into database above
                # make seperate function

        #conn = sqlite3.connect('saldb.sqlite')
        #cursor = conn.cursor()

        sqlGetAll = 'SELECT * FROM watchlist'



        #cursor.execute(sqlGetAll)

        res = cursor.execute(sqlGetAll)

        for row_num, row_data in enumerate(res):
            self.watchListTable.insertRow(row_num)
            for column_number, column_data in enumerate(row_data):
                item = str(column_data)
                if column_number == 0:
                    self.tableLabel = QLabel()
                    self.tableLabel.setScaledContents(True)
                    pixmap = QPixmap()
                    pixmap.loadFromData(column_data)
                    self.tableLabel.setPixmap(pixmap)

                    self.watchListTable.setCellWidget(row_num, column_number, self.tableLabel)
                else:
                    self.watchListTable.setItem(row_num, column_number, QTableWidgetItem(column_data))
            self.watchListTable.verticalHeader().setDefaultSectionSize(90)


        conn.close()

        #rows = cursor.fetchall()


        #for row in rows:
            #print('Rowww: ', row)


        #print('Number of Records :', len(rows))

        
        #self.watchListTable.setRowCount(len(rows))
        # self.watchListTable.setColumnCount(5)



        # tablerow = 0

        # for row in rows:

        #     self.watchListTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
        #     self.watchListTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
        #     self.watchListTable.setItem(tablerow, 2, QTableWidgetItem(row[2]))
        #     self.watchListTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
        #     self.watchListTable.setItem(tablerow, 4, QTableWidgetItem(row[4]))
        #     self.watchListTable.setItem(tablerow, 5, QTableWidgetItem(row[5]))

        #     tablerow += 1












