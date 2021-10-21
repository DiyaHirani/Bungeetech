import pandas as pd
import csv
population = pd.read_csv("D://bungee tech//internship-test2-master//input//question-2//main.csv")
print(population.head(5))
a=population.groupby('occupation').min()['age'],population.groupby('occupation').max()['age']
a=pd.DataFrame(a)
a.to_csv("D://bungee tech//internship-test2-master//output//answer-2//main.csv")
print(a)