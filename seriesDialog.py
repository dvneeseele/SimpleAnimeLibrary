# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerEkHqpR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore
from jikan_lookup import Ui_dialog_lookup
from dbHandler import dbInfo
import sqlite3
import json

class seriesDlg(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1582, 899)
        self.seriesLookup = Ui_dialog_lookup()
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.leftFrame = QFrame(Dialog)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.leftFrame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.seriesArtLabel = QLabel(self.leftFrame)
        self.seriesArtLabel.setObjectName(u"seriesArtLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.seriesArtLabel)

        self.seriesLookupBtn = QPushButton(self.leftFrame)
        self.seriesLookupBtn.setObjectName(u"seriesLookupBtn")
        self.seriesLookupBtn.clicked.connect(self.fetchInfo)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.seriesLookupBtn)

        self.chooseArtBtn = QPushButton(self.leftFrame)
        self.chooseArtBtn.setObjectName(u"chooseArtBtn")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.chooseArtBtn)


        self.gridLayout_2.addWidget(self.leftFrame, 0, 0, 1, 1)

        self.rightFrame = QFrame(Dialog)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.rightFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.seriesLicensorsLabel = QLabel(self.rightFrame)
        self.seriesLicensorsLabel.setObjectName(u"seriesLicensorsLabel")

        self.gridLayout.addWidget(self.seriesLicensorsLabel, 10, 0, 1, 1)

        self.seriesSynopsisLabel = QLabel(self.rightFrame)
        self.seriesSynopsisLabel.setObjectName(u"seriesSynopsisLabel")

        self.gridLayout.addWidget(self.seriesSynopsisLabel, 15, 0, 1, 1)

        self.seriesEnglishTitleLe = QLineEdit(self.rightFrame)
        self.seriesEnglishTitleLe.setObjectName(u"seriesEnglishTitleLe")

        self.gridLayout.addWidget(self.seriesEnglishTitleLe, 1, 1, 1, 1)

        self.seriesStartDateLe = QLineEdit(self.rightFrame)
        self.seriesStartDateLe.setObjectName(u"seriesStartDateLe")

        self.gridLayout.addWidget(self.seriesStartDateLe, 3, 1, 1, 1)

        self.englishTitleLabel = QLabel(self.rightFrame)
        self.englishTitleLabel.setObjectName(u"englishTitleLabel")

        self.gridLayout.addWidget(self.englishTitleLabel, 1, 0, 1, 1)

        self.seriesEpisodesLe = QLineEdit(self.rightFrame)
        self.seriesEpisodesLe.setObjectName(u"seriesEpisodesLe")

        self.gridLayout.addWidget(self.seriesEpisodesLe, 6, 1, 1, 1)

        self.seriesStatusLabel = QLabel(self.rightFrame)
        self.seriesStatusLabel.setObjectName(u"seriesStatusLabel")

        self.gridLayout.addWidget(self.seriesStatusLabel, 7, 0, 1, 1)

        self.seriesGenresLabel = QLabel(self.rightFrame)
        self.seriesGenresLabel.setObjectName(u"seriesGenresLabel")

        self.gridLayout.addWidget(self.seriesGenresLabel, 12, 0, 1, 1)

        self.seriesYearLabel = QLabel(self.rightFrame)
        self.seriesYearLabel.setObjectName(u"seriesYearLabel")

        self.gridLayout.addWidget(self.seriesYearLabel, 17, 0, 1, 1)

        self.seriesThemesLabel = QLabel(self.rightFrame)
        self.seriesThemesLabel.setObjectName(u"seriesThemesLabel")

        self.gridLayout.addWidget(self.seriesThemesLabel, 13, 0, 1, 1)

        self.seriesEpisodesLabel = QLabel(self.rightFrame)
        self.seriesEpisodesLabel.setObjectName(u"seriesEpisodesLabel")

        self.gridLayout.addWidget(self.seriesEpisodesLabel, 6, 0, 1, 1)

        self.seriesTypeLabel = QLabel(self.rightFrame)
        self.seriesTypeLabel.setObjectName(u"seriesTypeLabel")

        self.gridLayout.addWidget(self.seriesTypeLabel, 5, 0, 1, 1)

        self.seriesLicensorsLe = QLineEdit(self.rightFrame)
        self.seriesLicensorsLe.setObjectName(u"seriesLicensorsLe")

        self.gridLayout.addWidget(self.seriesLicensorsLe, 10, 1, 1, 1)

        self.seriesStatusLe = QLineEdit(self.rightFrame)
        self.seriesStatusLe.setObjectName(u"seriesStatusLe")

        self.gridLayout.addWidget(self.seriesStatusLe, 7, 1, 1, 1)

        self.seriesFinishDateLe = QLineEdit(self.rightFrame)
        self.seriesFinishDateLe.setObjectName(u"seriesFinishDateLe")

        self.gridLayout.addWidget(self.seriesFinishDateLe, 4, 1, 1, 1)

        self.seriesSynopsisLe = QLineEdit(self.rightFrame)
        self.seriesSynopsisLe.setObjectName(u"seriesSynopsisLe")

        self.gridLayout.addWidget(self.seriesSynopsisLe, 15, 1, 1, 1)

        self.seriesGenresLe = QLineEdit(self.rightFrame)
        self.seriesGenresLe.setObjectName(u"seriesGenresLe")

        self.gridLayout.addWidget(self.seriesGenresLe, 12, 1, 1, 1)

        self.seriesAiredLabel = QLabel(self.rightFrame)
        self.seriesAiredLabel.setObjectName(u"seriesAiredLabel")

        self.gridLayout.addWidget(self.seriesAiredLabel, 8, 0, 1, 1)

        self.seriesLanguageFormat = QLabel(self.rightFrame)
        self.seriesLanguageFormat.setObjectName(u"seriesLanguageFormat")

        self.gridLayout.addWidget(self.seriesLanguageFormat, 2, 0, 1, 1)

        self.seriesTitleLe = QLineEdit(self.rightFrame)
        self.seriesTitleLe.setObjectName(u"seriesTitleLe")

        self.gridLayout.addWidget(self.seriesTitleLe, 0, 1, 1, 1)

        self.seriesProducersLabel = QLabel(self.rightFrame)
        self.seriesProducersLabel.setObjectName(u"seriesProducersLabel")

        self.gridLayout.addWidget(self.seriesProducersLabel, 9, 0, 1, 1)

        self.seriesLangCbox = QComboBox(self.rightFrame)
        self.seriesLangCbox.addItem("")
        self.seriesLangCbox.addItem("")
        self.seriesLangCbox.setObjectName(u"seriesLangCbox")

        self.gridLayout.addWidget(self.seriesLangCbox, 2, 1, 1, 1)

        self.seriesTypeLe = QLineEdit(self.rightFrame)
        self.seriesTypeLe.setObjectName(u"seriesTypeLe")

        self.gridLayout.addWidget(self.seriesTypeLe, 5, 1, 1, 1)

        self.seriesBackgroundLe = QLineEdit(self.rightFrame)
        self.seriesBackgroundLe.setObjectName(u"seriesBackgroundLe")

        self.gridLayout.addWidget(self.seriesBackgroundLe, 16, 1, 1, 1)

        self.seriesStartDateLabel = QLabel(self.rightFrame)
        self.seriesStartDateLabel.setObjectName(u"seriesStartDateLabel")

        self.gridLayout.addWidget(self.seriesStartDateLabel, 3, 0, 1, 1)

        self.seriesFinishDateLabel = QLabel(self.rightFrame)
        self.seriesFinishDateLabel.setObjectName(u"seriesFinishDateLabel")

        self.gridLayout.addWidget(self.seriesFinishDateLabel, 4, 0, 1, 1)

        self.seriesYearLe = QLineEdit(self.rightFrame)
        self.seriesYearLe.setObjectName(u"seriesYearLe")

        self.gridLayout.addWidget(self.seriesYearLe, 17, 1, 1, 1)

        self.seriesProducersLe = QLineEdit(self.rightFrame)
        self.seriesProducersLe.setObjectName(u"seriesProducersLe")

        self.gridLayout.addWidget(self.seriesProducersLe, 9, 1, 1, 1)

        self.seriesBackgroundLabel = QLabel(self.rightFrame)
        self.seriesBackgroundLabel.setObjectName(u"seriesBackgroundLabel")

        self.gridLayout.addWidget(self.seriesBackgroundLabel, 16, 0, 1, 1)

        self.seriesThemesLe = QLineEdit(self.rightFrame)
        self.seriesThemesLe.setObjectName(u"seriesThemesLe")

        self.gridLayout.addWidget(self.seriesThemesLe, 13, 1, 1, 1)

        self.titleLabel = QLabel(self.rightFrame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.seriesAiredLe = QLineEdit(self.rightFrame)
        self.seriesAiredLe.setObjectName(u"seriesAiredLe")

        self.gridLayout.addWidget(self.seriesAiredLe, 8, 1, 1, 1)

        self.seriesStudioLabel = QLabel(self.rightFrame)
        self.seriesStudioLabel.setObjectName(u"seriesStudioLabel")

        self.gridLayout.addWidget(self.seriesStudioLabel, 11, 0, 1, 1)

        self.seriesStudiosLe = QLineEdit(self.rightFrame)
        self.seriesStudiosLe.setObjectName(u"seriesStudiosLe")

        self.gridLayout.addWidget(self.seriesStudiosLe, 11, 1, 1, 1)

        self.seriesDurationLabel = QLabel(self.rightFrame)
        self.seriesDurationLabel.setObjectName(u"seriesDurationLabel")

        self.gridLayout.addWidget(self.seriesDurationLabel, 14, 0, 1, 1)

        self.seriesDurationLe = QLineEdit(self.rightFrame)
        self.seriesDurationLe.setObjectName(u"seriesDurationLe")

        self.gridLayout.addWidget(self.seriesDurationLe, 14, 1, 1, 1)


        self.gridLayout_2.addWidget(self.rightFrame, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.seriesArtLabel.setText(QCoreApplication.translate("Dialog", u"Series Art", None))
        self.seriesLookupBtn.setText(QCoreApplication.translate("Dialog", u"Lookup Series Info", None))
        self.chooseArtBtn.setText(QCoreApplication.translate("Dialog", u"Choose File", None))
        self.seriesLicensorsLabel.setText(QCoreApplication.translate("Dialog", u"Licensors", None))
        self.seriesSynopsisLabel.setText(QCoreApplication.translate("Dialog", u"Synopsis", None))
        self.englishTitleLabel.setText(QCoreApplication.translate("Dialog", u"English Title", None))
        self.seriesStatusLabel.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.seriesGenresLabel.setText(QCoreApplication.translate("Dialog", u"Genres", None))
        self.seriesYearLabel.setText(QCoreApplication.translate("Dialog", u"Year", None))
        self.seriesThemesLabel.setText(QCoreApplication.translate("Dialog", u"Themes", None))
        self.seriesEpisodesLabel.setText(QCoreApplication.translate("Dialog", u"Episodes", None))
        self.seriesTypeLabel.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.seriesAiredLabel.setText(QCoreApplication.translate("Dialog", u"Aired", None))
        self.seriesLanguageFormat.setText(QCoreApplication.translate("Dialog", u"Sub/Dub *", None))
        self.seriesProducersLabel.setText(QCoreApplication.translate("Dialog", u"Producers", None))
        self.seriesLangCbox.setItemText(0, QCoreApplication.translate("Dialog", u"SUB", None))
        self.seriesLangCbox.setItemText(1, QCoreApplication.translate("Dialog", u"DUB", None))

        self.seriesStartDateLabel.setText(QCoreApplication.translate("Dialog", u"Start Date *", None))
        self.seriesFinishDateLabel.setText(QCoreApplication.translate("Dialog", u"Finish Date *", None))
        self.seriesBackgroundLabel.setText(QCoreApplication.translate("Dialog", u"Background", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Title *", None))
        self.seriesStudioLabel.setText(QCoreApplication.translate("Dialog", u"Studios", None))
        self.seriesDurationLabel.setText(QCoreApplication.translate("Dialog", u"Duration", None))
    # retranslateUi


    # jikan api json response sometimes returns a value that is a list of objects.
    # pass the key of the term as a string to this function to get all dict vales in the array with that key.
    def concatObjectListValues(self, search_key_arr):
        print("DEGUG object to Search : ", search_key_arr)
        values_list = []

        for k in search_key_arr:
            print(k)
            values_list.append(str(k['name']))
        
        values_list_string = ",".join(values_list)
        return values_list_string

    def fetchInfo(self):
        self.lookupDialog = QDialog()
        self.seriesLookup.setupUi(self.lookupDialog)
        # self.lookupDialog.show()
        
        # https://stackoverflow.com/questions/19462112/pyqt-wait-until-widget-closes
        # https://doc.qt.io/qt-5/qdialog.html#exec
        self.lookupDialog.exec()
        self.autofillJikanData()

    
    def autofillJikanData(self):
        d = self.seriesLookup.getSeriesInfo()
        a = self.seriesLookup.getArt()

        # add more labels here and fill them.

        # self.seriesArtLabel.setPixmap(a)
        # self.seriesTitleLe.setText(d[0])
        # self.seriesTypeLe.setText(d[1])
        # self.seriesGenresLe.setText(d[2])

        jikanSeriesKeys = [
            # 'large_image_url',
            'title_english',
            'title_japanese',
            'aired',
            'synopsis',
            'background',
            'year',
            'producers',
            'licensors',
            'studios',
            'type',
            'episodes',
            'status',
            'duration',
            'genres',
            'themes'
        ]


        # c = {}
        k = d.keys()
        print("json keys :", k)
        for x in jikanSeriesKeys:
            if x == 'title_english':
                print("English Title value", d[x])
                self.seriesEnglishTitleLe.setText(d[x])
            elif x == 'title_japanese':
                print("Japanese Title", d[x])
                self.seriesTitleLe.setText(d[x])
            elif x == 'aired':
                print("aired", d[x])
                print("DEBUG aired : ", d[x]['string'])
                self.seriesAiredLe.setText(d[x]['string'])
            elif x == 'synopsis':
                print("synopsis", d[x])
                self.seriesSynopsisLe.setText(d[x])
            elif x == 'background':
                print("background", d[x])
                self.seriesBackgroundLe.setText(d[x])
            elif x == 'year':
                print("year", d[x])
                self.seriesYearLe.setText(str(d[x]))
            elif x == 'producers':
                print("producers", d[x])
                producers_string = self.concatObjectListValues(d[x])
                self.seriesProducersLe.setText(producers_string)            
            elif x == 'licensors':
                print("licensors", d[x])
                licensors_string = self.concatObjectListValues(d[x])
                self.seriesLicensorsLe.setText(licensors_string)
            elif x == 'studios':
                print("studios", d[x])
                studios_string = self.concatObjectListValues(d[x])
                self.seriesStudiosLe.setText(studios_string)
            elif x == 'type':
                print("type", d[x])
                self.seriesTypeLe.setText(d[x])
            elif x == 'episodes':
                print("episodes", str(d[x]))
                self.seriesEpisodesLe.setText(str(d[x]))
            elif x == 'status':
                print("status", d[x])
                self.seriesStatusLe.setText(d[x])
            elif x == 'duration':
                print("duration", d[x])
                self.seriesDurationLe.setText(str(d[x]))
            elif x == 'genres':
                print("genres", d[x])
                genres_string = self.concatObjectListValues(d[x])
                self.seriesGenresLe.setText(genres_string)
            elif x == 'theme':
                print("theme", d[x])
                self.seriesThemesLe.setText(d[x])
            


    def getUserSubmission(self):
        self.seriesLookup.getSeriesInfo()


    def getFinalResults(self):
        final_results = []
        
        try:
            final_results.append(self.seriesArtLabel.pixmap())
            final_results.append(self.seriesTitleLe.text())
            final_results.append(self.seriesEnglishTitleLe.text())
            final_results.append(self.seriesLangCbox.currentText())
            final_results.append(self.seriesStartDateLe.text())
            final_results.append(self.seriesFinishDateLe.text())
            final_results.append(self.seriesTypeLe.text())
            final_results.append(self.seriesGenresLe.text())
            final_results.append(self.seriesThemesLe.text())
            final_results.append(self.seriesThemesLe.text())
        except:
            final_results.append('')



        print(final_results)

        dbInfo().entrySubmit(final_results)
        self.dialog.accept()
        #return final_results
        

    # def entrySubmit(self, seriesdata):

    #         if seriesdata:

    #             # art
    #             # title
    #             # english title
    #             # sub/dub - manually entered.
    #             # start date - manually entered.
    #             # end date - manually entered.
    #             # type
    #             # genres
    #             # themes

    #             seriesArt = seriesdata[0]
    #             seriesTitle = seriesdata[1]
    #             seriesEnglishTitle = seriesdata[2]
    #             seriesFormat = seriesdata[3]
    #             seriesStartDate = seriesdata[4]
    #             seriesFinishDate = seriesdata[5]
    #             seriesType = seriesdata[6]
    #             seriesGeneres = seriesdata[7]
    #             seriesThemes = seriesdata[8]



    #             # get lineedit texts
    #             # get the art image
    #             # self.title = self.seriesTitle_le.text()
    #             # self.englishtitle = self.seriesEnglishTitle_le.text()


    #             # self.language = self.seriesFormat_cb.currentText()

    #             # self.start = self.startDate_le.text()
    #             # self.fin = self.completionDate_le.text()
    #             # self.type = self.seriesType_le.text()

    #             # execute sql insert

    #             conn = sqlite3.connect('saldb.sqlite')  

    #             cursor = conn.cursor()



    #             if seriesArt.pixmap() != None:

    #                 pix = self.artLabel.pixmap()
    #                 b_array = QByteArray()
    #                 buffer = QBuffer(b_array)
    #                 buffer.open(QIODevice.WriteOnly)
    #                 pix.save(buffer, "JPG")
    #                 blob = b_array.data()


    #             else:

    #                 with open('icons/saldb_darkred.png', 'rb') as file:
    #                     blob = file.read()
    #                 file.close()

                
                
    #             # info_tuple = (blob, self.title, self.englishtitle, self.language, self.start, self.fin, self.type)
    #             info_tuple = (blob, seriesTitle, seriesEnglishTitle, seriesFormat, seriesStartDate, seriesFinishDate, seriesType, seriesGeneres, seriesThemes)

    #             # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?, ?)", info_tuple)
    #             cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type, Series_Genres, Series_Themes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_tuple)


    #             conn.commit()

    #             conn.close()



    #             rows = self.watchListTable.rowCount()
    #             self.watchListTable.setRowCount(rows + 1)

    #             col = 0


    #             for item in range(len(info_tuple)):
    #                 if col == 0:
    #                     label = QLabel()
    #                     label.setScaledContents(True)
    #                     pixmap = QPixmap()
    #                     pixmap.loadFromData(info_tuple[item])
    #                     #pixmap.scaled(50, 3000, Qt.IgnoreAspectRatio, Qt.FastTransformation)
    #                     label.setPixmap(pixmap.scaled(75, 100, Qt.KeepAspectRatio, Qt.FastTransformation))
    #                     self.watchListTable.setCellWidget(self.watchListTable.rowCount()-1, col, label)
    #                 else:
    #                     self.watchListTable.setItem(self.watchListTable.rowCount()-1, col, QTableWidgetItem(info_tuple[item]))
    #                 col += 1

    #             self.series_dialog.close()


    #         else:
    #             print("Missing Title Entry")
    #             # msg_nullTitle = QMessageBox(self.mainWindow)
    #             # msg_nullTitle.setText("Title can not be blank")
    #             # msg_nullTitle.setWindowTitle("Missing Entry Title")

    #             # msg_nullTitle.show()

    #         self.dialog.accept()
        
        