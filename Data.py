import pandas as pd 
import RandomPasswordGenerator as rd

names=["Joshua","Prince","Gabi","Erica","Narkie","Joyce"]
place=["Teshie","Labadi","Nungua","Bush Road","Kaneshie","Kasoa"]
number=[rd.RandomGenerator(),rd.RandomGenerator(),rd.RandomGenerator(),rd.RandomGenerator(),rd.RandomGenerator(),rd.RandomGenerator()]
Dic={'names':names,'place':place,'number':number}
DataFrame=pd.DataFrame(Dic, columns=["Names","Place","Number"],index=[1,2,3])
print(DataFrame)
