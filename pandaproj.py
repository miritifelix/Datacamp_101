#counting the positive sentiments by airline

#importing pandas
import pandas as pd

#oper file
myfile = open('C:/Users/MIRITI/Documents/Datasets/tweets.csv')

#reading from the CSV and storing as dataframe
df = pd.read_csv(myfile, index_col=0)
print(df)

#extracting airline column from df
air_col = df['airline_sentiment']
print(air_col)

#looping into the airline comments while counting
count = 0
neg = 0
neu = 0
for sent in air_col:
    if sent == 'positive':
        count += 1
    elif sent == 'neutral':
        neu += 1
    else:
        neg += 1
print("There are {} psitive sentiments.".format(count))
print(neg)
print(neu)