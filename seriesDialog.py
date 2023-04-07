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

class seriesDlg(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1026, 712)
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


        self.gridLayout_2.addWidget(self.leftFrame, 0, 0, 1, 1)

        self.rightFrame = QFrame(Dialog)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.rightFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.seriesLanguageFormat = QLabel(self.rightFrame)
        self.seriesLanguageFormat.setObjectName(u"seriesLanguageFormat")

        self.gridLayout.addWidget(self.seriesLanguageFormat, 2, 0, 1, 1)

        self.englishTitleLabel = QLabel(self.rightFrame)
        self.englishTitleLabel.setObjectName(u"englishTitleLabel")

        self.gridLayout.addWidget(self.englishTitleLabel, 1, 0, 1, 1)

        self.seriesStartDate = QLabel(self.rightFrame)
        self.seriesStartDate.setObjectName(u"seriesStartDate")

        self.gridLayout.addWidget(self.seriesStartDate, 3, 0, 1, 1)

        self.seriesTypeLe = QLineEdit(self.rightFrame)
        self.seriesTypeLe.setObjectName(u"seriesTypeLe")

        self.gridLayout.addWidget(self.seriesTypeLe, 5, 1, 1, 1)

        self.seriesGenresLe = QLineEdit(self.rightFrame)
        self.seriesGenresLe.setObjectName(u"seriesGenresLe")

        self.gridLayout.addWidget(self.seriesGenresLe, 6, 1, 1, 1)

        self.seriesFinishDateLe = QLineEdit(self.rightFrame)
        self.seriesFinishDateLe.setObjectName(u"seriesFinishDateLe")

        self.gridLayout.addWidget(self.seriesFinishDateLe, 4, 1, 1, 1)

        self.titleLabel = QLabel(self.rightFrame)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.seriesStartDateLe = QLineEdit(self.rightFrame)
        self.seriesStartDateLe.setObjectName(u"seriesStartDateLe")

        self.gridLayout.addWidget(self.seriesStartDateLe, 3, 1, 1, 1)

        self.seriesType = QLabel(self.rightFrame)
        self.seriesType.setObjectName(u"seriesType")

        self.gridLayout.addWidget(self.seriesType, 5, 0, 1, 1)

        self.seriesTitleLe = QLineEdit(self.rightFrame)
        self.seriesTitleLe.setObjectName(u"seriesTitleLe")

        self.gridLayout.addWidget(self.seriesTitleLe, 0, 1, 1, 1)

        self.seriesGenres = QLabel(self.rightFrame)
        self.seriesGenres.setObjectName(u"seriesGenres")

        self.gridLayout.addWidget(self.seriesGenres, 6, 0, 1, 1)

        self.seriesFinishDate = QLabel(self.rightFrame)
        self.seriesFinishDate.setObjectName(u"seriesFinishDate")

        self.gridLayout.addWidget(self.seriesFinishDate, 4, 0, 1, 1)

        self.seriesEnglishTitleLe = QLineEdit(self.rightFrame)
        self.seriesEnglishTitleLe.setObjectName(u"seriesEnglishTitleLe")

        self.gridLayout.addWidget(self.seriesEnglishTitleLe, 1, 1, 1, 1)

        self.seriesThemes = QLabel(self.rightFrame)
        self.seriesThemes.setObjectName(u"seriesThemes")

        self.gridLayout.addWidget(self.seriesThemes, 7, 0, 1, 1)

        self.seriesThemesLe = QLineEdit(self.rightFrame)
        self.seriesThemesLe.setObjectName(u"seriesThemesLe")

        self.gridLayout.addWidget(self.seriesThemesLe, 7, 1, 1, 1)

        self.seriesLangCbox = QComboBox(self.rightFrame)
        self.seriesLangCbox.addItem("")
        self.seriesLangCbox.addItem("")
        self.seriesLangCbox.setObjectName(u"seriesLangCbox")

        self.gridLayout.addWidget(self.seriesLangCbox, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.rightFrame, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.buttonBox.accepted.connect(self.finish)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.seriesArtLabel.setText(QCoreApplication.translate("Dialog", u"Series Art", None))
        self.seriesLookupBtn.setText(QCoreApplication.translate("Dialog", u"Lookup Series Info", None))
        self.seriesLanguageFormat.setText(QCoreApplication.translate("Dialog", u"Sub/Dub", None))
        self.englishTitleLabel.setText(QCoreApplication.translate("Dialog", u"English Title", None))
        self.seriesStartDate.setText(QCoreApplication.translate("Dialog", u"Start Date", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Title", None))
        self.seriesType.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.seriesGenres.setText(QCoreApplication.translate("Dialog", u"Genres", None))
        self.seriesFinishDate.setText(QCoreApplication.translate("Dialog", u"Finish Date", None))
        self.seriesThemes.setText(QCoreApplication.translate("Dialog", u"Themes", None))
        self.seriesLangCbox.setItemText(0, QCoreApplication.translate("Dialog", u"SUB", None))
        self.seriesLangCbox.setItemText(1, QCoreApplication.translate("Dialog", u"DUB", None))

    # retranslateUi


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

        self.seriesArtLabel.setPixmap(a)
        self.seriesTitleLe.setText(d[0])
        self.seriesTypeLe.setText(d[1])
        self.seriesGenresLe.setText(d[2])

        


    def getUserSubmission(self):
        self.seriesLookup.getSeriesInfo()


    def finish(self):
        pass