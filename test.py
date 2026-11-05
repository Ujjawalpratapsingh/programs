import pandas as pd
df = pd.read_csv("number_words-v2.csv")
number = df['Number']
word=df['Word']
lst = pd.Series(word.values,index=number).to_dict()
print(lst)
# print(number)
val=int(input("Enter your number :"))
lst2 = [i for i in val]
print(lst2)