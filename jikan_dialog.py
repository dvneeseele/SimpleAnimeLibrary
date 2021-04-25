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

        pix = QPixmap()

        self.jikanData.setAcceptDrops(True)

        layout = QGridLayout()

        self.title = QLabel("Results For {}".format(self.seriesTitle))


        self.entry1 = QLabel()
        self.entry2 = QLabel()
        self.entry3 = QLabel()


        self.entryTitle1 = QLabel()
        self.entryTitle2 = QLabel()
        self.entryTitle3 = QLabel()




    api_base = 'https://api.jikan.moe/v3'

    url = api_base + '/search/anime?q={}&page=1'.format(self.seriesTitle)

    req = requests.get(url)
    resp = req.json()

    # .content returns image data in bytes

    self.result1_img = resp['results'][0]['image_url'].content
    self.result2_img = resp['results'][1]['image_url'].content
    self.result3_img = resp['results'][2]['image_url'].content

    self.result1_title = resp['results'][0]['title']
    self.result2_title = resp['results'][1]['title']
    self.result3_title = resp['results'][2]['title']


    self.entry1.setPixmap(pix.loadFromData(self.result1_img))
    self.entryTitle1.setText(self.result1_title)

    self.entry2.setPixmap(pix.loadFromData(self.result2_img))
    self.entryTitle2.setText(self.result2_title)

    self.entry3.setPixmap(pix.loadFromData(self.result3_img))
    self.entryTitle3.setText(self.result3_title)
