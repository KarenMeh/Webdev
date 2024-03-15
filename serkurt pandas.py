import pandas as pd
k = pd.read_csv('QuizScore.csv')
k.fillna('Karen', inplace=True)

print(k)
