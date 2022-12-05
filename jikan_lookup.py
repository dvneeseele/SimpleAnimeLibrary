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
    # setupUi

    def retranslateUi(self, dialog_lookup):
        dialog_lookup.setWindowTitle(QCoreApplication.translate("dialog_lookup", u"Dialog", None))
        self.label_seriesImagePreview.setText("")
        self.label_seriesTextInfo.setText(QCoreApplication.translate("dialog_lookup", u"TextLabel", None))
    # retranslateUi

