import pandas as pd
import numpy as np


amz = pd.read_csv('amazon_prime_titles.csv')
disn = pd.read_csv('disney_plus_titles.csv')
hulu = pd.read_csv('hulu_titles.csv')
nf = pd.read_csv('netflix_titles.csv')
stream = [amz,disn,hulu,nf]


for df in stream:
    df.drop(columns=["description","date_added"],inplace=True)

streamdf = pd.concat(stream)
streamdf.to_csv("streaming.csv", index=False)


dfname = pd.read_csv('name.basics.tsv.gz', sep="[\t]", chunksize=1000_000, engine='python', on_bad_lines='skip')

"""
11 chunks
@nconst: alphanumeric unique identifier of the name/person
@primaryName: name by which the person is most often credited
@birthYear – in YYYY format
@deathYear – in YYYY format if applicable, else '\\N';
@primaryProfession (array of strings)– the top-3 professions of the person
DROPED @knownForTitles (array of tconsts) – titles the person is known for
"""
df0=pd.DataFrame()
for data in dfname:
    data.replace(["\\N"], np.nan, inplace=True)
    data.drop(columns=['knownForTitles'],inplace=True)
    data.dropna(subset=['nconst'],inplace=True)
    data.dropna(subset=['primaryName'], inplace=True)
    data.dropna(subset=['birthYear'], inplace=True)

    data.info()
    df0 = pd.concat([df0, data])

df0.head()

df0.to_csv("People Nabirth.csv", chunksize=500_000, index=False)

pp = pd.read_csv("People.csv",chunksize=50_000, engine='python', on_bad_lines='skip')
for d in pp:
    print(d)
    d.info()
    break

#TODO: match with streaming


