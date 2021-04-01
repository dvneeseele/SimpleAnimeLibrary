import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QMainWindow, QAbstractItemView, QToolBar, QSplitter, QHBoxLayout, QWidget, QAction, QStackedWidget, QListWidget, QTableWidget, QTableWidgetItem, QTableView)


class salUI(object):
    def __init__(self):
        super(salUI).__init__()


    def setupUI(self, MainWindow):

        # setup menubar

        menubar = MainWindow.menuBar()

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

        self.addnewAction = QAction("Create New Entry", MainWindow)
        self.addnewAction.setShortcut('Ctrl+N')

        self.toolbar.addAction(self.addnewAction)


        self.editAction = QAction("Edit Entry", MainWindow)
        self.editAction.setShortcut("Ctrl+E")

        self.toolbar.addAction(self.editAction)

        self.deleteAction = QAction("Delete Entry", MainWindow)
        self.deleteAction.setShortcut("Ctrl+D")

        self.toolbar.addAction(self.deleteAction)

        self.infoAction = QAction("App Info")

        self.toolbar.addAction(self.infoAction)


#############################################################################################################



        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName('central')

        self.splitter = QSplitter(self.centralWidget)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setStretchFactor(0, 25)
        self.splitter.setStretchFactor(1, 75)

        # sidebar (QListWidget)

        self.sidebar = QListWidget(self.splitter)
        self.sidebar.setObjectName('sidebar')
        self.sidebar.addItem('Fin.')
        self.sidebar.addItem('Planned')
        self.sidebar.addItem('Ongoing')
        self.sidebar.addItem('Current')
        self.sidebar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)


        # [nevermind lol] pretty sure i dont need this here, it should be created in the backend and added to the stack.
        self.watchListTable = QTableWidget()
        self.watchListTable.setObjectName('watchListTable')
        self.watchListTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.watchListTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.watchListTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.watchListTable.customContextMenuRequested.connect(self.tableContextMenu)
        self.watchListTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.watchListTable.setColumnCount(7)

        self.watchListTable.setHorizontalHeaderLabels(["Art", "Title", "English Title", "SUB/DUB", "Start Date" , "Completion Date", "Series Type"])







        # stackwidget to switch contents of list catagories

        self.tableStack = QStackedWidget(self.splitter)
        self.tableStack.setObjectName('tablestack')

        self.tableStack.addWidget(self.watchListTable)

        
        # add widgets to splitter

        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.tableStack)


        self.splitter.setSizes([50, 650])



########################################################################################################
########################################################################################################



        self.boxLayout = QHBoxLayout()
        self.centralWidget.setLayout(self.boxLayout)
        MainWindow.setCentralWidget(self.centralWidget)



        self.boxLayout.addWidget(self.splitter) 



        MainWindow.show()



