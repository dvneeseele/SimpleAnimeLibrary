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
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit, QTabWidget, QWidget, QPushButton, QListWidgetItem, QLabel, QVBoxLayout, QGridLayout, QStackedWidget,
                            QColorDialog, QMessageBox, QFileDialog, QDialog, QFontDialog, QTableWidgetItem)



class SAL_app(salUI):
    def __init__(self):
        super().__init__()

        self.mainWindow = QMainWindow()
        self.mainWindow.setAcceptDrops(True)
        self.setupUI(self.mainWindow)

        # Menubar functions

        self.mb_newAction.triggered.connect(self.seriesDialog)

        # Toolbar functions

        # TODO

        # load function here
        self.dbLoad()






    def getCurrentStack(self):
        pass




    def seriesDialog(self):

        self.series_dialog = QWidget()
        self.series_dialog.setAcceptDrops(True)

        dialog_layout = QGridLayout()

        # Labels
        self.artLabel = QLabel()
        #self.artLabel.setText("Drop Image")
        self.artLabel.setAcceptDrops(True)
        self.artLabel.setAlignment(Qt.AlignCenter)
        

        self.seriesTitleLabel = QLabel("Title :")
        self.seriesEnglishTitleLabel = QLabel("English Title :")
        self.seriesFormatLabel = QLabel("SUB/DUB :")
        self.startDateLabel = QLabel("Start Date :")
        self.completionDateLabel = QLabel("Completion Date :")
        self.seriesTypeLabel = QLabel("Series Type :")

        # LineEdits
        self.artLabel_le = QLineEdit()
        self.seriesTitle_le = QLineEdit()
        self.seriesEnglishTitle_le = QLineEdit()
        self.seriesFormat_le = QLineEdit()
        self.startDate_le = QLineEdit()
        self.completionDate_le = QLineEdit()
        self.seriesType_le = QLineEdit()

        # Buttons
        self.titleArtBtn = QPushButton("Fetch Series Title Art")
        self.titleArtBtn.clicked.connect(self.getSeriesArt)
        self.submitEntryBtn = QPushButton("Submit")
        self.submitEntryBtn.clicked.connect(self.entrySubmit)

        # drag event sequence functions

        def dragEnterEvent(self, event):
            if event.mimeData().hasImage:
                event.accept()
            else:
                event.ignore()
                print('event ignored')

        def dragMoveEvent(self, event):
            if event.mimeData().hasImage:
                event.accept()
            else:
                event.ignore()
                print('event ignored')      

        def dropEvent(self, event):
            if event.mimeData().hasImage:
                event.setDropAction(Qt.CopyAction)
                img_fp = event.mimeData().urls()[0].toLocalFile()
                print(img_fp)
                self.artLabel.setPixmap(QPixmap(img_fp))
                

                event.accept()
            else:
                event.ignore()
                print('drop event ignored')




        

        # Set Dialog Layout
        self.series_dialog.setLayout(dialog_layout)
        # column 1
        dialog_layout.addWidget(self.artLabel, 1, 1)
        dialog_layout.addWidget(self.titleArtBtn, 2, 1)
        dialog_layout.addWidget(self.submitEntryBtn, 3, 1)
        # column 2
        dialog_layout.addWidget(self.seriesTitleLabel, 1, 2)
        dialog_layout.addWidget(self.seriesEnglishTitleLabel, 2, 2)
        dialog_layout.addWidget(self.seriesFormatLabel, 3, 2)        
        dialog_layout.addWidget(self.startDateLabel, 4, 2)
        dialog_layout.addWidget(self.completionDateLabel, 5, 2)
        dialog_layout.addWidget(self.seriesTypeLabel, 6, 2)
        # column 3
        dialog_layout.addWidget(self.seriesTitle_le, 1, 3)
        dialog_layout.addWidget(self.seriesEnglishTitle_le, 2, 3)
        dialog_layout.addWidget(self.seriesFormat_le, 3, 3)        
        dialog_layout.addWidget(self.startDate_le, 4, 3)
        dialog_layout.addWidget(self.completionDate_le, 5, 3)
        dialog_layout.addWidget(self.seriesType_le, 6, 3)


        self.series_dialog.show()


    # dialog button functions
    def getSeriesArt(self):
        pass


    def entrySubmit(self):
        # get lineedit texts
        # get the art image
        self.title = self.seriesTitle_le.text()
        self.englishtitle = self.seriesEnglishTitle_le.text()
        self.language = self.seriesFormat_le.text()
        self.start = self.startDate_le.text()
        self.fin = self.completionDate_le.text()
        self.type = self.seriesType_le.text()

        # execute sql insert

        conn = sqlite3.connect('saldb.sqlite')  

        cursor = conn.cursor()

        # TODO implement art as well
        # for testing
        with open("naruto.jpg", 'rb') as file:
            blob = file.read()

        
        info_tuple = (blob, self.title, self.englishtitle, self.language, self.start, self.fin, self.type)


        cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?, ?)", info_tuple)

        conn.commit()

        conn.close()

        # add to tablewidget
        #self.watchListTable.setItem(row_num, column_number, QTableWidgetItem(column_data))

        # self.watchListTable.insertRow(self.watchListTable.rowCount())
        # print('row count :', self.watchListTable.rowCount())

        #self.watchListTable.setItem(self.watchListTable.rowCount()-1,)

        # for x in range(self.watchListTable.columnCount()):
        #     for y in range(len(info_tuple)):
        #         if y == 0:
        #             self.tableLabel = QLabel()
        #             self.tableLabel.setScaledContents(True)
        #             pixmap = QPixmap()
        #             pixmap.loadFromData(info_tuple[y])
        #             self.tableLabel.setPixmap(pixmap)
        #         else:
        #             self.watchListTable.setItem(self.watchListTable.rowCount()-1, x, QTableWidgetItem(info_tuple[y]))


        rows = self.watchListTable.rowCount()
        self.watchListTable.setRowCount(rows + 1)

        col = 0


        for item in range(len(info_tuple)):
            if col == 0:
                label = QLabel()
                label.setScaledContents(True)
                pixmap = QPixmap()
                pixmap.loadFromData(info_tuple[item])
                label.setPixmap(pixmap)
                #cell = QTableWidgetItem(label)
                self.watchListTable.setCellWidget(self.watchListTable.rowCount()-1, col, label)
            else:
                self.watchListTable.setItem(self.watchListTable.rowCount()-1, col, QTableWidgetItem(info_tuple[item]))
            col += 1




                    # self.tableLabel = QLabel()
                    # self.tableLabel.setScaledContents(True)
                    # pixmap = QPixmap()
                    # pixmap.loadFromData(column_data)
                    # self.tableLabel.setPixmap(pixmap)
                    # self.watchListTable.setCellWidget(row_num, column_number, self.tableLabel)







    def newDB(self):
        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()

        createTable = "CREATE TABLE IF NOT EXISTS watchlist(Art BLOB, Title TEXT PRIMARY KEY, English_Title TEXT, Format TEXT, Start_Date TEXT ,Completion_Date TEXT, Series_Type TEXT)"

        cursor.execute(createTable)

        # for testing
        with open("naruto.jpg", 'rb') as file:
            blob = file.read()

        entry_tuple = (blob, 'ani', 'Anime', 'SUB', '9/05/20', '12/01/2021', 'ORI')

        # for testing
        # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Completion_Date, Series_Type) VALUES ({}, 'ani', 'Anime', 'SUB', '12/01/2021', 'ORI')".format(blob))

        # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Completion_Date, Series_Type) VALUES ({}, 'qwer', 'Anime22', 'DUB', '120/90/2021', 'SQ')".format(blob))

        cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?, ?)", entry_tuple)

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












