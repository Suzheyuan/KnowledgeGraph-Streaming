import pandas as pd
import random

def pick(df, name="name.csv"):
    a100 = df[df["votes"]>3000]
    num = []
    while True:
        a = random.randint(0,a100.shape[0])
        if len(num)<100:
            if a not in num:
                num.append(a)
        else:
            break
    a100 = a100.iloc[num]
    num.clear()
    a100.info()
    a100.to_csv(name, index=False)
    #return a100

amz = pd.read_csv('amazon.csv')
dis = pd.read_csv('disney.csv')
hulu = pd.read_csv('hulu.csv')
nf = pd.read_csv('netflix.csv')


pick(amz, 'amazon100.csv')
pick(hulu, 'hulu100.csv')
pick(nf, 'netflix100.csv')
pick(dis, 'disney100.csv')

