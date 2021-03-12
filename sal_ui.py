import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QToolBar, QSplitter, QHBoxLayout, QWidget, QAction, QStackedWidget, QListWidget, QTableWidget)


class salUI():
    def __init__(self):
        super(salUI).__init__()


    def setupUI(self, MainWindow):

        # setup menubar

        menubar = MainWindow.menubar()

        self.mb_file = menubar.addMenu("File")
        self.mb_edit = menubar.addMenu("Edit")
        self.mb_view = menubar.addMenu("View")
        self.mb_help = menubar.addMenu("Help")


        # menubar file menu

        self.mb_newAction = QAction("New Entry", MainWindow)
        self.mb_file.addAction(self.mb_newAction)

        # menubar edit menu

        self.mb_editEntryAction = QAction("Edit Entry", MainWindow)
        self.mb_edit.addAction(self.mb_editEntryAction)

        # menubar view menu

        # TODO

        # menubar help menu

        # TODO



        # Toolbar

        self.toolbar = QToolBar(MainWindow)

        MainWindow.addToolBar(self.toolbar)

        self.addnew = QAction("Create New Entry", MainWindow)
        self.addnew.setShortcut('Ctrl+N')

        # the rest is TODO



        