import pandas as pd

df = pd.read_csv('D://bungee tech//internship-test2-master//input//question-3//main.csv')

y = df.sort_values(['Yellow Cards'], ascending=[False])

r = y.sort_values(['Red Cards'], ascending=[False])

print(r[['Team', 'Yellow Cards', 'Red Cards']])
