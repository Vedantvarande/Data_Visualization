import csv
import plotly_express as px
import pandas as pd
import numpy as np


def graph(data_path):
    with open(data_path) as f:
        #reader = csv.reader(f)
        df = pd.read_csv(f)
        fig = px.scatter(df, x="Temperature", y="Ice-cream Sales")
        fig.show()


def getDataSource(data_path):
    icecream = []
    temperature = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for i in reader:
            icecream.append(float(i["Ice-cream Sales"]))
            temperature.append(float(i["Temperature"]))
    return{"x": icecream, "y": temperature}


def findCorrelation(dataSource):
    result = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation coeffecient is: ", result[0, 1])


def main():
    a = "ice_cream.csv"
    b = getDataSource(a)
    graph(a)
    findCorrelation(b)


main()
