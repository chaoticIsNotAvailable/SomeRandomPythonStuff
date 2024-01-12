
import pandas as pd
article = pd.read_csv('ListOfIdiots.csv', delimiter=';')

names = ['user_id', 'user_name', 'user_age']

print(article)
article.iloc[2, 2] = "hi"
article.to_csv("ListOfIdiots.csv", index=False, sep=";")
print(article)
