import sys
import os
import sqlite3
import json
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice

class dbInfo(object):
    def __init__(self):
        pass

    def entrySubmit(self, seriesdata):

        # art
        # title
        # english title
        # sub/dub - manually entered.
        # start date - manually entered.
        # end date - manually entered.
        # type
        # genres
        # themes

        seriesArt = seriesdata[0]
        seriesTitle = seriesdata[1]
        seriesEnglishTitle = seriesdata[2]
        seriesFormat = seriesdata[3]
        seriesStartDate = seriesdata[4]
        seriesFinishDate = seriesdata[5]
        seriesType = seriesdata[6]
        seriesGeneres = seriesdata[7]
        seriesThemes = seriesdata[8]
        
        # execute sql insert

        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()



        # if seriesArt.pixmap() != None:
            
        #     pix = self.artLabel.pixmap()
        #     b_array = QByteArray()
        #     buffer = QBuffer(b_array)
        #     buffer.open(QIODevice.WriteOnly)
        #     pix.save(buffer, "JPG")
        #     blob = b_array.data()
        if seriesArt != None:
            b_array = QByteArray()
            buffer = QBuffer(b_array)
            buffer.open(QIODevice.WriteOnly)
            seriesArt.save(buffer, "JPG")
            blob = b_array.data()


        else:

            with open('icons/saldb_darkred.png', 'rb') as file:
                blob = file.read()
            file.close()

        
        
        # info_tuple = (blob, self.title, self.englishtitle, self.language, self.start, self.fin, self.type)
        info_tuple = (blob, seriesTitle, seriesEnglishTitle, seriesFormat, seriesStartDate, seriesFinishDate, seriesType, seriesGeneres, seriesThemes)

        # cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type) VALUES (?, ?, ?, ?, ?, ?, ?)", info_tuple)
        cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type, Series_Genres, Series_Themes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_tuple)


        conn.commit()

        conn.close()

    def removeEntry(self):
        pass

    def editEntry(self):
        pass

    def queryDB(self):
        pass