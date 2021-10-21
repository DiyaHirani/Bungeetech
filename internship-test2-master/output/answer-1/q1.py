import pandas as pd
population = pd.read_csv("D://bungee tech//internship-test2-master//input//question-1//main.csv")
population['pop']=population['Population']-population['Population'].shift(1)
p=population.iloc[0,1]
print(f'{p=}')
population['pop']=population['pop'].fillna(p)
#p=population.loc[0:0],['population']
population['dpop']=population['pop']+population['pop'].shift(-1)

a=population
a=population.groupby((population.Year//10)*10).sum()
a.to_csv("D://bungee tech//internship-test2-master//output//answer-1//main.csv")
a.iloc[0,14]=p
print(population.head(10))
print(a.head(5))
