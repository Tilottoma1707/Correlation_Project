import plotly.express as px
import csv
import numpy as np

def getDataSource():
    Coffee = []
    Sleep = []

    with open("CoffeevsSleep.csv")as f:
        df = csv.DictReader(f)
        for i in df:
            Coffee.append(float(i["Coffee in ml"]))
            Sleep.append(float(i["sleep in hours"]))
    return{"x":Coffee,"y":Sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])
def Setup():
    dataSource = getDataSource()
    findCorrelation(dataSource)
Setup()


