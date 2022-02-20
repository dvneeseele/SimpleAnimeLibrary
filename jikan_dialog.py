import os
import sys
import requests
import json

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QGridLayout


class jikanData(QWidget):
    def __init__(self, titletxt):
        super(jikanData, self).__init__()

        self.seriesTitle = titletxt



        #self.jikanData.setAcceptDrops(True)



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


        self.layout = QGridLayout()


        self.layout.addWidget(self.title, 1, 1)

        self.layout.addWidget(self.entry1, 2, 1)
        self.layout.addWidget(self.entry2, 2, 2)
        self.layout.addWidget(self.entry3, 2, 3)

        self.layout.addWidget(self.entryTitle1, 3, 1)
        self.layout.addWidget(self.entryTitle2, 3, 2)
        self.layout.addWidget(self.entryTitle3, 3, 3)

        self.layout.addWidget(self.btn1, 4, 1)
        self.layout.addWidget(self.btn2, 4, 2)
        self.layout.addWidget(self.btn3, 4, 3)


        self.setLayout(self.layout)
        
        self.search()



    def search(self):

        api_base = 'https://api.jikan.moe/v3'

        url = api_base + '/search/anime?q={}&page=1'.format(self.seriesTitle)

        req = requests.get(url)
        resp = req.json()


        # .content returns image data in bytes

        self.result1_img = resp['results'][0]['image_url']
        self.result1_getData = requests.get(self.result1_img).content

        self.result2_img = resp['results'][1]['image_url']
        self.result2_getData = requests.get(self.result2_img).content

        self.result3_img = resp['results'][2]['image_url']
        self.result3_getData = requests.get(self.result3_img).content

        self.result1_title = resp['results'][0]['title']
        self.result2_title = resp['results'][1]['title']
        self.result3_title = resp['results'][2]['title']



        self.pix = QPixmap()

        self.pix.loadFromData(self.result1_getData)

        self.entry1.setPixmap(self.pix)
        self.entryTitle1.setText(self.result1_title)

        self.pix.loadFromData(self.result2_getData)
        self.entry2.setPixmap(self.pix)
        self.entryTitle2.setText(self.result2_title)

        self.pix.loadFromData(self.result3_getData)
        self.entry3.setPixmap(self.pix)
        self.entryTitle3.setText(self.result3_title)




    def select1(self):
        self.artLabel.setPixmap(self.entry1)

    def select2(self):
        self.artLabel.setPixmap(self.entry2)

    def select3(self):
        self.artLabel.setPixmap(self.entry3)


        
