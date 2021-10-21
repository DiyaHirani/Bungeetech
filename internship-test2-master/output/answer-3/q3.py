import pandas as pd

df = pd.read_csv('D://bungee tech//internship-test2-master//input//question-3//main.csv')

yellow = df.sort_values(['Yellow Cards'], ascending=[False])

red = yellow.sort_values(['Red Cards'], ascending=[False])

print(red[['Team', 'Yellow Cards', 'Red Cards']])