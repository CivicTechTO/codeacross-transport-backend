import csv, sqlite3

# a simple csv to sqlite db file script for CofT bt data

localPath ="enter path of your csv files here"

con = sqlite3.connect(localPath + "bt_toronto.db") #:memory:
cur = con.cursor()

#shp_table
#create table shp_table (segid TEXT, normalspeed REAL, seglength REAL, PRIMARY KEY (segid));
cur.execute("create table IF NOT EXISTS shp_table (segid TEXT, normalspeed REAL, seglength REAL, PRIMARY KEY (segid), UNIQUE (segid) ON CONFLICT IGNORE);") # use your column names here
with open(localPath + 'shp_table.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['segid'], i['normalspeed'], i['seglength']) for i in dr]

cur.executemany("INSERT INTO shp_table (segid, normalspeed,seglength) VALUES (?,?,?);", to_db)
con.commit()

#create table bt_table (id String, segid TEXT, normalspeed REAL, seglength REAL, PRIMARY KEY (id));
cur.execute("create table IF NOT EXISTS bt_table (id INTEGER PRIMARY KEY AUTOINCREMENT, segid TEXT, tt REAL, count REAL, localtime String, UNIQUE (segid, localtime) ON CONFLICT IGNORE);") # use your column names here

with open(localPath + 'bt_2014.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['resultId'], i['timeInSeconds'], i['count'], i['updated']) for i in dr]
cur.executemany("INSERT INTO bt_table (segid, tt, count, localtime) VALUES (?,?,?,?);", to_db)
con.commit()
with open(localPath + 'bt_2015.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['resultId'], i['timeInSeconds'], i['count'], i['updated']) for i in dr]
cur.executemany("INSERT INTO bt_table (segid, tt, count, localtime) VALUES (?,?,?,?);", to_db)
con.commit()
with open(localPath + 'bt_2016.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['resultId'], i['timeInSeconds'], i['count'], i['updated']) for i in dr]
cur.executemany("INSERT INTO bt_table (segid, tt, count, localtime) VALUES (?,?,?,?);", to_db)
con.commit()
with open(localPath + 'bt_2017.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['resultId'], i['timeInSeconds'], i['count'], i['updated']) for i in dr]
cur.executemany("INSERT INTO bt_table (segid, tt, count, localtime) VALUES (?,?,?,?);", to_db)
con.commit()

con.close()