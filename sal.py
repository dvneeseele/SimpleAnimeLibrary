#############################################################################
# me
#############################################################################


from sal_ui import salUI
import os
import sys
import sqlite3
import requests


from PyQt5 import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage, QTextListFormat, QFont, QColor
from PyQt5.QtCore import QEvent, Qt, QSize, QDate, QTime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFormLayout, QLineEdit, QTabWidget, QWidget, QPushButton, QListWidgetItem, QLabel, QVBoxLayout, QStackedWidget,
                            QColorDialog, QMessageBox, QFileDialog, QDialog, QFontDialog)



class SAL_app(salUI):
    def __init__(self):
        super().__init__()

        self.mainWindow = QMainWindow()
        self.setupUI(self.mainWindow)

        # Menubar functions

        # TODO

        # Toolbar functions

        # TODO

        # load function here






    def getCurrentStack(self):
        pass









    def dbLoad(self):
        
        # pandas vs just for loop over db??

        try:






