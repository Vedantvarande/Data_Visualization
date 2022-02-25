import random
import plotly.express as px
import plotly.figure_factory as ff
dice_result = []
index = []

for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1+dice2)
    index.append(i)

#fig = px.bar(x=dice_result, y=index)
# fig.show()

fig = ff.create_distplot([dice_result], ["Result"], colors=index, show_hist=False)
fig.show()

