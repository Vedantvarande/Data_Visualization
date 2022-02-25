import numpy
import csv
import plotly_express as px
import pandas as pd


def graph(data_path):
    with open(data_path) as f:
        #reader = csv.reader(f)
        df = pd.read_csv(f)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()


def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for i in reader:
            coffee.append(float(i["Coffee in ml"]))
            sleep.append(float(i["sleep in hours"]))

    return {"coffee": coffee, "sleep": sleep}


def findCorrelation(data_source):
    a = numpy.corrcoef(data_source["coffee"], data_source["sleep"])
    print("Correlation corficiant is: ", a[0, 1])


def main():
    b = "coffee.csv"
    n = getDataSource(b)
    findCorrelation(n)
    graph(b)


main()
