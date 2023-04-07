# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sal_dialogBdQDZh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QFrame, QFormLayout, QHBoxLayout, QLineEdit, QVBoxLayout, QLabel, QDialogButtonBox, QPushButton, QListWidget, QListWidgetItem
import requests
from requests.exceptions import HTTPError
import json


class Ui_dialog_lookup(object):
    def setupUi(self, dialog_lookup):
        if not dialog_lookup.objectName():
            dialog_lookup.setObjectName(u"dialog_lookup")
        dialog_lookup.resize(1053, 694)
        self.dialog = dialog_lookup
        self.formLayout = QFormLayout(dialog_lookup)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_search = QFrame(dialog_lookup)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_search)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame_search)
        self.lineEdit.setObjectName(u"lineEdit")
        #self.lineEdit.textChanged.connect(self.seriesLookup)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_search)

        self.frame_searchresults = QFrame(dialog_lookup)
        self.frame_searchresults.setObjectName(u"frame_searchresults")
        self.frame_searchresults.setFrameShape(QFrame.StyledPanel)
        self.frame_searchresults.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_searchresults)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView_searchresults = QListWidget(self.frame_searchresults)
        self.listView_searchresults.setObjectName(u"listView_searchresults")
        self.listView_searchresults.clicked.connect(self.itemChanged)

        self.verticalLayout_2.addWidget(self.listView_searchresults)


        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.frame_searchresults)

        self.frame_seriesInfoLabels = QFrame(dialog_lookup)
        self.frame_seriesInfoLabels.setObjectName(u"frame_seriesInfoLabels")
        self.frame_seriesInfoLabels.setFrameShape(QFrame.StyledPanel)
        self.frame_seriesInfoLabels.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_seriesInfoLabels)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_seriesImagePreview = QLabel(self.frame_seriesInfoLabels)
        self.label_seriesImagePreview.setObjectName(u"label_seriesImagePreview")

        self.verticalLayout.addWidget(self.label_seriesImagePreview)

        self.label_seriesTextInfo = QLabel(self.frame_seriesInfoLabels)
        self.label_seriesTextInfo.setObjectName(u"label_seriesTextInfo")

        self.verticalLayout.addWidget(self.label_seriesTextInfo)


        self.testlist = QListWidget()
        self.verticalLayout.addWidget(self.testlist)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_seriesInfoLabels)

        self.dialog_lookup_buttonBox = QDialogButtonBox(dialog_lookup)
        self.dialog_lookup_buttonBox.setObjectName(u"dialog_lookup_buttonBox")
        self.dialog_lookup_buttonBox.setOrientation(Qt.Horizontal)
        self.dialog_lookup_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        # Separate submit button for api search.
        self.submitSearch = QPushButton('Submit Search')
        self.submitSearch.clicked.connect(self.seriesLookup)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.submitSearch)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dialog_lookup_buttonBox)



        self.retranslateUi(dialog_lookup)
        # self.dialog_lookup_buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.testSubmit)
        self.dialog_lookup_buttonBox.accepted.connect(dialog_lookup.accept)
        #self.dialog_lookup_buttonBox.accepted.connect(self.commit)
        self.dialog_lookup_buttonBox.rejected.connect(dialog_lookup.reject)


        QMetaObject.connectSlotsByName(dialog_lookup)

        # self.selectedResults = {
        #     'large_image_url' : None,
        #     'title_english' : None,
        #     'type' : None,
        #     'episodes' : None,
        #     'status' : None,
        #     'duration' : None,
        #     'genres' : None,
        #     'themes' : None
        # }


        #self.dialog.exec()

    # setupUi

    def retranslateUi(self, dialog_lookup):
        dialog_lookup.setWindowTitle(QCoreApplication.translate("dialog_lookup", u"Dialog", None))
        self.label_seriesImagePreview.setText("hereitis")
        self.label_seriesTextInfo.setText(QCoreApplication.translate("dialog_lookup", u"", None))
    # retranslateUi



    def getArt(self):
        print("getting art")
        return self.label_seriesImagePreview.pixmap()


    def getListResultItems(self):
        self.allItems = []

        for x in range(self.testlist.count()):
            self.allItems.append(self.testlist.item(x).text())
        
        return self.allItems


    def testSubmit(self):

        results = self.getListResultItems()

        
        for i in range(len(self.selectedResults.keys())):
            k = list(self.selectedResults.keys())[i]
            self.selectedResults[k] = results[i]
            # print("Final :", json.dumps(self.selectedResults, indent=4))

        return self.selectedResults



    def getSeriesInfo(self):
        return self.getListResultItems()
        self.dialog.accept()


    def seriesLookup(self):
        # jikan api v4
        # example search (https://api.jikan.moe/v4/anime?q=Naruto&sfw)
        api_base = 'https://api.jikan.moe/v4'

        url = api_base + '/anime?q={}&sfw'.format(self.lineEdit.text())

        try:
            req = requests.get(url)
            self.resp = req.json()
        except HTTPError as http_err:
            print('HTTP error code : {http_err}')
            # TODO implement qmessagebox for displaying the error and exiting.
        except Exception as err:
            print('Error Occured : {err}')
            # TODO implement qmessagebox for displaying the error and exiting.

        titles_count = self.resp['pagination']['items']['count']

        self.listView_searchresults.clear()

        for i in range(titles_count):
            try:
                self.listView_searchresults.addItem(self.resp['data'][i]['title'])
                # item = QStandardItem(resp['data'][i]['title'])
                # self.model.appendRow(item)
            except Exception as err:
                print('Error Occured :, {err}')
                continue


    def itemChanged(self):
        self.idx = self.listView_searchresults.currentRow()

        self.testlist.clear()

        testarr = [
            'large_image_url',
            'title_english',
            'type',
            'episodes',
            'status',
            'duration',
            'genres',
            'themes'
        ]

        for d in testarr:
            try:
                if d == 'large_image_url':
                    print('hey look its a image')
                    art = requests.get(self.resp['data'][self.idx]['images']['jpg']['large_image_url']).content
                    #lbl = QLabel()
                    pix = QPixmap()
                    pix.loadFromData(art)
                    self.label_seriesImagePreview.setPixmap(pix)
                    #lbl.setPixmap(pix)
                    #itm = QListWidgetItem(d, self.testlist)
                    #self.testlist.setItemWidget(itm, lbl)
                elif d == 'genres':
                    print("its a", d)
                    itmtxt = self.resp['data'][self.idx][d][0]['name']
                    itm = QListWidgetItem(itmtxt, self.testlist)
                elif d == 'themes':
                    itmtxt = self.resp['data'][self.idx][d][0]['name']
                    itm = QListWidgetItem(itmtxt, self.testlist)                    
                else:
                    itmtxt = self.resp['data'][self.idx][d]
                    itm = QListWidgetItem(itmtxt, self.testlist)
            except:
                itm = QListWidgetItem("null", self.testlist)


