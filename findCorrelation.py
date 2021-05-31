import plotly.express as px
import csv
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage",size="Marks In Percentage",title="Correlation between marks in percentage and days present",color="Roll No")
        fig.show()

def getdataSource(dataPath):
    marks = []
    daysPresent = []
    with open(dataPath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            daysPresent.append(float(row["Days Present"]))

    return {"x" : marks, "y": daysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Marks in percentage and Days present :",correlation[0,1])

def setup():
    dataPath  = "./Student Marks vs Days Present.csv"

    dataSource = getdataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)

setup()