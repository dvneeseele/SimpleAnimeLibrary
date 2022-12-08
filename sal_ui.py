#############################################################################
# dvneeseele
#############################################################################

import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QMainWindow, QAbstractItemView, QToolBar, QSplitter, QHBoxLayout, QWidget, QAction, QStackedWidget, QListWidget, QTableWidget, QTableWidgetItem, QTableView, QHeaderView)


class salUI(object):
    def __init__(self):
        super(salUI).__init__()


    def setupUI(self, MainWindow):

        MainWindow.setWindowIcon(QIcon("icons/saldb_red"))
        MainWindow.setWindowTitle("Simple Anime Library   |   ヽ( ´ー`)ノ")

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
        self.toolbar.setIconSize(QSize(40, 40))

        MainWindow.addToolBar(self.toolbar)

        self.addnewAction = QAction(QIcon("icons/add_1.png"),"Create New Entry", MainWindow)
        self.addnewAction.setShortcut('Ctrl+N')

        self.toolbar.addAction(self.addnewAction)

        self.deleteAction = QAction(QIcon("icons/delete_1.png") ,"Delete Entry", MainWindow)
        self.deleteAction.setShortcut("Ctrl+D")

        self.toolbar.addAction(self.deleteAction)

        self.editAction = QAction(QIcon("icons/edit.png") ,"Edit Entry", MainWindow)
        self.editAction.setShortcut("Ctrl+E")

        self.toolbar.addAction(self.editAction)

        self.toolbar.addSeparator()

        self.tableViewAction = QAction(QIcon("icons/saldbicon.png") ,"Table View", MainWindow)
        self.tableViewAction.setShortcut("ctrl+t")
        self.toolbar.addAction(self.tableViewAction)

        self.cardViewAction = QAction(QIcon("icons/saldb_cyan.png") ,"Card View", MainWindow)
        self.cardViewAction.setShortcut("ctrl+alt+c")
        self.toolbar.addAction(self.cardViewAction)


        self.toolbar.addSeparator()




        self.findAction = QAction(QIcon("icons/find.png") ,"Search", MainWindow)
        self.findAction.setShortcut("Ctrl+F")

        self.toolbar.addAction(self.findAction)

        self.queryAction = QAction(QIcon("icons/filter.png") ,"Filter/Sort", MainWindow)
        self.queryAction.setShortcut("Ctrl+Alt+Q")

        self.toolbar.addAction(self.queryAction)

        self.toolbar.addSeparator()

        self.jikanAction = QAction(QIcon("icons/find.png") , "Search Anime Series", MainWindow)
        self.jikanAction.setShortcut("ctrl+shift+s")
        self.toolbar.addAction(self.jikanAction)


        self.toolbar.addSeparator()



        self.settingsAction = QAction(QIcon("icons/settings.png") ,"App Settings", MainWindow)
        self.settingsAction.setShortcut("Ctrl+Shift+S")

        self.toolbar.addAction(self.settingsAction)

        self.infoAction = QAction(QIcon("icons/info.png") ,"App Info", MainWindow)

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
        self.watchListTable.setFont(QFont('Arial', 14))
        self.watchListTable.setWordWrap(False)
        #self.watchListTable.setTextAlignment(Qt.AlignCenter)
        self.watchListTable.setColumnCount(7)
        self.watchListTable.setShowGrid(False)

        self.watchListTable.setHorizontalHeaderLabels(["Art", "Title", "English Title", "SUB/DUB", "Start Date" , "Completion Date", "Series Type"])
        #self.watchListTable.verticalHeader().setDefaultSectionSize(140)
        self.watchListTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.watchListTable.horizontalHeader().setDefaultSectionSize(120)
        self.watchListTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)







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



