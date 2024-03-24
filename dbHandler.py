import sys
import os
import sqlite3
import json
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice
from PyQt5.QtWidgets import QMessageBox

class dbInfo(object):
    def __init__(self):
        pass


    def createDB(self):
        conn = sqlite3.connect('saldb.sqlite')

        cursor = conn.cursor()

        # Create tables for watchlist, to be watched, etc.
            # 'large_image_url',
            # 'title_english',
            # 'title_japanese',
            # 'aired',
            # 'synopsis',
            # 'background',
            # 'year',
            # 'producers',
            # 'licensors',
            # 'studios',
            # 'type',
            # 'episodes',
            # 'status',
            # 'duration',
            # 'genres',
            # 'themes'


        createTable = """
            CREATE TABLE IF NOT EXISTS watchlist(
                art BLOB, title_japanese TEXT PRIMARY KEY, title_english TEXT, format TEXT, date_start TEXT , date_finish TEXT, type TEXT,
                aired TEXT, synopsis TEXT, background TEXT, year TEXT, producers TEXT, licensors TEXT, studios TEXT, air_status TEXT,
                episode_duration TEXT, genres TEXT, themes TEXT
                )
            """

        cursor.execute(createTable)

        conn.commit()
        conn.close()


    def dbLoadTables(self):
        # return sql select all query
        # Something like this maybe...
        # {
        #     'watchlist' : "sql select all query for watchlist table",
        #     'planned' : "sql select all query for planned table"
        # }


        tables = {}

        conn = sqlite3.connect('saldb.sqlite')
        cursor = conn.cursor()

        if os.path.exists('saldb.sqlite'):
            # conn = sqlite3.connect('saldb.sqlite')
            # cursor = conn.cursor()
            print("Database Exists")

        else:
            # qmessagebox to say there was not a 'saldb.sqlite' db found in the directory so a new one will be created.
            # dbFileErrorMsg = QMessageBox.question(self.mainWindow, 'Error - Database Not Found', 'saldb.sqlite db file was not found in the current directory press ok and a new one will be created.', QMessageBox.Ok, QMessageBox.Cancel)

            print("No Database exists...Creating a new database.")
            self.createDB()
            # if dbFileErrorMsg == QMessageBox.Ok:
            #     self.createDB()
            #     # conn = sqlite3.connect('saldb.sqlite')
            #     # cursor = conn.cursor()
            # else:
            #     sys.exit()


        list_tables_query = """SELECT name FROM sqlite_master
        WHERE type='table';"""

        db_tables = cursor.execute(list_tables_query)
        

        for table in db_tables:
            print("DEBUG table variable : ", table)
            for f in table:
                print("THIS IS F : ", f)
                sqlFetchAll = 'SELECT * FROM {}'.format(f)
                print("DEBUG - Fetch All : ", sqlFetchAll)
                result = cursor.execute(sqlFetchAll)
                tables[f] = result.fetchall()

        conn.close()
        print("RETURN VALUE", tables)
        return tables




    def entrySubmit(self, seriesdata):


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

        # just an idea...
        tup = (seriesdata['title'], seriesdata['title_english'], seriesdata['aired'])
        cursor.execute("INSERT INTO watchlist (Art, Title, English_Title, Format, Start_Date ,Completion_Date, Series_Type, Series_Genres, Series_Themes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_tuple)

        conn.commit()

        conn.close()

    def removeEntry(self):
        pass

    def editEntry(self):
        pass

    def queryDB(self):
        pass