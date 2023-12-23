import pandas as pd 
import RandomPasswordGenerator 

rd=RandomPasswordGenerator.RandomGenerator()

names=["Joshua","Prince","Gabi","Erica","Narkie","Joyce"]
place=["Teshie","Labadi","Nungua","Bush Road","Kaneshie","Kasoa"]
password=[rd,rd,rd,rd,rd,rd]
Dic={'names':names,'place':place,'passwrd':password}
DataFrame=pd.DataFrame(Dic)
print(DataFrame)
