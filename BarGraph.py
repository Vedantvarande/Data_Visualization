import pandas as pd

import plotly.express as px

data = pd.read_csv("data.csv")

bar = px.bar(data, x='Country', y='InternetUsers')

bar.show()
