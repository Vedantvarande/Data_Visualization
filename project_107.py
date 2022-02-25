import csv
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go

df = pd.read_csv("pixel_math.csv")

students_data = df.groupby(['student_id', 'level'], as_index=False)[
    "attempt"].mean()

fig = px.scatter(students_data, x="student_id", y="level",
                 size="attempt", color="attempt")
fig.show()
