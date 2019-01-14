from flask import Flask
import json
import csv
import html

app = Flask(__name__)

@app.route('/all')
def all():
     with open("hotel.csv", "rt") as fileInput:
            fields = ['ID', 'Anzahl_Zimmer', 'QM', 'Preis/Nacht', 'Status']
            csvReader = csv.DictReader(fileInput, fields)
            roomsHotel = [zeile for zeile in csvReader]
            jsonAusgabe = json.dumps(roomsHotel, indent=4)
     return jsonAusgabe

@app.route('/free')
def free():

    with open("hotel.csv", newline ='') as fileInputFrei:
        csvReaderFrei = csv.reader(fileInputFrei)
        frei = []
        for row in csvReaderFrei:
            if (row[4] == "frei"):
                frei.append(row)
        
        jsonausgabeFrei = json.dumps(frei, indent=4)
        return jsonausgabeFrei

@app.route('/booked')
def booked():

    with open("hotel.csv", newline ='') as fileInputFrei:
        csvReaderGeb = csv.reader(fileInputFrei)
        gebucht = []
        for row in csvReaderGeb:
            if (row[4] == "gebucht"):
                gebucht.append(row)
        
        jsonausgabeGeb = json.dumps(gebucht, indent=4)
        return jsonausgabeGeb


if __name__ == '__main__':
	app.run()