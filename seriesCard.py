import os
import sys
import requests
import json

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QGridLayout


class seriesCard(QWidget):
    def __init__(self, titletxt, art, eps, seriestype, generes , airstart, airend):
        super(seriesCard, self).__init__()

        self.seriesTitleTxt = titletxt
        self.seriesArt = art
        self.seriesType = seriestype
        self.seriesAirStart = airstart
        self.seriesAirEnd = airend
        self.seriesEpisodeCount = eps
        self.seriesGeneres = generes

        

    def setTitle(self):
        pass

    def setSeriesArt(self):
        pass
    def setSeriesType(self):
        pass
    def setSeriesAirStart(self):
        pass
    def setSeriesAirEnd(self):
        pass
    def setSeriesEpisodeCount(self):
        pass
    def setSeriesGeneres(self):
        pass

    
    # getters

    def getSeriesTitle(self):
        return self.seriesTitleTxt

    def getSeriesArt(self):
        return self.seriesArt

    def getSeriesType(self):
        return self.seriesType


    def getSeriesAirStart(self):
        return self.seriesAirStart


    def getSeriesAirEnd(self):
        return self.seriesAirEnd

    def getSeriesEpisodeCount(self):
        return self.seriesEpisodeCount
    
    def getSeriesGeneres(self):
        return self.seriesGeneres








