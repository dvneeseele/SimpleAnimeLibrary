#############################################################################
# dvneeseele
#############################################################################


from sal_ui import salUI
from jikan_dialog import jikanData
from jikan_lookup import Ui_dialog_lookup
from seriesDialog import seriesDlg
import os
import sys
import sqlite3
import requests
import pandas as pd
import json


from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QTextListFormat, QFont, QColor
from PyQt5.QtCore import QEvent, Qt, QSize, QDate, QTime, QByteArray, QBuffer, QIODevice
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QFormLayout, QLineEdit, QTabWidget, QWidget, QPushButton, QListWidgetItem, QLabel, QVBoxLayout, QGridLayout, QStackedWidget,
                            QColorDialog, QMessageBox, QFileDialog, QDialog, QFontDialog, QTableWidgetItem, QMenu, QComboBox, QGroupBox, QHBoxLayout, QFrame)






class seriesArtLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText("Drop Image")
        self.setScaledContents(True)

        self.setStyleSheet('''
            QLabel{
            border: 4px #aaa
            }
        ''')
        

        def setPixmap(self, image):
            super().setPixmap(image)















class SAL_app(salUI):
    def __init__(self):
        super().__init__()

        self.mainWindow = QMainWindow()
        self.mainWindow.setAcceptDrops(True)
        self.setupUI(self.mainWindow)

        # Menubar functions

        self.mb_newAction.triggered.connect(self.seriesDialog)

        # Toolbar functions

        self.addnewAction.triggered.connect(self.seriesDialog)
        self.editAction.triggered.connect(self.seriesEditDialog)
        self.deleteAction.triggered.connect(self.deleteSeries)
        self.infoAction.triggered.connect(self.applicationInfo)

        self.mainWindow.closeEvent = self.closeEvent

        # load function here
        self.dbLoad()








    # close event
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self.mainWindow, 'Exit App', "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:


            self.settings()

            event.accept()


            sys.exit()

        else:
            event.ignore()








    def getCurrentStack(self):
        pass





    def tableContextMenu(self, event):

        self.tableMenu = QMenu()

        # menu actions
        addSeries = self.tableMenu.addAction('Add New Series')
        editSeries = self.tableMenu.addAction('Edit This Entry')
        deleteSeries = self.tableMenu.addAction('Delete This Entry')

        # when stackwidget support is added this below would take the getCurrentStack function instead of just self.watchListTable
        tableAction = self.tableMenu.exec_(self.watchListTable.mapToGlobal(event))

        if tableAction == addSeries:
        # self.seriesLookup = Ui_dialog_lookup()
        # self.lookupDialog = QDialog()
        # self.seriesLookup.setupUi(self.lookupDialog)
        # self.lookupDialog.show()
            self.seriesInfo = seriesDlg()
            self.dlg = QDialog()
            self.seriesInfo.setupUi(self.dlg)
            self.dlg.show()
            #self.seriesDialog()
        if tableAction == editSeries:
            self.seriesEditDialog()
        if tableAction == deleteSeries:
            self.deleteSeries()
            







    def deleteSeries(self):

        currentRow = self.watchListTable.currentIndex().row()


        if currentRow >= 0:

            delSeries = self.watchListTable.item(currentRow, 1).text()            

            if delSeries != None:


                delete_msg = QMessageBox.question(self.mainWindow, 'Delete - Are you sure?', 'Are you sure you want to delete this entry? It cannot be undone!', QMessageBox.Ok | QMessageBox.Cancel)

                if delete_msg == QMessageBox.Ok:
                    conn = sqlite3.connect('saldb.sqlite')
                    cursor = conn.cursor()


                    cursor.execute("DELETE FROM watchlist WHERE Title = (?)", (delSeries,))
                    conn.commit()
                    conn.close()

                    # delete the row from the qtablewidget
                    self.watchListTable.removeRow(currentRow)






    def seriesEditDialog(self):

        curr_row = self.watchListTable.currentIndex().row()

        if curr_row >= 0:




    #############################################################################################################################################################################
    #############################################################################################################################################################################




            # this query is just to get the info to fill in the QDialog

            curr_row = self.watchListTable.currentIndex().row()

            # column 2 should have the Title of the series which is also the unique primary key for the db
            pk_id = self.watchListTable.item(curr_row, 1).text()


            conn = sqlite3.connect('saldb.sqlite')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            rowdata = cursor.execute("SELECT Art, Title, English_Title, Format, Start_Date, Completion_Date, Series_Type FROM watchlist WHERE Title = ?;", (pk_id,))

            
            for r in rowdata.fetchall():
                self.vals = dict(r)


            #THIS WORKS
            #print('ROWDATA', rowdata.fetchall()[0][0])

            conn.commit()

            conn.close()






    #############################################################################################################################################################################
    #############################################################################################################################################################################








            self.series_edit_dialog = QWidget()

            self.series_edit_dialog.setAcceptDrops(True)

            edit_dialog_layout = QGridLayout()




            # Labels
            self.artLabelEdit = QLabel()
            self.artLabelEdit.setScaledContents(True)
            self.pix = QPixmap()
            self.pix.loadFromData(self.vals['Art'])
            self.artLabelEdit.setPixmap(self.pix)
            #self.artLabel.setText("Drop Image")
            self.artLabelEdit.setAcceptDrops(True)
            self.artLabelEdit.setAlignment(Qt.AlignCenter)
            

            self.seriesTitleLabel = QLabel("Title :")
            self.seriesEnglishTitleLabel = QLabel("English Title :")
            self.seriesFormatLabel = QLabel("SUB/DUB :")
            self.startDateLabel = QLabel("Start Date :")
            self.completionDateLabel = QLabel("Completion Date :")
            self.seriesTypeLabel = QLabel("Series Type :")

            # LineEdits
            self.artLabel_le = QLineEdit()
            #self.artLabel_le.setPixmap(QPixmap(the blob data from the db. ))
            self.editSeriesTitle_le = QLineEdit()
            self.editSeriesTitle_le.setText(self.vals['Title'])
            self.editEnglishTitle_le = QLineEdit()
            self.editEnglishTitle_le.setText(self.vals['English_Title'])

            self.editFormat_cb = QComboBox()
            self.editFormat_cb.addItem("SUB")
            self.editFormat_cb.addItem("DUB")
            self.editFormat_cb.setCurrentText(self.vals['Format'])

            self.editStartDate_le = QLineEdit()
            self.editStartDate_le.setText(self.vals['Start_Date'])
            self.editCompletionDate_le = QLineEdit()
            self.editCompletionDate_le.setText(self.vals['Completion_Date'])
            self.editSeriesType_le = QLineEdit()
            self.editSeriesType_le.setText(self.vals['Series_Type'])

            # Buttons
            self.titleArtBtn = QPushButton("Fetch Series Title Art")
            self.titleArtBtn.clicked.connect(lambda: self.getSeriesArt(self.artLabelEdit, self.vals['Title']))
            self.submitEntryBtn = QPushButton("Submit")
            self.submitEntryBtn.clicked.connect(self.editEntrySubmit)
            self.chooseArtFile = QPushButton("Choose File")
            self.chooseArtFile.clicked.connect(lambda: self.insertArtFile(self.artLabelEdit))

            self.editStartDateBtn = QPushButton("Insert Current Date")# Will be replaced with an icon, no text, tooltip
            self.editStartDateBtn.clicked.connect(self.editStartDate)

            self.editEndDateBtn = QPushButton("Select Date")# Will be replaced with an icon, no text, tooltip
            self.editEndDateBtn.clicked.connect(self.selectEditEndDate)

            self.editFinishCurrentDateBtn = QPushButton("Insert Current Date")# Will be replaced with an icon, no text, tooltip
            self.editFinishCurrentDateBtn.clicked.connect(self.editFinishDate)

            self.editFinishSelectionDateBtn = QPushButton("Select Date")# Will be replaced with an icon, no text, tooltip
            self.editFinishSelectionDateBtn.clicked.connect(self.editFinishSelectionDate)


            # QFrames
            self.editButtonsFrame = QFrame()
            
            frameLayout = QHBoxLayout()
            self.editButtonsFrame.setLayout(frameLayout)

            frameLayout.addWidget(self.editStartDateBtn)
            frameLayout.addWidget(self.editEndDateBtn)




            self.editDateFinBtnsFrame = QFrame()
            finFrameLayout = QHBoxLayout()
            self.editDateFinBtnsFrame.setLayout(finFrameLayout)

            finFrameLayout.addWidget(self.editFinishCurrentDateBtn)
            finFrameLayout.addWidget(self.editFinishSelectionDateBtn)




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
            self.series_edit_dialog.setLayout(edit_dialog_layout)
            # column 1
            edit_dialog_layout.addWidget(self.artLabelEdit, 1, 1)
            edit_dialog_layout.addWidget(self.titleArtBtn, 2, 1)
            edit_dialog_layout.addWidget(self.chooseArtFile, 3, 1)
            edit_dialog_layout.addWidget(self.submitEntryBtn, 4, 1)
            # column 2
            edit_dialog_layout.addWidget(self.seriesTitleLabel, 1, 2)
            edit_dialog_layout.addWidget(self.seriesEnglishTitleLabel, 2, 2)
            edit_dialog_layout.addWidget(self.seriesFormatLabel, 3, 2)        
            edit_dialog_layout.addWidget(self.startDateLabel, 4, 2)
            edit_dialog_layout.addWidget(self.completionDateLabel, 6, 2)
            edit_dialog_layout.addWidget(self.seriesTypeLabel, 8, 2)
            # column 3
            edit_dialog_layout.addWidget(self.editSeriesTitle_le, 1, 3)
            edit_dialog_layout.addWidget(self.editEnglishTitle_le, 2, 3)
            edit_dialog_layout.addWidget(self.editFormat_cb, 3, 3)        
            edit_dialog_layout.addWidget(self.editStartDate_le, 4, 3) 
            edit_dialog_layout.addWidget(self.editButtonsFrame, 5, 3) #
            edit_dialog_layout.addWidget(self.editCompletionDate_le, 6, 3)
            edit_dialog_layout.addWidget(self.editDateFinBtnsFrame, 7, 3)
            edit_dialog_layout.addWidget(self.editSeriesType_le, 8, 3) #



            self.series_edit_dialog.show()






    def editStartDate(self):
        date = QDate.currentDate()
        self.editStartDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))


    def editFinishDate(self):
        date = QDate.currentDate()
        self.editCompletionDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))        


    def selectEditEndDate(self):
        pass

    def editFinishSelectionDate(self):
        pass







    def editEntrySubmit(self):



        if self.editSeriesTitle_le.text() != '':


    #########################################################################################################################################################
    #########################################################################################################################################################


            conn = sqlite3.connect('saldb.sqlite')
            cursor = conn.cursor()


            newart = self.artLabelEdit.pixmap()
            b_array = QByteArray()
            buffer = QBuffer(b_array)
            buffer.open(QIODevice.WriteOnly)
            newart.save(buffer, "JPG")
            blob = b_array.data()

            newValues = (self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text())

            #cursor.execute("INSERT OR REPLACE INTO watchlist(Title, English_Title, Format, Start_Date, Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?)", newValues)
            # cursor.execute("UPDATE watchlist SET Art = ?, Title = ?, English_Title = ?, Format = ?, Start_Date = ?, Completion_Date = ?, Series_Type = ? WHERE Title = ?", (self.vals['Art'] ,self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text(), self.vals['Title']))
            cursor.execute("UPDATE watchlist SET Art = ?, Title = ?, English_Title = ?, Format = ?, Start_Date = ?, Completion_Date = ?, Series_Type = ? WHERE Title = ?", (blob ,self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text(), self.vals['Title']))


            conn.commit()
            conn.close()





    #########################################################################################################################################################
    #########################################################################################################################################################



            newValues = [self.artLabelEdit ,self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text()]

            curr_row = self.watchListTable.currentIndex().row()

            new_ctr = 0

            for c in range(self.watchListTable.columnCount()):
                if c == 0:

                    self.watchListTable.setCellWidget(curr_row, c, newValues[c])

                else:

                    cell = self.watchListTable.item(curr_row, c).setText(newValues[new_ctr])

                new_ctr += 1

        else:
            title_msg = QMessageBox(self.mainWindow)
            title_msg.setText("Title field can not be blank")
            title_msg.setWindowTitle("Missing Entry Title")

            title_msg.show()



        self.series_edit_dialog.close()





    def seriesDialog(self):

        self.series_dialog = QWidget()
        self.series_dialog.setAcceptDrops(True)

        dialog_layout = QGridLayout()

        # Labels
        self.artLabel = seriesArtLabel()
        #self.artLabel = QLabel()
        #self.artLabel.setText("Drop Image")
        #self.artLabel.setAcceptDrops(True)
        #self.artLabel.setAlignment(Qt.AlignCenter)
        

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



        self.startDate_le = QLineEdit()
        self.completionDate_le = QLineEdit()
        self.seriesType_le = QLineEdit()


        # Combobox
        self.seriesFormat_cb = QComboBox()
        self.seriesFormat_cb.addItem("SUB")
        self.seriesFormat_cb.addItem("DUB")


        # Buttons
        self.titleArtBtn = QPushButton("Fetch Series Title Art")
        #self.titleArtBtn.clicked.connect(lambda: self.getSeriesArt(self.artLabel, self.seriesTitle_le.text()))
        self.titleArtBtn.clicked.connect(lambda: self.seriesFetchAll)

        self.addArtFile = QPushButton("Choose Art File")
        self.addArtFile.clicked.connect(lambda: self.insertArtFile(self.artLabel))

        self.submitEntryBtn = QPushButton("Submit")
        self.submitEntryBtn.clicked.connect(self.entrySubmit)

        self.fetchAllInfoBtn = QPushButton("Fetch all Series Info")
        self.fetchAllInfoBtn.clicked.connect(self.seriesFetchAll)

        self.currentStartDateBtn = QPushButton("Insert Current Date") # Will be replaced with an icon, no text, tooltip
        self.currentStartDateBtn.clicked.connect(self.insertStartCurrentDate)

        self.startDateSelectionBtn = QPushButton("Select Date") # Will be replaced with an icon , no text, tooltip
        self.startDateSelectionBtn.clicked.connect(self.insertStartDateSelection)

        self.finishCurrentDateBtn = QPushButton("Insert Current Date") # Will be replaced with an icon, no text, tooltip
        self.finishCurrentDateBtn.clicked.connect(self.finishCurrentDate)

        self.finishDateSelectionBtn = QPushButton("Select Date") # Will be replaced with an icon , no text, tooltip
        self.finishDateSelectionBtn.clicked.connect(self.finishDateSelection)        




        # QFrames
        self.formButtonsFrame = QFrame()
        
        frameLayout = QHBoxLayout()
        self.formButtonsFrame.setLayout(frameLayout)

        frameLayout.addWidget(self.currentStartDateBtn)
        frameLayout.addWidget(self.startDateSelectionBtn)



        self.dateFinBtnsFrame = QFrame()
        finFrameLayout = QHBoxLayout()
        self.dateFinBtnsFrame.setLayout(finFrameLayout)

        finFrameLayout.addWidget(self.finishCurrentDateBtn)
        finFrameLayout.addWidget(self.finishDateSelectionBtn)



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
                self.set_image(img_fp)
                

                event.accept()
            else:
                event.ignore()
                print('drop event ignored')


        def setImage(self, file_path):
            self.artLabel.setPixmap(QPixmap(file_path))



        

        # Set Dialog Layout
        self.series_dialog.setLayout(dialog_layout)
        # column 1
        dialog_layout.addWidget(self.artLabel, 1, 1)
        dialog_layout.addWidget(self.titleArtBtn, 2, 1)
        dialog_layout.addWidget(self.fetchAllInfoBtn, 3, 1)
        dialog_layout.addWidget(self.addArtFile, 4, 1)
        dialog_layout.addWidget(self.submitEntryBtn, 5, 1)
        # column 2
        dialog_layout.addWidget(self.seriesTitleLabel, 1, 2)
        dialog_layout.addWidget(self.seriesEnglishTitleLabel, 2, 2)
        dialog_layout.addWidget(self.seriesFormatLabel, 3, 2)        
        dialog_layout.addWidget(self.startDateLabel, 4, 2)
        dialog_layout.addWidget(self.completionDateLabel, 6, 2)
        dialog_layout.addWidget(self.seriesTypeLabel, 8, 2)
        # column 3
        dialog_layout.addWidget(self.seriesTitle_le, 1, 3)
        dialog_layout.addWidget(self.seriesEnglishTitle_le, 2, 3)
        #dialog_layout.addWidget(self.seriesFormat_le, 3, 3)
        dialog_layout.addWidget(self.seriesFormat_cb, 3, 3)        
        dialog_layout.addWidget(self.startDate_le, 4, 3)
        dialog_layout.addWidget(self.formButtonsFrame, 5, 3) #QGroupBox
        dialog_layout.addWidget(self.completionDate_le, 6, 3)
        dialog_layout.addWidget(self.dateFinBtnsFrame, 7, 3) #QGroupBox

        dialog_layout.addWidget(self.seriesType_le, 8, 3)


        self.series_dialog.show()








    def insertArtFile(self, lbl):
        artfn = QFileDialog.getOpenFileName(self.mainWindow, 'Choose Title Art', "." , "Images (*.png *.jpg *.bmp)")

        filename = str(artfn[0])

        chosenart = lbl.setPixmap(QPixmap(filename))

        return chosenart







    def getSeriesArt(self, lbl, txt):

        self.imgBytes = jikanData(txt, lbl)
        self.imgBytes.show()




    def insertStartCurrentDate(self):
        date = QDate.currentDate()
        self.startDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))

    def insertStartDateSelection(self):
        # QCalendarWidget for selection
        pass

    def finishCurrentDate(self):
        date = QDate.currentDate()
        self.completionDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))

    def finishDateSelection(self):
        # QCalendarWidget for selection
        pass





    def applicationInfo(self):
        pass




    def seriesFetchAll(self):
        print('called')
        self.seriesLookup = Ui_dialog_lookup()
        self.lookupDialog = QDialog()
        self.seriesLookup.setupUi(self.lookupDialog)
        self.lookupDialog.show()












    def entrySubmit(self):

        if self.seriesTitle_le.text() != '':

                



            # get lineedit texts
            # get the art image
            self.title = self.seriesTitle_le.text()
            self.englishtitle = self.seriesEnglishTitle_le.text()


            self.language = self.seriesFormat_cb.currentText()

            self.start = self.startDate_le.text()
            self.fin = self.completionDate_le.text()
            self.type = self.seriesType_le.text()

            # execute sql insert

            conn = sqlite3.connect('saldb.sqlite')  

            cursor = conn.cursor()



            if self.artLabel.pixmap() != None:

                pix = self.artLabel.pixmap()
                b_array = QByteArray()
                buffer = QBuffer(b_array)
                buffer.open(QIODevice.WriteOnly)
                pix.save(buffer, "JPG")
                blob = b_array.data()


            else:

                with open('icons/saldb_darkred.png', 'rb') as file:
                    blob = file.read()
                file.close()

            
            
            info_tuple = (blob, self.title, self.englishtitle, self.language, self.start, self.fin, self.type)


            cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?, ?)", info_tuple)

            conn.commit()

            conn.close()



            rows = self.watchListTable.rowCount()
            self.watchListTable.setRowCount(rows + 1)

            col = 0


            for item in range(len(info_tuple)):
                if col == 0:
                    label = QLabel()
                    label.setScaledContents(True)
                    pixmap = QPixmap()
                    pixmap.loadFromData(info_tuple[item])
                    #pixmap.scaled(50, 3000, Qt.IgnoreAspectRatio, Qt.FastTransformation)
                    label.setPixmap(pixmap.scaled(75, 100, Qt.KeepAspectRatio, Qt.FastTransformation))
                    self.watchListTable.setCellWidget(self.watchListTable.rowCount()-1, col, label)
                else:
                    self.watchListTable.setItem(self.watchListTable.rowCount()-1, col, QTableWidgetItem(info_tuple[item]))
                col += 1

            self.series_dialog.close()


        else:
            msg_nullTitle = QMessageBox(self.mainWindow)
            msg_nullTitle.setText("Title can not be blank")
            msg_nullTitle.setWindowTitle("Missing Entry Title")

            msg_nullTitle.show()






    # TODO : Need to use this function below to use the jikan_dialog.py and its class to go fetch other info to fill in. 
    # such as genere, air dates, characters, etc.
    # at some point i will probably add the option to have a full page info view panel for each entry, setup kind of like mal or anidb.

    def fetchInfo(self, fetchtitle):

        self.jd = jikanData(fetchtitle)
        self.jd.show()

        #jikanData.search(fetchtitle)

        #return self.jd







    def settings(self):

        if not os.path.exists("settings"):
            os.mkdir("settings")




        # main window
        mwh = self.mainWindow.height()
        mww = self.mainWindow.width()
        mwx = self.mainWindow.x()
        mwy = self.mainWindow.y()

        # splitter size

        stack_w = self.tableStack.width()
        listw = self.sidebar.width()



        # settings dict
        sal_settings = {
            'mainwindow_height' : mwh,
            'mainwindow_width' : mww,
            'mainwindow_x' : mwx,
            'mainwindow_y' : mwy,
            'stack_width' : stack_w,
            'list_width' : listw

        }


        with open('settings/salsettings.json', 'w') as shit:
            json.dump(sal_settings , shit, indent=4)
        shit.close()











    def newDB(self):
        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()

        createTable = "CREATE TABLE IF NOT EXISTS watchlist(Art BLOB, Title TEXT PRIMARY KEY, English_Title TEXT, Format TEXT, Start_Date TEXT ,Completion_Date TEXT, Series_Type TEXT)"

        cursor.execute(createTable)








    def dbLoad(self):
        
        # pandas vs just for loop over db??

        if os.path.exists('saldb.sqlite'):
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


        sqlGetAll = 'SELECT * FROM watchlist'




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
                    self.tableLabel.setPixmap(pixmap.scaled(85, 110, Qt.IgnoreAspectRatio, Qt.FastTransformation))

                    self.watchListTable.setCellWidget(row_num, column_number, self.tableLabel)
                else:
                    self.watchListTable.setItem(row_num, column_number, QTableWidgetItem(column_data))
            self.watchListTable.verticalHeader().setDefaultSectionSize(140)
            self.watchListTable.horizontalHeader().setDefaultSectionSize(120)


        conn.close()




        if os.path.isfile('settings\salsettings.json'):

            with open('settings\salsettings.json') as fyle:
                data = json.load(fyle)
            

            self.mainWindow.setGeometry(data['mainwindow_x'], data['mainwindow_y'], data['mainwindow_width'], data['mainwindow_height'])

            self.splitter.setSizes([data['list_width'], data['stack_width']])

