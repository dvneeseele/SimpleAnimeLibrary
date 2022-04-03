import os
import sys
import requests
import json

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QGridLayout


class seriesCard(QWidget):
    def __init__(self, titletxt, art, eps, seriestype, generes , airstart, airend):
        super(seriesCard, self).__init__()

        self.titleTxt = titletxt
        self.seriesArt = art
        self.seriesType = seriestype
        self.seriesAirStart = airstart
        self.seriesAirEnd = airend
        self.seriesEpisodesCount = eps
        self.seriesGeneres = generes

        









