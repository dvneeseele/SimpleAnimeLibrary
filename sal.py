#############################################################################
# me
#############################################################################


from sal_ui import salUI
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
            self.seriesDialog()
        if tableAction == editSeries:
            self.seriesEditDialog()
        if tableAction == deleteSeries:
            self.deleteSeries()
            







    def deleteSeries(self):

        currentRow = self.watchListTable.currentIndex().row()


        if currentRow > 0:

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

        # get table row data and fill the seriesEditDialog QLineEdits with the content
        # then find a way to lookup the corresponding row in sqlite db

#############################################################################################################################################################################
#############################################################################################################################################################################




        # curr_row = self.watchListTable.currentIndex().row()
        # print('Current Row :', curr_row)

        # self.edit_row_data = []

        

        # for i in range(self.watchListTable.columnCount()):
        #     if i == 0:
        #         # get the widget QLabel with pixmap in it.
        #         # set it to self.artLabel

        #         # get primary key (Title) from the QTableWidget then use it to lookup all the data in that row including blob data
        #         self.artLabelEdit = self.watchListTable.cellWidget(curr_row, i)


        #         # maybe add this to the self.edit_row_data list
        #         #continue
        #     else:
        #         cell = self.watchListTable.item(curr_row, i).text() # i think it is reading the blob data in the first cell of the row...
        #         self.edit_row_data.append(cell)
        
        # print('Cell Data :', self.edit_row_data)





#############################################################################################################################################################################
#############################################################################################################################################################################




        # this query is just to get the info to fill in the QDialog

        curr_row = self.watchListTable.currentIndex().row()

        # column 2 should have the Title of the series which is also the unique primary key for the db
        pk_id = self.watchListTable.item(curr_row, 1).text()

        # print("curr_row", curr_row)
        # print('PK_ID' ,pk_id)

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
        #self.editStartDate_le.clear()
        self.editStartDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))


    def editFinishDate(self):
        date = QDate.currentDate()
        self.editCompletionDate_le.setText(date.toString(Qt.DefaultLocaleShortDate))        


    def selectEditEndDate(self):
        pass

    def editFinishSelectionDate(self):
        pass







    def editEntrySubmit(self):
        # if series title == None or blank '' string:
            # qmessagebox must have a title field is required

        #print(self.edit_row_data)






        # sql = [('Title' ,self.editSeriesTitle_le.text(), 'Title', self.edit_row_data[0]), ('English_Title', self.editEnglishTitle_le.text(), 'English_Title', self.edit_row_data[1]),
        #         ('Format', self.editFormat_le.text(), 'Format', self.edit_row_data[2]), ('Start_Date', self.editStartDate_le.text(), 'Start_Date', self.edit_row_data[3]), 
        #         ('Completion_Date', self.editCompletionDate_le.text(), 'Completion_Date', self.edit_row_data[4]), ('Series_Type', self.editSeriesType_le.text(), 'Series_Type', self.edit_row_data[5])]


        # # sql = [['Title' ,self.editSeriesTitle_le.text()], ['Title', self.edit_row_data[0]], ['English_Title', self.editEnglishTitle_le.text()], ['English_Title', self.edit_row_data[1]],
        # # ['Format', self.editFormat_le.text()], ['Format', self.edit_row_data[2]], ['Start_Date', self.editStartDate_le.text()], ['Start_Date', self.edit_row_data[3]], 
        # # ['Completion_Date', self.editCompletionDate_le.text()], ['Completion_Date', self.edit_row_data[4]], ['Series_Type', self.editSeriesType_le.text()], ['Series_Type', self.edit_row_data[5]]]

        # conn = sqlite3.connect('saldb.sqlite')
        # cursor = conn.cursor()

        # for u in range(len(sql)):
        #     #print('this here', sql[u])
        #     # unpack the tuple\
        #     h, i, j, k = sql[u]
        #     tuppie = tuple(sql[u])
        #     print('tuppie :',tuppie)
        #     #fuck = "UPDATE watchlist SET '{}' = '{}' WHERE '{}' = '{}'".format(h, i, j, k)
        #     cursor.execute('''UPDATE watchlist SET ? = ? WHERE ? = ?''', (h, i, h, k))
        #     #cursor.execute('''UPDATE watchlist SET ? = ?''', (h, i,))
        #     #print(fuck)
        #     #cursor.execute(fuck)        
        #     conn.commit()

        # conn.close()









        if self.editSeriesTitle_le.text() != '':








    #########################################################################################################################################################
    #########################################################################################################################################################


            conn = sqlite3.connect('saldb.sqlite')
            cursor = conn.cursor()

            newValues = (self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text())

            #cursor.execute("INSERT OR REPLACE INTO watchlist(Title, English_Title, Format, Start_Date, Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?)", newValues)
            cursor.execute("UPDATE watchlist SET Art = ?, Title = ?, English_Title = ?, Format = ?, Start_Date = ?, Completion_Date = ?, Series_Type = ? WHERE Title = ?", (self.vals['Art'] ,self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text(), self.vals['Title']))

            conn.commit()
            conn.close()





    #########################################################################################################################################################
    #########################################################################################################################################################




            #newValues = [self.artLabelEdit ,self.seriesTitle_le.text(), self.seriesEnglishTitle_le.text(), self.seriesFormat_le.text(), self.startDate_le.text(), self.completionDate_le.text(), self.seriesType_le.text()]


            #newValues = [self.artLabelEdit ,self.edit_row_data[0], self.edit_row_data[1], self.edit_row_data[2], self.edit_row_data[3], self.edit_row_data[4], self.edit_row_data[5]]
            newValues = [self.artLabelEdit ,self.editSeriesTitle_le.text(), self.editEnglishTitle_le.text(), self.editFormat_cb.currentText(), self.editStartDate_le.text(), self.editCompletionDate_le.text(), self.editSeriesType_le.text()]
            #print('New VAlues :', newValues)

            curr_row = self.watchListTable.currentIndex().row()

            new_ctr = 0

            for c in range(self.watchListTable.columnCount()):
                if c == 0:
                    # self.watchListTable.item(curr_row, c).setCellWidget() to qlabel
                    #self.watchListTable.item(curr_row, c).setCellWidget(newValues[c])

                    # self.watchListTable.setCellWidget(curr_row, c, newValues[c])
                    self.watchListTable.setCellWidget(curr_row, c, newValues[c])
                    #continue
                else:
                    #cell = self.watchListTable.setItem(curr_row, c, QTableWidgetItem(self.seriesTitle_le.text()))
                    cell = self.watchListTable.item(curr_row, c).setText(newValues[new_ctr])

                new_ctr += 1

        else:
            title_msg = QMessageBox(self.mainWindow)
            title_msg.setText("Title field can not be blank")
            title_msg.setWindowTitle("Missing Entry Title")

            title_msg.show()







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



        #self.seriesFormat_le = QLineEdit()
        self.startDate_le = QLineEdit()
        self.completionDate_le = QLineEdit()
        self.seriesType_le = QLineEdit()


        # Combobox
        self.seriesFormat_cb = QComboBox()
        self.seriesFormat_cb.addItem("SUB")
        self.seriesFormat_cb.addItem("DUB")


        # Buttons
        self.titleArtBtn = QPushButton("Fetch Series Title Art")
        self.titleArtBtn.clicked.connect(lambda: self.getSeriesArt(self.artLabel, self.seriesTitle_le.text()))

        self.submitEntryBtn = QPushButton("Submit")
        self.submitEntryBtn.clicked.connect(self.entrySubmit)

        self.currentStartDateBtn = QPushButton("Insert Current Date") # Will be replaced with an icon, no text, tooltip
        self.currentStartDateBtn.clicked.connect(self.insertStartCurrentDate)

        self.startDateSelectionBtn = QPushButton("Select Date") # Will be replaced with an icon , no text, tooltip
        self.startDateSelectionBtn.clicked.connect(self.insertStartDateSelection)

        self.finishCurrentDateBtn = QPushButton("Insert Current Date") # Will be replaced with an icon, no text, tooltip
        self.finishCurrentDateBtn.clicked.connect(self.finishCurrentDate)

        self.finishDateSelectionBtn = QPushButton("Select Date") # Will be replaced with an icon , no text, tooltip
        self.finishDateSelectionBtn.clicked.connect(self.finishDateSelection)        



        # GroupBox
        # self.formButtonsGroupBox = QGroupBox()


        # groupbox_layout = QHBoxLayout()
        # self.formButtonsGroupBox.setLayout(groupbox_layout)

        # groupbox_layout.addWidget(self.currentStartDateBtn)
        # groupbox_layout.addWidget(self.startDateSelectionBtn)


        # self.formButtonsCompletion = QGroupBox()
        # self.formButtonsCompletion.setStyleSheet("border:none")

        # completeButtons_layout = QHBoxLayout()
        # self.formButtonsCompletion.setLayout(completeButtons_layout)

        # completeButtons_layout.addWidget(self.finishCurrentDateBtn)
        # completeButtons_layout.addWidget(self.finishDateSelectionBtn)


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
                #self.artLabel.setPixmap(QPixmap(img_fp))
                #self.artLabel.setPixmap(QPixmap(img_fp))
                

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
        dialog_layout.addWidget(self.submitEntryBtn, 3, 1)
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

        print(filename)

        lbl.setPixmap(QPixmap(filename))







    # either make another getArt() function
    # or pass in the QLabel that the pixmap in the function below can be set to.




    # dialog button functions
    # def getSeriesArt(self):
        
    #     self.imgBytes = self.fetchInfo(self.seriesTitle_le.text())

    #     self.imgPixmap = QPixmap()
    #     self.imgPixmap.loadFromData(self.imgBytes)

    #     # set the existing art qlabel in the add series dialog
    #     self.artLabel.setPixmap(self.imgPixmap)





    def getSeriesArt(self, lbl, txt):
        #self.imgBytes = self.fetchInfo(self.seriesTitle_le.text())
        self.imgBytes = self.fetchInfo(txt)

        titleart = QPixmap()
        titleart.loadFromData(self.imgBytes)

        lbl.setPixmap(QPixmap(titleart))



















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

















    def entrySubmit(self):

        # validate Title lineedit and Art label

        # for artLabel -- If I implement a default icon then dont have to check if it is None. It will always be a default icon if no art is added.

        if self.seriesTitle_le.text() != '' and self.artLabel.pixmap() != None:
                



            # get lineedit texts
            # get the art image
            self.title = self.seriesTitle_le.text()
            self.englishtitle = self.seriesEnglishTitle_le.text()

            #self.language = self.seriesFormat_le.text()
            self.language = self.seriesFormat_cb.currentText()

            self.start = self.startDate_le.text()
            self.fin = self.completionDate_le.text()
            self.type = self.seriesType_le.text()

            # execute sql insert

            conn = sqlite3.connect('saldb.sqlite')  

            cursor = conn.cursor()

            # TODO implement art as well
            # for testing
            # with open("naruto.jpg", 'rb') as file:
            #     blob = file.read()

            # if qlabel has a pixmap => convert to blob
            # if not then maybe load default icon

            pix = self.artLabel.pixmap()
            b_array = QByteArray()
            buffer = QBuffer(b_array)
            buffer.open(QIODevice.WriteOnly)
            pix.save(buffer, "JPG")
            blob = b_array.data()
            print(blob)
            
            
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

            self.seriesDialog.close()



                        # self.tableLabel = QLabel()
                        # self.tableLabel.setScaledContents(True)
                        # pixmap = QPixmap()
                        # pixmap.loadFromData(column_data)
                        # self.tableLabel.setPixmap(pixmap)
                        # self.watchListTable.setCellWidget(row_num, column_number, self.tableLabel)

        else:
            msg_nullTitle = QMessageBox(self.mainWindow)
            msg_nullTitle.setText("Title can not be blank")
            msg_nullTitle.setWindowTitle("Missing Entry Title")

            msg_nullTitle.show()





    def fetchInfo(self, fetchtitle):

        # format url api string with the title?
        api_base = 'https://api.jikan.moe/v3'
        url = api_base + '/search/anime?q={}&page=1'.format(fetchtitle)

        # get title of series
        # when in the addSeries Dialog => if self.seriesTitle_le == '' or None => then qmessagebox "Must have a Title"


        req = requests.get(url)

        resp = req.json()

        seriesImage = resp['results'][0]['image_url']

        getImage = requests.get(seriesImage).content

        # should return image in bytes
        # .content method give image in bytes so should be able to insert it directly into sqlite db
        # imageContent = requests.get(seriesImage.content)

        return getImage







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


        #cfg = json.loads("/settings/salsettings.json")






















    def newDB(self):
        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()

        createTable = "CREATE TABLE IF NOT EXISTS watchlist(Art BLOB, Title TEXT PRIMARY KEY, English_Title TEXT, Format TEXT, Start_Date TEXT ,Completion_Date TEXT, Series_Type TEXT)"

        cursor.execute(createTable)


        # # for testing
        with open("naruto.jpg", 'rb') as file:
            blob = file.read()

        # maybe insert a default series art/icon here as the blob data
        



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
                    #self.tableLabel.resize(300, 500)
                    pixmap = QPixmap()
                    pixmap.loadFromData(column_data)
                    self.tableLabel.setPixmap(pixmap)

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












