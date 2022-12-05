# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sal_dialogBdQDZh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.7
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *  # type: ignore
from PyQt5.QtGui import *  # type: ignore
from PyQt5.QtWidgets import *  # type: ignore
import requests
from requests.exceptions import HTTPError
#import json


class Ui_dialog_lookup(object):
    def setupUi(self, dialog_lookup):
        if not dialog_lookup.objectName():
            dialog_lookup.setObjectName(u"dialog_lookup")
        dialog_lookup.resize(1053, 694)
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
        self.lineEdit.textChanged.connect(self.seriesLookup)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_search)

        self.frame_searchresults = QFrame(dialog_lookup)
        self.frame_searchresults.setObjectName(u"frame_searchresults")
        self.frame_searchresults.setFrameShape(QFrame.StyledPanel)
        self.frame_searchresults.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_searchresults)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView_searchresults = QListView(self.frame_searchresults)
        self.listView_searchresults.setObjectName(u"listView_searchresults")

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


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_seriesInfoLabels)

        self.dialog_lookup_buttonBox = QDialogButtonBox(dialog_lookup)
        self.dialog_lookup_buttonBox.setObjectName(u"dialog_lookup_buttonBox")
        self.dialog_lookup_buttonBox.setOrientation(Qt.Horizontal)
        self.dialog_lookup_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dialog_lookup_buttonBox)


        self.retranslateUi(dialog_lookup)
        self.dialog_lookup_buttonBox.accepted.connect(dialog_lookup.accept)
        self.dialog_lookup_buttonBox.rejected.connect(dialog_lookup.reject)

        QMetaObject.connectSlotsByName(dialog_lookup)


        self.seriesArt = []
        self.title = []
        self.englishTitle = []
        self.seriesType = []
        self.seriesEpisodes = []
        self.seriesStatus = []
        self.seriesDuration = []
        self.seriesGenres = []
        self.seriesThemes = []


    # setupUi

    def retranslateUi(self, dialog_lookup):
        dialog_lookup.setWindowTitle(QCoreApplication.translate("dialog_lookup", u"Dialog", None))
        self.label_seriesImagePreview.setText("")
        self.label_seriesTextInfo.setText(QCoreApplication.translate("dialog_lookup", u"TextLabel", None))
    # retranslateUi

    def seriesLookup(self):
        # jikan api v4
        # example search (https://api.jikan.moe/v4/anime?q=Naruto&sfw)
        api_base = 'https://api.jikan.moe/v4'

        url = api_base + '/anime?q={}&sfw'.format(self.seriesTitle)

        try:
            req = requests.get(url)
            resp = req.json()
        except HTTPError as http_err:
            print('HTTP error code : {http_err}')
            # TODO implement qmessagebox for displaying the error and exiting.
        except Exception as err:
            print('Error Occured : {err}')
            # TODO implement qmessagebox for displaying the error and exiting.

        titles_count = resp['pagination']['items']['count']

        for i in range(titles_count):
            try:
                self.seriesArt.append(resp['data'][i]['images']['jpg']['large_image_url'])
                self.title.append(resp['data'][i]['title'])
                self.englishTitle.append(resp['data'][i]['title_english'])
                self.seriesType.append(resp['data'][i]['type'])
                self.seriesEpisodes.append(resp['data'][i]['episodes'])
                self.seriesStatus.append(resp['data'][i]['status'])
                self.seriesDuration.append(resp['data'][i]['duration'])
                self.seriesGenres.append(resp['data'][i]['genres'][0]['name'])
                self.seriesThemes.append(resp['data'][i]['themes'][0]['name'])
                # self.seriesArt = resp['data'][i]['images']['jpg']['large_image_url']
                # self.title = resp['data'][i]['title']
                # self.englishTitle = resp['data'][i]['title_english']
                # self.seriesType = resp['data'][i]['type']
                # self.seriesEpisodes = resp['data'][i]['episodes']
                # self.seriesStatus = resp['data'][i]['status']
                # self.seriesDuration = resp['data'][i]['duration']
                # self.seriesGenres = resp['data'][i]['genres'][0]['name']
                # self.seriesThemes = resp['data'][i]['themes'][0]['name']
            except IndexError:
                print("Index Error Occured. Value is null")
                # TODO Probably need to find the array that errored and insert a "null" value to that array, so everything lines up.





            # print(resp['data'][i]['images']['jpg']['large_image_url'])
            # print(resp['data'][i]['title'])
            # print(resp['data'][i]['title_english'])
            # print(resp['data'][i]['type'])
            # print(resp['data'][i]['episodes'])
            # print(resp['data'][i]['status'])
            # print(resp['data'][i]['duration'])
            # print(resp['data'][i]['genres'][0]['name'])
            # print(resp['data'][i]['themes'][0]['name'])








