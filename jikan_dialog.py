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


        self.btn1 = QPushButton("Select")
        self.btn2 = QPushButton("Select")
        self.btn3 = QPushButton("Select")


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


    self.setLayout(layout)


    layout.addWidget(self.title, 1, 1)

    layout.addWidget(self.result1_img, 2, 1)
    layout.addWidget(self.result2_img, 2, 2)
    layout.addWidget(self.result3_img, 2, 3)

    layout.addWidget(self.result1_title, 3, 1)
    layout.addWidget(self.result2_title, 3, 2)
    layout.addWidget(self.result3_title, 3, 3)

    layout.addWidget(self.btn1, 4, 1)
    layout.addWidget(self.btn2, 4, 2)
    layout.addWidget(self.btn3, 4, 3)



    self.show()



    def select1(self):
        self.artLabel.setPixmap(self.entry1)

    def select2(self):
        self.artLabel.setPixmap(self.entry2)

    def select3(self):
        self.artLabel.setPixmap(self.entry3)