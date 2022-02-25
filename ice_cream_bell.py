import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("ice_cream.csv")


# fig = px.bar(x=df["Temperature"].tolist(
# ), y=df["Ice-cream Sales"].tolist(), color=df["Temperature"].tolist())

fig = ff.create_distplot(
    [df["Ice-cream Sales"].tolist()], ["Icecream"], show_hist=False)

fig.show()
