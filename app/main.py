from flask import Flask, request
import json
from flask-cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def writeToFile(url):
    file = open("urls.json", 'r+', encoding='UTF-8')
    data = json.load(file)
    data["urls"].append(url)
    file.seek(0)
    json.dump(data, file)



def readFromFile():
    file = open("urls.json", 'r+')
    data = json.load(file)
    return data

"""
@app.route("/setUrls")
@cross_origin()
def setUrls():
    url = request.args["url"]
    writeToFile(url)
    return readFromFile()
"""

@app.route("/")
@cross_origin()
def getUrls():
    return readFromFile()


