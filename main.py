import numpy as np
import pandas as pd

xlsx=pd.ExcelFile('imiona.xlsx')
df1=pd.read_excel(xlsx,header=0)
print(df1)

#zad2a

#print(df1[(df1.Liczba>1000)])

#zad2b

#print(df1[(df1.Imie=='ARKADIUSZ')])

#zad2c
#print((df1.agg({'Liczba':['sum']})))

#zad2d
# dane=(df1[(df1.Rok>1999)&(df1.Rok<2006)])
# print((dane.agg({'Liczba':['sum']})))

#zad2e

chlopcy=(df1[(df1.Plec=='M')])
print((chlopcy.agg({'Liczba':['sum']})))

dziewczynki=(df1[(df1.Plec=='K')])
print((dziewczynki.agg({'Liczba':['sum']})))