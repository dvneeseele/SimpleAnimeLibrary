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

        createTable = "CREATE TABLE IF NOT EXISTS watchlist(Title TEXT PRIMARY KEY, English_Title TEXT, Format TEXT, Completion_Date TEXT, Series_Type TEXT)"

        cursor.execute(createTable)

        # for testing
        cursor.execute("INSERT INTO watchlist (Title, English_Title, Format, Completion_Date, Series_Type) VALUES ('ani', 'Anime', 'SUB', '12/01/2021', 'ORI')")

        cursor.execute("INSERT INTO watchlist (Title, English_Title, Format, Completion_Date, Series_Type) VALUES ('qwer', 'Anime22', 'DUB', '120/90/2021', 'SQ')")

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


                # need to make new tables to put into database above
                # make seperate function

        #conn = sqlite3.connect('saldb.sqlite')
        #cursor = conn.cursor()

        sqlGetAll = 'SELECT * FROM watchlist'



        cursor.execute(sqlGetAll)

        rows = cursor.fetchall()


        for row in rows:
            print('Rowww: ', row)

        rownum = len(cursor.fetchall())

        print('Number of Records :', len(rows))

        
        #self.watchListTable.setRowCount(len(result.fetchall()))


        tablerow = 0

        for row in rows:

            self.watchListTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.watchListTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.watchListTable.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.watchListTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.watchListTable.setItem(tablerow, 4, QTableWidgetItem(row[4]))

            tablerow += 1


        conn.close()









