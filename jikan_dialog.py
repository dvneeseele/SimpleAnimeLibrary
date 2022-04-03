import os
import sys
import requests
import json

from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel, QPushButton, QVBoxLayout, QGridLayout


class jikanData(QWidget):
    def __init__(self, titletxt, label):
        super(jikanData, self).__init__()

        self.seriesTitle = titletxt
        self.titleart_lbl = label


        #self.jikanData.setAcceptDrops(True)
        self.selection = ""

        self.title = QLabel("Results For {}".format(self.seriesTitle))


        self.btn1 = QPushButton("Select")
        self.btn1.clicked.connect(self.select1)
        self.btn2 = QPushButton("Select")
        self.btn2.clicked.connect(self.select2)
        self.btn3 = QPushButton("Select")
        self.btn3.clicked.connect(self.select3)


        self.entry1 = QLabel()
        self.entry2 = QLabel()
        self.entry3 = QLabel()


        self.entryTitle1 = QLabel()
        self.entryTitle2 = QLabel()
        self.entryTitle3 = QLabel()

        self.entryType1 = QLabel()
        self.entryType2 = QLabel()
        self.entryType3 = QLabel()



        self.layout = QGridLayout()


        self.layout.addWidget(self.title, 1, 1)

        self.layout.addWidget(self.entry1, 2, 1)
        self.layout.addWidget(self.entry2, 2, 2)
        self.layout.addWidget(self.entry3, 2, 3)

        self.layout.addWidget(self.entryTitle1, 3, 1)
        self.layout.addWidget(self.entryTitle2, 3, 2)
        self.layout.addWidget(self.entryTitle3, 3, 3)

        self.layout.addWidget(self.entryType1, 4, 1)
        self.layout.addWidget(self.entryType2, 4, 2)
        self.layout.addWidget(self.entryType3, 4, 3)


        self.layout.addWidget(self.btn1, 5, 1)
        self.layout.addWidget(self.btn2, 5, 2)
        self.layout.addWidget(self.btn3, 5, 3)


        self.setLayout(self.layout)
        
        self.search()



    def search(self):



        #api_base = 'https://api.jikan.moe/v3'

        #url = api_base + '/search/anime?q={}&page=1'.format(self.seriesTitle)


        # jikan api v4
        # example search (https://api.jikan.moe/v4/anime?q=Naruto&sfw)
        api_base = 'https://api.jikan.moe/v4'

        url = api_base + '/anime?q={}&sfw'.format(self.seriesTitle)


        req = requests.get(url)
        resp = req.json()


        # TODO : So for some searches like Death Note, there are only 2 matches for that search string, so the third option below doesn't work.
        # Need error handling for this. 
        # Need to find a more dynamic way of handling the response. Just list all results or something...


        # .content returns image data in bytes

        self.result1_img = resp['data'][0]['images']['jpg']['large_image_url']
        self.result1_getData = requests.get(self.result1_img).content

        self.result2_img = resp['data'][1]['images']['jpg']['large_image_url']
        self.result2_getData = requests.get(self.result2_img).content

        self.result3_img = resp['data'][2]['images']['jpg']['large_image_url']
        self.result3_getData = requests.get(self.result3_img).content

        self.result1_title = resp['data'][0]['title']
        self.result2_title = resp['data'][1]['title']
        self.result3_title = resp['data'][2]['title']

        self.result1_type = resp['data'][0]['type']
        self.result2_type = resp['data'][1]['type']
        self.result3_type = resp['data'][2]['type']

        self.entryType1.setText("Series Type : {}".format(self.result1_type))
        self.entryType2.setText("Series Type : {}".format(self.result2_type))
        self.entryType3.setText("Series Type : {}".format(self.result3_type))


        self.pix = QPixmap()

        self.pix.loadFromData(self.result1_getData)

        self.entry1.setPixmap(self.pix)
        self.entryTitle1.setText("Series Title : {}".format(self.result1_title))

        self.pix.loadFromData(self.result2_getData)
        self.entry2.setPixmap(self.pix)
        self.entryTitle2.setText("Series Title : {}".format(self.result2_title))

        self.pix.loadFromData(self.result3_getData)
        self.entry3.setPixmap(self.pix)
        self.entryTitle3.setText("Series Title : {}".format(self.result3_title))




    def select1(self):
        self.titleart_lbl.setPixmap(self.entry1.pixmap())
        self.close()

    def select2(self):
        self.titleart_lbl.setPixmap(self.entry2.pixmap())
        self.close()

    def select3(self):
        self.titleart_lbl.setPixmap(self.entry3.pixmap())
        self.close()

