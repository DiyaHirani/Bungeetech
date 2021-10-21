import pandas as pd
import csv
population = pd.read_csv("D://bungee tech//internship-test2-master//input//question-2//main.csv")
print(population.head(5))
a=population.groupby('occupation').min()['age'],population.groupby('occupation').max()['age']
a=pd.DataFrame(a)
with open("D://bungee tech//internship-test2-master//output//answer-2//main.csv","a") as file:
    csvwrite = csv.writer(file)
    col = ['occupation', str(population.groupby('occupation').min()['age']),str( population.groupby('occupation').max()['age'])]
    csvwrite.writerow(col)

print(a)