import os
import sys
import requests
import json

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QGridLayout


class jikanData(QWidget):
    def __init__(self, titletxt):
        super().__init__()

        self.seriesTitle = titletxt

        self.jikanData.setAcceptDrops(True)

        layout = QGridLayout()

        self.title = QLabel("Results For {}".format(self.seriesTitle))


        self.entry1 = QLabel()
        self.entry2 = QLabel()
        self.entry3 = QLabel()

        self.entryTitle1 = QLabel()
        self.entryTitle2 = QLabel()
        self.entryTitle3 = QLabel()

    def jikanFetch(self):

        api_base = 'https://api.jikan.moe/v3'

        url = api_base + '/search/anime?q={}&page=1'.format(self.seriesTitle)

        req = requests.get(url)
        resp = req.json()

        # array?

        result1 = resp['results'][0]['image_url']
        result1 = resp['results'][1]['image_url']
        result1 = resp['results'][2]['image_url']





